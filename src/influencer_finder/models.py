from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field

Platform = Literal["youtube", "instagram", "tiktok", "website"]
SourceType = Literal["channel_description", "external_link", "website", "bio"]
ExtractionMethod = Literal["regex_direct", "mailto_href", "deobfuscated"]


class Profile(BaseModel):
    id: Optional[int] = None
    platform: Platform
    handle: str
    display_name: Optional[str] = None
    url: str
    follower_count: Optional[int] = None
    bio: Optional[str] = None
    country: Optional[str] = None
    discovered_at: Optional[datetime] = None


class Email(BaseModel):
    id: Optional[int] = None
    profile_id: int
    email: str
    syntax_valid: Optional[bool] = None
    has_mx: Optional[bool] = None
    is_role_based: Optional[bool] = None
    source_url: str
    raw_context: str = Field(description="100 chars surrounding the extracted email for manual verification")
    extraction_method: ExtractionMethod
    extracted_at: Optional[datetime] = None


class Source(BaseModel):
    id: Optional[int] = None
    profile_id: int
    url: str
    type: SourceType
    fetched_at: Optional[datetime] = None
    success: Optional[bool] = None
