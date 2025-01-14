"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class FollowChannelRequestBodyTypedDict(TypedDict):
    webhook_channel_id: str


class FollowChannelRequestBody(BaseModel):
    webhook_channel_id: str


class FollowChannelRequestTypedDict(TypedDict):
    channel_id: str
    request_body: FollowChannelRequestBodyTypedDict


class FollowChannelRequest(BaseModel):
    channel_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        FollowChannelRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
