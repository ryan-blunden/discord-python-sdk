"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .newmemberactionresponse import (
    NewMemberActionResponse,
    NewMemberActionResponseTypedDict,
)
from .resourcechannelresponse import (
    ResourceChannelResponse,
    ResourceChannelResponseTypedDict,
)
from .welcomemessageresponse import (
    WelcomeMessageResponse,
    WelcomeMessageResponseTypedDict,
)
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class GuildHomeSettingsResponseTypedDict(TypedDict):
    guild_id: str
    enabled: bool
    welcome_message: NotRequired[Nullable[WelcomeMessageResponseTypedDict]]
    new_member_actions: NotRequired[Nullable[List[NewMemberActionResponseTypedDict]]]
    resource_channels: NotRequired[Nullable[List[ResourceChannelResponseTypedDict]]]


class GuildHomeSettingsResponse(BaseModel):
    guild_id: str

    enabled: bool

    welcome_message: OptionalNullable[WelcomeMessageResponse] = UNSET

    new_member_actions: OptionalNullable[List[NewMemberActionResponse]] = UNSET

    resource_channels: OptionalNullable[List[ResourceChannelResponse]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["welcome_message", "new_member_actions", "resource_channels"]
        nullable_fields = ["welcome_message", "new_member_actions", "resource_channels"]
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