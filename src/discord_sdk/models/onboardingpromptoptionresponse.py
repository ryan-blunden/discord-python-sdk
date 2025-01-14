"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .settingsemojiresponse import SettingsEmojiResponse, SettingsEmojiResponseTypedDict
from discord_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OnboardingPromptOptionResponseTypedDict(TypedDict):
    id: str
    title: str
    description: str
    emoji: SettingsEmojiResponseTypedDict
    role_ids: List[str]
    channel_ids: List[str]


class OnboardingPromptOptionResponse(BaseModel):
    id: str

    title: str

    description: str

    emoji: SettingsEmojiResponse

    role_ids: List[str]

    channel_ids: List[str]
