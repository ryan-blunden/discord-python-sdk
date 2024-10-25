"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UploadApplicationAttachmentSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class UploadApplicationAttachmentSecurity(BaseModel):
    bot_token: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="apiKey",
                sub_type="header",
                field_name="Authorization",
            )
        ),
    ] = None


class UploadApplicationAttachmentRequestBodyTypedDict(TypedDict):
    file: str


class UploadApplicationAttachmentRequestBody(BaseModel):
    file: Annotated[str, FieldMetadata(multipart=True)]


class UploadApplicationAttachmentRequestTypedDict(TypedDict):
    application_id: str
    request_body: UploadApplicationAttachmentRequestBodyTypedDict


class UploadApplicationAttachmentRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        UploadApplicationAttachmentRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="multipart/form-data")),
    ]