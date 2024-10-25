"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .channelselectdefaultvalue import (
    ChannelSelectDefaultValue,
    ChannelSelectDefaultValueTypedDict,
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


class ChannelSelectTypedDict(TypedDict):
    custom_id: str
    type: Literal[1]
    placeholder: NotRequired[Nullable[str]]
    min_values: NotRequired[Nullable[int]]
    max_values: NotRequired[Nullable[int]]
    disabled: NotRequired[Nullable[bool]]
    default_values: NotRequired[Nullable[List[ChannelSelectDefaultValueTypedDict]]]
    channel_types: NotRequired[Nullable[List[int]]]


class ChannelSelect(BaseModel):
    custom_id: str

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1

    placeholder: OptionalNullable[str] = UNSET

    min_values: OptionalNullable[int] = UNSET

    max_values: OptionalNullable[int] = UNSET

    disabled: OptionalNullable[bool] = UNSET

    default_values: OptionalNullable[List[ChannelSelectDefaultValue]] = UNSET

    channel_types: OptionalNullable[List[int]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "placeholder",
            "min_values",
            "max_values",
            "disabled",
            "default_values",
            "channel_types",
        ]
        nullable_fields = [
            "placeholder",
            "min_values",
            "max_values",
            "disabled",
            "default_values",
            "channel_types",
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
