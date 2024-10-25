"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from typing_extensions import TypedDict


class GithubRepositoryTypedDict(TypedDict):
    id: int
    html_url: str
    name: str
    full_name: str


class GithubRepository(BaseModel):
    id: int

    html_url: str

    name: str

    full_name: str