"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .guildtemplatechannelresponse import (
    GuildTemplateChannelResponse,
    GuildTemplateChannelResponseTypedDict,
)
from .guildtemplateroleresponse import (
    GuildTemplateRoleResponse,
    GuildTemplateRoleResponseTypedDict,
)
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from discord_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class GuildTemplateSnapshotResponseTypedDict(TypedDict):
    name: str
    system_channel_flags: int
    roles: List[GuildTemplateRoleResponseTypedDict]
    channels: List[GuildTemplateChannelResponseTypedDict]
    description: NotRequired[Nullable[str]]
    region: NotRequired[Nullable[str]]
    verification_level: Literal[0]
    default_message_notifications: Literal[0]
    explicit_content_filter: Literal[0]
    preferred_locale: Literal["ar"]
    afk_channel_id: NotRequired[Nullable[str]]
    afk_timeout: Literal[60]
    system_channel_id: NotRequired[Nullable[str]]


class GuildTemplateSnapshotResponse(BaseModel):
    name: str

    system_channel_flags: int

    roles: List[GuildTemplateRoleResponse]

    channels: List[GuildTemplateChannelResponse]

    description: OptionalNullable[str] = UNSET

    region: OptionalNullable[str] = UNSET

    VERIFICATION_LEVEL: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="verification_level"),
    ] = 0

    DEFAULT_MESSAGE_NOTIFICATIONS: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="default_message_notifications"),
    ] = 0

    EXPLICIT_CONTENT_FILTER: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="explicit_content_filter"),
    ] = 0

    PREFERRED_LOCALE: Annotated[
        Annotated[Literal["ar"], AfterValidator(validate_const("ar"))],
        pydantic.Field(alias="preferred_locale"),
    ] = "ar"

    afk_channel_id: OptionalNullable[str] = UNSET

    AFK_TIMEOUT: Annotated[
        Annotated[Literal[60], AfterValidator(validate_const(60))],
        pydantic.Field(alias="afk_timeout"),
    ] = 60

    system_channel_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "region",
            "afk_channel_id",
            "system_channel_id",
        ]
        nullable_fields = [
            "description",
            "region",
            "afk_channel_id",
            "system_channel_id",
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
