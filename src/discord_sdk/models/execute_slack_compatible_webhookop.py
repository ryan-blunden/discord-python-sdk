"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .slackwebhook import SlackWebhook, SlackWebhookTypedDict
from discord_sdk.types import BaseModel
from discord_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    QueryParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ExecuteSlackCompatibleWebhookSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class ExecuteSlackCompatibleWebhookSecurity(BaseModel):
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


class ExecuteSlackCompatibleWebhookRequestTypedDict(TypedDict):
    webhook_id: str
    webhook_token: str
    slack_webhook: SlackWebhookTypedDict
    wait: NotRequired[bool]
    thread_id: NotRequired[str]


class ExecuteSlackCompatibleWebhookRequest(BaseModel):
    webhook_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    webhook_token: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    slack_webhook: Annotated[
        SlackWebhook,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    wait: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    thread_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None