"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationcommandcreaterequest import (
    ApplicationCommandCreateRequest,
    ApplicationCommandCreateRequestTypedDict,
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


class CreateGuildApplicationCommandSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class CreateGuildApplicationCommandSecurity(BaseModel):
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


class CreateGuildApplicationCommandRequestTypedDict(TypedDict):
    application_id: str
    guild_id: str
    application_command_create_request: ApplicationCommandCreateRequestTypedDict


class CreateGuildApplicationCommandRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    application_command_create_request: Annotated[
        ApplicationCommandCreateRequest,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
