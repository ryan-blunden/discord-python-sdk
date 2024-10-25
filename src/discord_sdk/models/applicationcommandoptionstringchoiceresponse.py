"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class ApplicationCommandOptionStringChoiceResponseTypedDict(TypedDict):
    name: str
    value: str
    name_localized: NotRequired[Nullable[str]]
    name_localizations: NotRequired[Nullable[Dict[str, str]]]


class ApplicationCommandOptionStringChoiceResponse(BaseModel):
    name: str

    value: str

    name_localized: OptionalNullable[str] = UNSET

    name_localizations: OptionalNullable[Dict[str, str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["name_localized", "name_localizations"]
        nullable_fields = ["name_localized", "name_localizations"]
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
