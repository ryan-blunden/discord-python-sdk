"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from typing_extensions import TypedDict


class WidgetActivityTypedDict(TypedDict):
    name: str


class WidgetActivity(BaseModel):
    name: str
