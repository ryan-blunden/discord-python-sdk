"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userresponse import UserResponse, UserResponseTypedDict
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class SoundboardSoundResponseTypedDict(TypedDict):
    name: str
    sound_id: str
    volume: float
    available: bool
    emoji_id: NotRequired[Nullable[str]]
    emoji_name: NotRequired[Nullable[str]]
    guild_id: NotRequired[Nullable[str]]
    user: NotRequired[Nullable[UserResponseTypedDict]]


class SoundboardSoundResponse(BaseModel):
    name: str

    sound_id: str

    volume: float

    available: bool

    emoji_id: OptionalNullable[str] = UNSET

    emoji_name: OptionalNullable[str] = UNSET

    guild_id: OptionalNullable[str] = UNSET

    user: OptionalNullable[UserResponse] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["emoji_id", "emoji_name", "guild_id", "user"]
        nullable_fields = ["emoji_id", "emoji_name", "guild_id", "user"]
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