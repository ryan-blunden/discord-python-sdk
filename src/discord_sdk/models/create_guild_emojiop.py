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
from typing import List
from typing_extensions import Annotated, NotRequired, TypedDict


class CreateGuildEmojiRequestBodyTypedDict(TypedDict):
    name: str
    image: str
    roles: NotRequired[Nullable[List[str]]]


class CreateGuildEmojiRequestBody(BaseModel):
    name: str

    image: str

    roles: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["roles"]
        nullable_fields = ["roles"]
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


class CreateGuildEmojiRequestTypedDict(TypedDict):
    guild_id: str
    request_body: CreateGuildEmojiRequestBodyTypedDict


class CreateGuildEmojiRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        CreateGuildEmojiRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
