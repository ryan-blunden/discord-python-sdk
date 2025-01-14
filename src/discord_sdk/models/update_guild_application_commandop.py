"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationcommandpatchrequestpartial import (
    ApplicationCommandPatchRequestPartial,
    ApplicationCommandPatchRequestPartialTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateGuildApplicationCommandSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class UpdateGuildApplicationCommandSecurity(BaseModel):
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


class UpdateGuildApplicationCommandRequestTypedDict(TypedDict):
    application_id: str
    guild_id: str
    command_id: str
    application_command_patch_request_partial: (
        ApplicationCommandPatchRequestPartialTypedDict
    )


class UpdateGuildApplicationCommandRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    command_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    application_command_patch_request_partial: Annotated[
        ApplicationCommandPatchRequestPartial,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
