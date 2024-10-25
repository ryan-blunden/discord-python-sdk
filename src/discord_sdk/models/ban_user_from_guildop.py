"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from pydantic import model_serializer
from typing_extensions import Annotated, NotRequired, TypedDict


class BanUserFromGuildRequestBodyTypedDict(TypedDict):
    delete_message_seconds: NotRequired[Nullable[int]]
    delete_message_days: NotRequired[Nullable[int]]


class BanUserFromGuildRequestBody(BaseModel):
    delete_message_seconds: OptionalNullable[int] = UNSET

    delete_message_days: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["delete_message_seconds", "delete_message_days"]
        nullable_fields = ["delete_message_seconds", "delete_message_days"]
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


class BanUserFromGuildRequestTypedDict(TypedDict):
    guild_id: str
    user_id: str
    request_body: BanUserFromGuildRequestBodyTypedDict


class BanUserFromGuildRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        BanUserFromGuildRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]