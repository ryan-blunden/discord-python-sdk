"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .entitymetadatavoice import EntityMetadataVoice, EntityMetadataVoiceTypedDict
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
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class VoiceScheduledEventCreateRequestTypedDict(TypedDict):
    name: str
    scheduled_start_time: datetime
    description: NotRequired[Nullable[str]]
    image: NotRequired[Nullable[str]]
    scheduled_end_time: NotRequired[Nullable[datetime]]
    privacy_level: Literal[2]
    entity_type: Literal[0]
    channel_id: NotRequired[Nullable[str]]
    entity_metadata: NotRequired[Nullable[EntityMetadataVoiceTypedDict]]


class VoiceScheduledEventCreateRequest(BaseModel):
    name: str

    scheduled_start_time: datetime

    description: OptionalNullable[str] = UNSET

    image: OptionalNullable[str] = UNSET

    scheduled_end_time: OptionalNullable[datetime] = UNSET

    PRIVACY_LEVEL: Annotated[
        Annotated[Literal[2], AfterValidator(validate_const(2))],
        pydantic.Field(alias="privacy_level"),
    ] = 2

    ENTITY_TYPE: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="entity_type"),
    ] = 0

    channel_id: OptionalNullable[str] = UNSET

    entity_metadata: OptionalNullable[EntityMetadataVoice] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "description",
            "image",
            "scheduled_end_time",
            "channel_id",
            "entity_metadata",
        ]
        nullable_fields = [
            "description",
            "image",
            "scheduled_end_time",
            "channel_id",
            "entity_metadata",
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
