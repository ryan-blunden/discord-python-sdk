"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .guildroletagsresponse import GuildRoleTagsResponse, GuildRoleTagsResponseTypedDict
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class GuildRoleResponseTypedDict(TypedDict):
    id: str
    name: str
    permissions: str
    position: int
    color: int
    hoist: bool
    managed: bool
    mentionable: bool
    description: NotRequired[Nullable[str]]
    icon: NotRequired[Nullable[str]]
    unicode_emoji: NotRequired[Nullable[str]]
    tags: NotRequired[Nullable[GuildRoleTagsResponseTypedDict]]


class GuildRoleResponse(BaseModel):
    id: str

    name: str

    permissions: str

    position: int

    color: int

    hoist: bool

    managed: bool

    mentionable: bool

    description: OptionalNullable[str] = UNSET

    icon: OptionalNullable[str] = UNSET

    unicode_emoji: OptionalNullable[str] = UNSET

    tags: OptionalNullable[GuildRoleTagsResponse] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["description", "icon", "unicode_emoji", "tags"]
        nullable_fields = ["description", "icon", "unicode_emoji", "tags"]
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
