"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationcommandoptionintegerchoiceresponse import (
    ApplicationCommandOptionIntegerChoiceResponse,
    ApplicationCommandOptionIntegerChoiceResponseTypedDict,
)
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
from typing import Dict, List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class ApplicationCommandIntegerOptionResponseTypedDict(TypedDict):
    name: str
    description: str
    type: Literal[1]
    name_localized: NotRequired[Nullable[str]]
    name_localizations: NotRequired[Nullable[Dict[str, str]]]
    description_localized: NotRequired[Nullable[str]]
    description_localizations: NotRequired[Nullable[Dict[str, str]]]
    required: NotRequired[Nullable[bool]]
    autocomplete: NotRequired[Nullable[bool]]
    choices: NotRequired[
        Nullable[List[ApplicationCommandOptionIntegerChoiceResponseTypedDict]]
    ]
    min_value: NotRequired[Nullable[int]]
    max_value: NotRequired[Nullable[int]]


class ApplicationCommandIntegerOptionResponse(BaseModel):
    name: str

    description: str

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1

    name_localized: OptionalNullable[str] = UNSET

    name_localizations: OptionalNullable[Dict[str, str]] = UNSET

    description_localized: OptionalNullable[str] = UNSET

    description_localizations: OptionalNullable[Dict[str, str]] = UNSET

    required: OptionalNullable[bool] = UNSET

    autocomplete: OptionalNullable[bool] = UNSET

    choices: OptionalNullable[List[ApplicationCommandOptionIntegerChoiceResponse]] = (
        UNSET
    )

    min_value: OptionalNullable[int] = UNSET

    max_value: OptionalNullable[int] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name_localized",
            "name_localizations",
            "description_localized",
            "description_localizations",
            "required",
            "autocomplete",
            "choices",
            "min_value",
            "max_value",
        ]
        nullable_fields = [
            "name_localized",
            "name_localizations",
            "description_localized",
            "description_localizations",
            "required",
            "autocomplete",
            "choices",
            "min_value",
            "max_value",
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
