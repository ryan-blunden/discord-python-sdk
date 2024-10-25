"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class CreateApplicationEmojiRequestBodyTypedDict(TypedDict):
    name: str
    image: str


class CreateApplicationEmojiRequestBody(BaseModel):
    name: str

    image: str


class CreateApplicationEmojiRequestTypedDict(TypedDict):
    application_id: str
    request_body: CreateApplicationEmojiRequestBodyTypedDict


class CreateApplicationEmojiRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        CreateApplicationEmojiRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
