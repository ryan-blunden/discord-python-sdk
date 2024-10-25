"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .incomingwebhookupdaterequestpartial import (
    IncomingWebhookUpdateRequestPartial,
    IncomingWebhookUpdateRequestPartialTypedDict,
)
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


class UpdateOriginalWebhookMessageJSONSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class UpdateOriginalWebhookMessageJSONSecurity(BaseModel):
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


class UpdateOriginalWebhookMessageJSONRequestTypedDict(TypedDict):
    webhook_id: str
    webhook_token: str
    incoming_webhook_update_request_partial: (
        IncomingWebhookUpdateRequestPartialTypedDict
    )
    thread_id: NotRequired[str]


class UpdateOriginalWebhookMessageJSONRequest(BaseModel):
    webhook_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    webhook_token: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    incoming_webhook_update_request_partial: Annotated[
        IncomingWebhookUpdateRequestPartial,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    thread_id: Annotated[
        Optional[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None