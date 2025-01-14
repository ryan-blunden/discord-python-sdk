"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .welcomescreenpatchrequestpartial import (
    WelcomeScreenPatchRequestPartial,
    WelcomeScreenPatchRequestPartialTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateGuildWelcomeScreenRequestTypedDict(TypedDict):
    guild_id: str
    welcome_screen_patch_request_partial: WelcomeScreenPatchRequestPartialTypedDict


class UpdateGuildWelcomeScreenRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    welcome_screen_patch_request_partial: Annotated[
        WelcomeScreenPatchRequestPartial,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
