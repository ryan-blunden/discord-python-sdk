"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from typing_extensions import TypedDict


class GithubCheckAppTypedDict(TypedDict):
    name: str


class GithubCheckApp(BaseModel):
    name: str
