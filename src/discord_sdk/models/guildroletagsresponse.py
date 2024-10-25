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
from typing import Any
from typing_extensions import NotRequired, TypedDict


class GuildRoleTagsResponseTypedDict(TypedDict):
    premium_subscriber: NotRequired[Nullable[Any]]
    bot_id: NotRequired[Nullable[str]]
    integration_id: NotRequired[Nullable[str]]
    subscription_listing_id: NotRequired[Nullable[str]]
    available_for_purchase: NotRequired[Nullable[Any]]
    guild_connections: NotRequired[Nullable[Any]]


class GuildRoleTagsResponse(BaseModel):
    premium_subscriber: OptionalNullable[Any] = UNSET

    bot_id: OptionalNullable[str] = UNSET

    integration_id: OptionalNullable[str] = UNSET

    subscription_listing_id: OptionalNullable[str] = UNSET

    available_for_purchase: OptionalNullable[Any] = UNSET

    guild_connections: OptionalNullable[Any] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "premium_subscriber",
            "bot_id",
            "integration_id",
            "subscription_listing_id",
            "available_for_purchase",
            "guild_connections",
        ]
        nullable_fields = [
            "premium_subscriber",
            "bot_id",
            "integration_id",
            "subscription_listing_id",
            "available_for_purchase",
            "guild_connections",
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
