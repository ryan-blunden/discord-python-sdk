"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing_extensions import Annotated, TypedDict


class SearchGuildMembersRequestTypedDict(TypedDict):
    guild_id: str
    limit: int
    query: str


class SearchGuildMembersRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    limit: Annotated[
        int, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]

    query: Annotated[
        str, FieldMetadata(query=QueryParamMetadata(style="form", explode=True))
    ]
