"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .useravatardecorationresponse import (
    UserAvatarDecorationResponse,
    UserAvatarDecorationResponseTypedDict,
)
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class UserResponseTypedDict(TypedDict):
    id: str
    username: str
    discriminator: str
    public_flags: int
    flags: int
    avatar: NotRequired[Nullable[str]]
    bot: NotRequired[Nullable[bool]]
    system: NotRequired[Nullable[bool]]
    banner: NotRequired[Nullable[str]]
    accent_color: NotRequired[Nullable[int]]
    global_name: NotRequired[Nullable[str]]
    avatar_decoration_data: NotRequired[Nullable[UserAvatarDecorationResponseTypedDict]]


class UserResponse(BaseModel):
    id: str

    username: str

    discriminator: str

    public_flags: int

    flags: int

    avatar: OptionalNullable[str] = UNSET

    bot: OptionalNullable[bool] = UNSET

    system: OptionalNullable[bool] = UNSET

    banner: OptionalNullable[str] = UNSET

    accent_color: OptionalNullable[int] = UNSET

    global_name: OptionalNullable[str] = UNSET

    avatar_decoration_data: OptionalNullable[UserAvatarDecorationResponse] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "avatar",
            "bot",
            "system",
            "banner",
            "accent_color",
            "global_name",
            "avatar_decoration_data",
        ]
        nullable_fields = [
            "avatar",
            "bot",
            "system",
            "banner",
            "accent_color",
            "global_name",
            "avatar_decoration_data",
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
