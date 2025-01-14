"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entitymetadataexternal import (
    EntityMetadataExternal,
    EntityMetadataExternalTypedDict,
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
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ExternalScheduledEventPatchRequestPartialTypedDict(TypedDict):
    status: Nullable[Literal[1]]
    name: NotRequired[str]
    description: NotRequired[Nullable[str]]
    image: NotRequired[Nullable[str]]
    scheduled_start_time: NotRequired[datetime]
    scheduled_end_time: NotRequired[Nullable[datetime]]
    entity_type: Literal[0]
    privacy_level: Literal[2]
    channel_id: NotRequired[Nullable[str]]
    entity_metadata: NotRequired[EntityMetadataExternalTypedDict]


class ExternalScheduledEventPatchRequestPartial(BaseModel):
    STATUS: Annotated[
        Annotated[OptionalNullable[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="status"),
    ] = 1

    name: Optional[str] = None

    description: OptionalNullable[str] = UNSET

    image: OptionalNullable[str] = UNSET

    scheduled_start_time: Optional[datetime] = None

    scheduled_end_time: OptionalNullable[datetime] = UNSET

    ENTITY_TYPE: Annotated[
        Annotated[Optional[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="entity_type"),
    ] = 0

    PRIVACY_LEVEL: Annotated[
        Annotated[Optional[Literal[2]], AfterValidator(validate_const(2))],
        pydantic.Field(alias="privacy_level"),
    ] = 2

    channel_id: OptionalNullable[str] = UNSET

    entity_metadata: Optional[EntityMetadataExternal] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "status",
            "name",
            "description",
            "image",
            "scheduled_start_time",
            "scheduled_end_time",
            "entity_type",
            "privacy_level",
            "channel_id",
            "entity_metadata",
        ]
        nullable_fields = [
            "status",
            "description",
            "image",
            "scheduled_end_time",
            "channel_id",
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
