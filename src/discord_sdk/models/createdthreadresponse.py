"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .threadmemberresponse import ThreadMemberResponse, ThreadMemberResponseTypedDict
from .threadmetadataresponse import (
    ThreadMetadataResponse,
    ThreadMetadataResponseTypedDict,
)
from datetime import datetime
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from discord_sdk.utils import validate_const
from enum import Enum
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class CreatedThreadResponseType(int, Enum):
    TEN = 10
    ELEVEN = 11
    TWELVE = 12


class CreatedThreadResponseTypedDict(TypedDict):
    id: str
    type: CreatedThreadResponseType
    flags: int
    guild_id: str
    name: str
    owner_id: str
    message_count: int
    member_count: int
    total_message_sent: int
    last_message_id: NotRequired[Nullable[str]]
    last_pin_timestamp: NotRequired[Nullable[datetime]]
    parent_id: NotRequired[Nullable[str]]
    rate_limit_per_user: NotRequired[Nullable[int]]
    bitrate: NotRequired[Nullable[int]]
    user_limit: NotRequired[Nullable[int]]
    rtc_region: NotRequired[Nullable[str]]
    video_quality_mode: Nullable[Literal[1]]
    permissions: NotRequired[Nullable[str]]
    thread_metadata: NotRequired[Nullable[ThreadMetadataResponseTypedDict]]
    applied_tags: NotRequired[Nullable[List[str]]]
    member: NotRequired[Nullable[ThreadMemberResponseTypedDict]]


class CreatedThreadResponse(BaseModel):
    id: str

    type: CreatedThreadResponseType

    flags: int

    guild_id: str

    name: str

    owner_id: str

    message_count: int

    member_count: int

    total_message_sent: int

    last_message_id: OptionalNullable[str] = UNSET

    last_pin_timestamp: OptionalNullable[datetime] = UNSET

    parent_id: OptionalNullable[str] = UNSET

    rate_limit_per_user: OptionalNullable[int] = UNSET

    bitrate: OptionalNullable[int] = UNSET

    user_limit: OptionalNullable[int] = UNSET

    rtc_region: OptionalNullable[str] = UNSET

    VIDEO_QUALITY_MODE: Annotated[
        Annotated[OptionalNullable[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="video_quality_mode"),
    ] = 1

    permissions: OptionalNullable[str] = UNSET

    thread_metadata: OptionalNullable[ThreadMetadataResponse] = UNSET

    applied_tags: OptionalNullable[List[str]] = UNSET

    member: OptionalNullable[ThreadMemberResponse] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "last_message_id",
            "last_pin_timestamp",
            "parent_id",
            "rate_limit_per_user",
            "bitrate",
            "user_limit",
            "rtc_region",
            "video_quality_mode",
            "permissions",
            "thread_metadata",
            "applied_tags",
            "member",
        ]
        nullable_fields = [
            "last_message_id",
            "last_pin_timestamp",
            "parent_id",
            "rate_limit_per_user",
            "bitrate",
            "user_limit",
            "rtc_region",
            "video_quality_mode",
            "permissions",
            "thread_metadata",
            "applied_tags",
            "member",
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
