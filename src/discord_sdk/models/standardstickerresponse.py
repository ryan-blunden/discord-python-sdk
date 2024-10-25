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
from typing import Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class StandardStickerResponseTypedDict(TypedDict):
    id: str
    name: str
    tags: str
    pack_id: str
    sort_value: int
    type: Literal[1]
    format_type: Nullable[Literal[1]]
    description: NotRequired[Nullable[str]]


class StandardStickerResponse(BaseModel):
    id: str

    name: str

    tags: str

    pack_id: str

    sort_value: int

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1

    FORMAT_TYPE: Annotated[
        Annotated[OptionalNullable[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="format_type"),
    ] = 1

    description: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["format_type", "description"]
        nullable_fields = ["format_type", "description"]
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
