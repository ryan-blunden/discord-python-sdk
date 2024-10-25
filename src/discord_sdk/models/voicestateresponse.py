"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .guildmemberresponse import GuildMemberResponse, GuildMemberResponseTypedDict
from datetime import datetime
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class VoiceStateResponseTypedDict(TypedDict):
    deaf: bool
    mute: bool
    suppress: bool
    self_deaf: bool
    self_mute: bool
    self_video: bool
    session_id: str
    user_id: str
    channel_id: NotRequired[Nullable[str]]
    guild_id: NotRequired[Nullable[str]]
    member: NotRequired[Nullable[GuildMemberResponseTypedDict]]
    request_to_speak_timestamp: NotRequired[Nullable[datetime]]
    self_stream: NotRequired[Nullable[bool]]


class VoiceStateResponse(BaseModel):
    deaf: bool

    mute: bool

    suppress: bool

    self_deaf: bool

    self_mute: bool

    self_video: bool

    session_id: str

    user_id: str

    channel_id: OptionalNullable[str] = UNSET

    guild_id: OptionalNullable[str] = UNSET

    member: OptionalNullable[GuildMemberResponse] = UNSET

    request_to_speak_timestamp: OptionalNullable[datetime] = UNSET

    self_stream: OptionalNullable[bool] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "channel_id",
            "guild_id",
            "member",
            "request_to_speak_timestamp",
            "self_stream",
        ]
        nullable_fields = [
            "channel_id",
            "guild_id",
            "member",
            "request_to_speak_timestamp",
            "self_stream",
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