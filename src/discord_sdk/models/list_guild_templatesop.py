"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class ListGuildTemplatesRequestTypedDict(TypedDict):
    guild_id: str


class ListGuildTemplatesRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
