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
from typing import List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class InviteGuildResponseTypedDict(TypedDict):
    id: str
    name: str
    features: List[str]
    splash: NotRequired[Nullable[str]]
    banner: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    icon: NotRequired[Nullable[str]]
    verification_level: Nullable[Literal[0]]
    vanity_url_code: NotRequired[Nullable[str]]
    nsfw_level: Nullable[Literal[0]]
    nsfw: NotRequired[Nullable[bool]]
    premium_subscription_count: NotRequired[Nullable[int]]


class InviteGuildResponse(BaseModel):
    id: str

    name: str

    features: List[str]

    splash: OptionalNullable[str] = UNSET

    banner: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET

    icon: OptionalNullable[str] = UNSET

    VERIFICATION_LEVEL: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="verification_level"),
    ] = 0

    vanity_url_code: OptionalNullable[str] = UNSET

    NSFW_LEVEL: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="nsfw_level"),
    ] = 0

    nsfw: OptionalNullable[bool] = UNSET

    premium_subscription_count: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "splash",
            "banner",
            "description",
            "icon",
            "verification_level",
            "vanity_url_code",
            "nsfw_level",
            "nsfw",
            "premium_subscription_count",
        ]
        nullable_fields = [
            "splash",
            "banner",
            "description",
            "icon",
            "verification_level",
            "vanity_url_code",
            "nsfw_level",
            "nsfw",
            "premium_subscription_count",
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