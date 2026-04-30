"""
0430 신규 풀 중 이메일 0개 채널(234개) 의 최신 영상 description 에서 이메일/외부링크 추출.

YouTube creator 들이 채널 bio 보다 영상 description 끝에 비즈 이메일을 박는 패턴이 흔해서,
extract 단계가 채널 bio 만 보는 한계를 보완.

quota: 채널당 channels.list(forHandle, contentDetails) 1 + playlistItems.list 1 ≈ 2 units
       → 234 채널 × 2 = ~470 units (오늘 잔여 8.5K 안에 충분)

emails 테이블 source_url = 영상 URL, raw_context 는 description 일부 → "no hallucinated emails"
invariant 그대로 유지 (사람이 영상 설명에서 ctrl+F 검증 가능).
"""

from __future__ import annotations

import os
import sqlite3
import sys
from pathlib import Path

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
load_dotenv(ROOT / ".env")

from influencer_finder.extractors.bio import extract_bio_links  # noqa: E402
from influencer_finder.extractors.email_regex import extract_emails  # noqa: E402

DB = ROOT / "influencer.db"


def main() -> int:
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if not api_key:
        print("YOUTUBE_API_KEY missing", file=sys.stderr)
        return 1
    yt = build("youtube", "v3", developerKey=api_key, cache_discovery=False)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute(
        """
        SELECT p.id, p.handle, p.url
        FROM profiles p
        LEFT JOIN emails e ON e.profile_id = p.id
        WHERE date(p.discovered_at) = '2026-04-30' AND e.id IS NULL
        ORDER BY p.follower_count DESC NULLS LAST
        """
    )
    targets = cur.fetchall()
    print(f"targets: {len(targets)} channels")

    new_emails = 0
    new_sources = 0
    handle_failed = 0
    no_videos = 0
    quota_used = 0

    for i, (pid, handle, channel_url) in enumerate(targets, 1):
        # Step 1: handle → channel_id + uploads playlist
        try:
            ch_resp = (
                yt.channels()
                .list(forHandle=f"@{handle}", part="id,contentDetails")
                .execute()
            )
            quota_used += 1
        except HttpError as e:
            if "quotaExceeded" in str(e):
                print(f"QUOTA EXCEEDED at {i}/{len(targets)}")
                break
            handle_failed += 1
            continue
        items = ch_resp.get("items", [])
        if not items:
            handle_failed += 1
            continue
        uploads = (
            items[0].get("contentDetails", {}).get("relatedPlaylists", {}).get("uploads")
        )
        if not uploads:
            no_videos += 1
            continue

        # Step 2: latest 10 videos description
        try:
            pl_resp = (
                yt.playlistItems()
                .list(
                    playlistId=uploads,
                    maxResults=10,
                    part="snippet,contentDetails",
                )
                .execute()
            )
            quota_used += 1
        except HttpError as e:
            if "quotaExceeded" in str(e):
                print(f"QUOTA EXCEEDED at {i}/{len(targets)}")
                break
            continue

        videos: list[tuple[str, str]] = []
        for vi in pl_resp.get("items", []):
            sn = vi.get("snippet", {}) or {}
            cd = vi.get("contentDetails", {}) or {}
            video_id = cd.get("videoId") or sn.get("resourceId", {}).get("videoId")
            desc = sn.get("description", "") or ""
            if not video_id or not desc:
                continue
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((video_url, desc))

        if not videos:
            no_videos += 1
            continue

        # Step 3: extract emails + links from each description
        seen_emails: set[str] = set()
        for video_url, desc in videos:
            for ex in extract_emails(desc):
                key = ex.email.lower()
                if key in seen_emails:
                    continue
                seen_emails.add(key)
                cur.execute(
                    """
                    INSERT OR IGNORE INTO emails(
                        profile_id, email, source_url, raw_context, extraction_method
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (pid, ex.email, video_url, ex.raw_context, ex.method),
                )
                if cur.rowcount:
                    new_emails += 1

            links = extract_bio_links(desc)
            for u in links.link_in_bio_urls + links.personal_domain_urls:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO sources(profile_id, url, type)
                    VALUES (?, ?, ?)
                    """,
                    (pid, u, "external_link"),
                )
                if cur.rowcount:
                    new_sources += 1

        if i % 25 == 0:
            conn.commit()
            print(
                f"[{i}/{len(targets)}] quota={quota_used} "
                f"new_emails={new_emails} new_sources={new_sources}"
            )

    conn.commit()
    print(
        f"DONE. quota={quota_used} new_emails={new_emails} new_sources={new_sources} "
        f"handle_failed={handle_failed} no_videos={no_videos}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
