from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Iterator, Optional

from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

load_dotenv()
logger = logging.getLogger(__name__)


@dataclass
class YouTubeChannel:
    channel_id: str
    title: str
    description: str
    custom_url: Optional[str]
    country: Optional[str]
    subscriber_count: Optional[int]
    video_count: Optional[int]
    view_count: Optional[int]

    @property
    def url(self) -> str:
        if self.custom_url:
            handle = self.custom_url if self.custom_url.startswith("@") else f"@{self.custom_url}"
            return f"https://www.youtube.com/{handle}"
        return f"https://www.youtube.com/channel/{self.channel_id}"

    @property
    def handle(self) -> str:
        if self.custom_url:
            return self.custom_url.lstrip("@")
        return self.channel_id


class YouTubeDiscovery:
    def __init__(self, api_key: Optional[str] = None):
        api_key = api_key or os.environ.get("YOUTUBE_API_KEY")
        if not api_key:
            raise RuntimeError(
                "YOUTUBE_API_KEY missing. Set it in .env or pass api_key explicitly."
            )
        self.client = build("youtube", "v3", developerKey=api_key, cache_discovery=False)

    def search_channels(
        self,
        query: str,
        max_results: int = 50,
        region_code: Optional[str] = None,
        relevance_language: Optional[str] = None,
    ) -> list[str]:
        channel_ids: list[str] = []
        page_token: Optional[str] = None
        remaining = max_results
        while remaining > 0:
            batch_size = min(50, remaining)
            try:
                request = self.client.search().list(
                    q=query,
                    type="channel",
                    part="snippet",
                    maxResults=batch_size,
                    pageToken=page_token,
                    regionCode=region_code,
                    relevanceLanguage=relevance_language,
                )
                response = request.execute()
            except HttpError as e:
                logger.error("YouTube search failed for %r: %s", query, e)
                break
            for item in response.get("items", []):
                cid = item["id"].get("channelId")
                if cid:
                    channel_ids.append(cid)
            page_token = response.get("nextPageToken")
            if not page_token:
                break
            remaining -= batch_size
        return channel_ids

    def fetch_channels(self, channel_ids: list[str]) -> Iterator[YouTubeChannel]:
        for batch_start in range(0, len(channel_ids), 50):
            batch = channel_ids[batch_start : batch_start + 50]
            try:
                response = (
                    self.client.channels()
                    .list(
                        id=",".join(batch),
                        part="snippet,statistics,brandingSettings",
                        maxResults=50,
                    )
                    .execute()
                )
            except HttpError as e:
                logger.error("YouTube channels.list failed: %s", e)
                continue
            for item in response.get("items", []):
                yield _parse_channel(item)


def _parse_channel(item: dict) -> YouTubeChannel:
    snippet = item.get("snippet", {})
    stats = item.get("statistics", {})
    branding = item.get("brandingSettings", {}).get("channel", {})
    return YouTubeChannel(
        channel_id=item["id"],
        title=snippet.get("title", ""),
        description=snippet.get("description", ""),
        custom_url=snippet.get("customUrl"),
        country=snippet.get("country") or branding.get("country"),
        subscriber_count=_int_or_none(stats.get("subscriberCount")),
        video_count=_int_or_none(stats.get("videoCount")),
        view_count=_int_or_none(stats.get("viewCount")),
    )


def _int_or_none(v: object) -> Optional[int]:
    if v is None:
        return None
    try:
        return int(v)
    except (TypeError, ValueError):
        return None
