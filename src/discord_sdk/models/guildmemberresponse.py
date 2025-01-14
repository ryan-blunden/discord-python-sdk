"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .useravatardecorationresponse import (
    UserAvatarDecorationResponse,
    UserAvatarDecorationResponseTypedDict,
)
from .userresponse import UserResponse, UserResponseTypedDict
from datetime import datetime
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


class GuildMemberResponseTypedDict(TypedDict):
    flags: int
    joined_at: datetime
    pending: bool
    roles: List[str]
    user: UserResponseTypedDict
    mute: bool
    deaf: bool
    avatar: NotRequired[Nullable[str]]
    avatar_decoration_data: NotRequired[Nullable[UserAvatarDecorationResponseTypedDict]]
    banner: NotRequired[Nullable[str]]
    communication_disabled_until: NotRequired[Nullable[datetime]]
    nick: NotRequired[Nullable[str]]
    premium_since: NotRequired[Nullable[datetime]]


class GuildMemberResponse(BaseModel):
    flags: int

    joined_at: datetime

    pending: bool

    roles: List[str]

    user: UserResponse

    mute: bool

    deaf: bool

    avatar: OptionalNullable[str] = UNSET

    avatar_decoration_data: OptionalNullable[UserAvatarDecorationResponse] = UNSET

    banner: OptionalNullable[str] = UNSET

    communication_disabled_until: OptionalNullable[datetime] = UNSET

    nick: OptionalNullable[str] = UNSET

    premium_since: OptionalNullable[datetime] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "avatar",
            "avatar_decoration_data",
            "banner",
            "communication_disabled_until",
            "nick",
            "premium_since",
        ]
        nullable_fields = [
            "avatar",
            "avatar_decoration_data",
            "banner",
            "communication_disabled_until",
            "nick",
            "premium_since",
        ]
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
