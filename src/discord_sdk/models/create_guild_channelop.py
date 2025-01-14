"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createguildchannelrequest import (
    CreateGuildChannelRequest,
    CreateGuildChannelRequestTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class CreateGuildChannelRequest1TypedDict(TypedDict):
    guild_id: str
    create_guild_channel_request: CreateGuildChannelRequestTypedDict


class CreateGuildChannelRequest1(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    create_guild_channel_request: Annotated[
        CreateGuildChannelRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
