"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationcommandattachmentoptionresponse import (
    ApplicationCommandAttachmentOptionResponse,
    ApplicationCommandAttachmentOptionResponseTypedDict,
)
from .applicationcommandbooleanoptionresponse import (
    ApplicationCommandBooleanOptionResponse,
    ApplicationCommandBooleanOptionResponseTypedDict,
)
from .applicationcommandchanneloptionresponse import (
    ApplicationCommandChannelOptionResponse,
    ApplicationCommandChannelOptionResponseTypedDict,
)
from .applicationcommandintegeroptionresponse import (
    ApplicationCommandIntegerOptionResponse,
    ApplicationCommandIntegerOptionResponseTypedDict,
)
from .applicationcommandmentionableoptionresponse import (
    ApplicationCommandMentionableOptionResponse,
    ApplicationCommandMentionableOptionResponseTypedDict,
)
from .applicationcommandnumberoptionresponse import (
    ApplicationCommandNumberOptionResponse,
    ApplicationCommandNumberOptionResponseTypedDict,
)
from .applicationcommandroleoptionresponse import (
    ApplicationCommandRoleOptionResponse,
    ApplicationCommandRoleOptionResponseTypedDict,
)
from .applicationcommandstringoptionresponse import (
    ApplicationCommandStringOptionResponse,
    ApplicationCommandStringOptionResponseTypedDict,
)
from .applicationcommanduseroptionresponse import (
    ApplicationCommandUserOptionResponse,
    ApplicationCommandUserOptionResponseTypedDict,
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
from typing import Dict, List, Literal, Union
from typing_extensions import Annotated, NotRequired, TypedDict


OptionsTypedDict = Union[
    ApplicationCommandAttachmentOptionResponseTypedDict,
    ApplicationCommandBooleanOptionResponseTypedDict,
    ApplicationCommandMentionableOptionResponseTypedDict,
    ApplicationCommandRoleOptionResponseTypedDict,
    ApplicationCommandUserOptionResponseTypedDict,
    ApplicationCommandChannelOptionResponseTypedDict,
    ApplicationCommandIntegerOptionResponseTypedDict,
    ApplicationCommandNumberOptionResponseTypedDict,
    ApplicationCommandStringOptionResponseTypedDict,
]


Options = Union[
    ApplicationCommandAttachmentOptionResponse,
    ApplicationCommandBooleanOptionResponse,
    ApplicationCommandMentionableOptionResponse,
    ApplicationCommandRoleOptionResponse,
    ApplicationCommandUserOptionResponse,
    ApplicationCommandChannelOptionResponse,
    ApplicationCommandIntegerOptionResponse,
    ApplicationCommandNumberOptionResponse,
    ApplicationCommandStringOptionResponse,
]


class ApplicationCommandSubcommandOptionResponseTypedDict(TypedDict):
    name: str
    description: str
    type: Literal[1]
    name_localized: NotRequired[Nullable[str]]
    name_localizations: NotRequired[Nullable[Dict[str, str]]]
    description_localized: NotRequired[Nullable[str]]
    description_localizations: NotRequired[Nullable[Dict[str, str]]]
    required: NotRequired[Nullable[bool]]
    options: NotRequired[Nullable[List[OptionsTypedDict]]]


class ApplicationCommandSubcommandOptionResponse(BaseModel):
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

    options: OptionalNullable[List[Options]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name_localized",
            "name_localizations",
            "description_localized",
            "description_localizations",
            "required",
            "options",
        ]
        nullable_fields = [
            "name_localized",
            "name_localizations",
            "description_localized",
            "description_localizations",
            "required",
            "options",
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
