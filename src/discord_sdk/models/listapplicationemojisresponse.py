"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .emojiresponse import EmojiResponse, EmojiResponseTypedDict
from discord_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListApplicationEmojisResponseTypedDict(TypedDict):
    items: List[EmojiResponseTypedDict]


class ListApplicationEmojisResponse(BaseModel):
    items: List[EmojiResponse]
