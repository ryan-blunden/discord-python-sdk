"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channelpermissionoverwriterequest import (
    ChannelPermissionOverwriteRequest,
    ChannelPermissionOverwriteRequestTypedDict,
)
from .createorupdatethreadtagrequest import (
    CreateOrUpdateThreadTagRequest,
    CreateOrUpdateThreadTagRequestTypedDict,
)
from .updatedefaultreactionemojirequest import (
    UpdateDefaultReactionEmojiRequest,
    UpdateDefaultReactionEmojiRequestTypedDict,
)
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


class CreateGuildRequestChannelItemType(int, Enum):
    ZERO = 0
    TWO = 2
    FOUR = 4


class CreateGuildRequestChannelItemTypedDict(TypedDict):
    name: str
    type: NotRequired[Nullable[CreateGuildRequestChannelItemType]]
    position: NotRequired[Nullable[int]]
    topic: NotRequired[Nullable[str]]
    bitrate: NotRequired[Nullable[int]]
    user_limit: NotRequired[Nullable[int]]
    nsfw: NotRequired[Nullable[bool]]
    rate_limit_per_user: NotRequired[Nullable[int]]
    parent_id: NotRequired[Nullable[str]]
    permission_overwrites: NotRequired[
        Nullable[List[ChannelPermissionOverwriteRequestTypedDict]]
    ]
    rtc_region: NotRequired[Nullable[str]]
    video_quality_mode: Nullable[Literal[1]]
    default_auto_archive_duration: Nullable[Literal[60]]
    default_reaction_emoji: NotRequired[
        Nullable[UpdateDefaultReactionEmojiRequestTypedDict]
    ]
    default_thread_rate_limit_per_user: NotRequired[Nullable[int]]
    default_sort_order: Nullable[Literal[0]]
    default_forum_layout: Nullable[Literal[0]]
    id: NotRequired[Nullable[str]]
    available_tags: NotRequired[Nullable[List[CreateOrUpdateThreadTagRequestTypedDict]]]


class CreateGuildRequestChannelItem(BaseModel):
    name: str

    type: OptionalNullable[CreateGuildRequestChannelItemType] = UNSET

    position: OptionalNullable[int] = UNSET

    topic: OptionalNullable[str] = UNSET

    bitrate: OptionalNullable[int] = UNSET

    user_limit: OptionalNullable[int] = UNSET

    nsfw: OptionalNullable[bool] = UNSET

    rate_limit_per_user: OptionalNullable[int] = UNSET

    parent_id: OptionalNullable[str] = UNSET

    permission_overwrites: OptionalNullable[List[ChannelPermissionOverwriteRequest]] = (
        UNSET
    )

    rtc_region: OptionalNullable[str] = UNSET

    VIDEO_QUALITY_MODE: Annotated[
        Annotated[OptionalNullable[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="video_quality_mode"),
    ] = 1

    DEFAULT_AUTO_ARCHIVE_DURATION: Annotated[
        Annotated[OptionalNullable[Literal[60]], AfterValidator(validate_const(60))],
        pydantic.Field(alias="default_auto_archive_duration"),
    ] = 60

    default_reaction_emoji: OptionalNullable[UpdateDefaultReactionEmojiRequest] = UNSET

    default_thread_rate_limit_per_user: OptionalNullable[int] = UNSET

    DEFAULT_SORT_ORDER: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="default_sort_order"),
    ] = 0

    DEFAULT_FORUM_LAYOUT: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="default_forum_layout"),
    ] = 0

    id: OptionalNullable[str] = UNSET

    available_tags: OptionalNullable[List[CreateOrUpdateThreadTagRequest]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "position",
            "topic",
            "bitrate",
            "user_limit",
            "nsfw",
            "rate_limit_per_user",
            "parent_id",
            "permission_overwrites",
            "rtc_region",
            "video_quality_mode",
            "default_auto_archive_duration",
            "default_reaction_emoji",
            "default_thread_rate_limit_per_user",
            "default_sort_order",
            "default_forum_layout",
            "id",
            "available_tags",
        ]
        nullable_fields = [
            "type",
            "position",
            "topic",
            "bitrate",
            "user_limit",
            "nsfw",
            "rate_limit_per_user",
            "parent_id",
            "permission_overwrites",
            "rtc_region",
            "video_quality_mode",
            "default_auto_archive_duration",
            "default_reaction_emoji",
            "default_thread_rate_limit_per_user",
            "default_sort_order",
            "default_forum_layout",
            "id",
            "available_tags",
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
