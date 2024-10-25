"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .settingsemojiresponse import SettingsEmojiResponse, SettingsEmojiResponseTypedDict
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


class NewMemberActionResponseTypedDict(TypedDict):
    channel_id: str
    title: str
    description: str
    action_type: Literal[0]
    emoji: NotRequired[Nullable[SettingsEmojiResponseTypedDict]]
    icon: NotRequired[Nullable[str]]


class NewMemberActionResponse(BaseModel):
    channel_id: str

    title: str

    description: str

    ACTION_TYPE: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="action_type"),
    ] = 0

    emoji: OptionalNullable[SettingsEmojiResponse] = UNSET

    icon: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["emoji", "icon"]
        nullable_fields = ["emoji", "icon"]
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
