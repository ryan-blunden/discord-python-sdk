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
from typing import List
from typing_extensions import NotRequired, TypedDict


class MyGuildResponseTypedDict(TypedDict):
    id: str
    name: str
    owner: bool
    permissions: str
    features: List[str]
    icon: NotRequired[Nullable[str]]
    banner: NotRequired[Nullable[str]]
    approximate_member_count: NotRequired[Nullable[int]]
    approximate_presence_count: NotRequired[Nullable[int]]


class MyGuildResponse(BaseModel):
    id: str

    name: str

    owner: bool

    permissions: str

    features: List[str]

    icon: OptionalNullable[str] = UNSET

    banner: OptionalNullable[str] = UNSET

    approximate_member_count: OptionalNullable[int] = UNSET

    approximate_presence_count: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "icon",
            "banner",
            "approximate_member_count",
            "approximate_presence_count",
        ]
        nullable_fields = [
            "icon",
            "banner",
            "approximate_member_count",
            "approximate_presence_count",
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