"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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


class StageInstanceResponseTypedDict(TypedDict):
    guild_id: str
    channel_id: str
    topic: str
    id: str
    privacy_level: Literal[1]
    discoverable_disabled: NotRequired[Nullable[bool]]
    guild_scheduled_event_id: NotRequired[Nullable[str]]


class StageInstanceResponse(BaseModel):
    guild_id: str

    channel_id: str

    topic: str

    id: str

    PRIVACY_LEVEL: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="privacy_level"),
    ] = 1

    discoverable_disabled: OptionalNullable[bool] = UNSET

    guild_scheduled_event_id: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["discoverable_disabled", "guild_scheduled_event_id"]
        nullable_fields = ["discoverable_disabled", "guild_scheduled_event_id"]
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
