"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountresponse import AccountResponse, AccountResponseTypedDict
from .userresponse import UserResponse, UserResponseTypedDict
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


class ExternalConnectionIntegrationResponseTypedDict(TypedDict):
    id: str
    user: UserResponseTypedDict
    type: Literal["discord"]
    name: NotRequired[Nullable[str]]
    account: NotRequired[Nullable[AccountResponseTypedDict]]
    enabled: NotRequired[Nullable[bool]]
    revoked: NotRequired[Nullable[bool]]
    expire_behavior: Nullable[Literal[0]]
    expire_grace_period: Nullable[Literal[1]]
    subscriber_count: NotRequired[Nullable[int]]
    synced_at: NotRequired[Nullable[datetime]]
    role_id: NotRequired[Nullable[str]]
    syncing: NotRequired[Nullable[bool]]
    enable_emoticons: NotRequired[Nullable[bool]]


class ExternalConnectionIntegrationResponse(BaseModel):
    id: str

    user: UserResponse

    TYPE: Annotated[
        Annotated[Literal["discord"], AfterValidator(validate_const("discord"))],
        pydantic.Field(alias="type"),
    ] = "discord"

    name: OptionalNullable[str] = UNSET

    account: OptionalNullable[AccountResponse] = UNSET

    enabled: OptionalNullable[bool] = UNSET

    revoked: OptionalNullable[bool] = UNSET

    EXPIRE_BEHAVIOR: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="expire_behavior"),
    ] = 0

    EXPIRE_GRACE_PERIOD: Annotated[
        Annotated[OptionalNullable[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="expire_grace_period"),
    ] = 1

    subscriber_count: OptionalNullable[int] = UNSET

    synced_at: OptionalNullable[datetime] = UNSET

    role_id: OptionalNullable[str] = UNSET

    syncing: OptionalNullable[bool] = UNSET

    enable_emoticons: OptionalNullable[bool] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "account",
            "enabled",
            "revoked",
            "expire_behavior",
            "expire_grace_period",
            "subscriber_count",
            "synced_at",
            "role_id",
            "syncing",
            "enable_emoticons",
        ]
        nullable_fields = [
            "name",
            "account",
            "enabled",
            "revoked",
            "expire_behavior",
            "expire_grace_period",
            "subscriber_count",
            "synced_at",
            "role_id",
            "syncing",
            "enable_emoticons",
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
