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
from typing_extensions import NotRequired, TypedDict


class CreateGuildRequestRoleItemTypedDict(TypedDict):
    id: int
    name: NotRequired[Nullable[str]]
    permissions: NotRequired[Nullable[int]]
    color: NotRequired[Nullable[int]]
    hoist: NotRequired[Nullable[bool]]
    mentionable: NotRequired[Nullable[bool]]
    unicode_emoji: NotRequired[Nullable[str]]


class CreateGuildRequestRoleItem(BaseModel):
    id: int

    name: OptionalNullable[str] = UNSET

    permissions: OptionalNullable[int] = UNSET

    color: OptionalNullable[int] = UNSET

    hoist: OptionalNullable[bool] = UNSET

    mentionable: OptionalNullable[bool] = UNSET

    unicode_emoji: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "permissions",
            "color",
            "hoist",
            "mentionable",
            "unicode_emoji",
        ]
        nullable_fields = [
            "name",
            "permissions",
            "color",
            "hoist",
            "mentionable",
            "unicode_emoji",
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
