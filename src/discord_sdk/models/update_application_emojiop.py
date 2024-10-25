"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateApplicationEmojiRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]


class UpdateApplicationEmojiRequestBody(BaseModel):
    name: Optional[str] = None


class UpdateApplicationEmojiRequestTypedDict(TypedDict):
    application_id: str
    emoji_id: str
    request_body: UpdateApplicationEmojiRequestBodyTypedDict


class UpdateApplicationEmojiRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    emoji_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        UpdateApplicationEmojiRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]