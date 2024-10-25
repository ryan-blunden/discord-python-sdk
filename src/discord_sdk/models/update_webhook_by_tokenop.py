"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationincomingwebhookresponse import (
    ApplicationIncomingWebhookResponse,
    ApplicationIncomingWebhookResponseTypedDict,
)
from .channelfollowerwebhookresponse import (
    ChannelFollowerWebhookResponse,
    ChannelFollowerWebhookResponseTypedDict,
)
from .guildincomingwebhookresponse import (
    GuildIncomingWebhookResponse,
    GuildIncomingWebhookResponseTypedDict,
)
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from discord_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
    SecurityMetadata,
)
from pydantic import model_serializer
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateWebhookByTokenSecurityTypedDict(TypedDict):
    bot_token: NotRequired[str]


class UpdateWebhookByTokenSecurity(BaseModel):
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


class UpdateWebhookByTokenRequestBodyTypedDict(TypedDict):
    name: NotRequired[str]
    avatar: NotRequired[Nullable[str]]


class UpdateWebhookByTokenRequestBody(BaseModel):
    name: Optional[str] = None

    avatar: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name", "avatar"]
        nullable_fields = ["avatar"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class UpdateWebhookByTokenRequestTypedDict(TypedDict):
    webhook_id: str
    webhook_token: str
    request_body: UpdateWebhookByTokenRequestBodyTypedDict


class UpdateWebhookByTokenRequest(BaseModel):
    webhook_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    webhook_token: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        UpdateWebhookByTokenRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


UpdateWebhookByTokenResponseBodyTypedDict = Union[
    ApplicationIncomingWebhookResponseTypedDict,
    ChannelFollowerWebhookResponseTypedDict,
    GuildIncomingWebhookResponseTypedDict,
]
r"""200 response for update_webhook_by_token"""


UpdateWebhookByTokenResponseBody = Union[
    ApplicationIncomingWebhookResponse,
    ChannelFollowerWebhookResponse,
    GuildIncomingWebhookResponse,
]
r"""200 response for update_webhook_by_token"""
