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
from typing_extensions import NotRequired, TypedDict


class MessageAttachmentRequestTypedDict(TypedDict):
    id: str
    filename: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    duration_secs: NotRequired[Nullable[float]]
    waveform: NotRequired[Nullable[str]]
    title: NotRequired[Nullable[str]]
    is_remix: NotRequired[Nullable[bool]]


class MessageAttachmentRequest(BaseModel):
    id: str

    filename: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET

    duration_secs: OptionalNullable[float] = UNSET

    waveform: OptionalNullable[str] = UNSET

    title: OptionalNullable[str] = UNSET

    is_remix: OptionalNullable[bool] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "filename",
            "description",
            "duration_secs",
            "waveform",
            "title",
            "is_remix",
        ]
        nullable_fields = [
            "filename",
            "description",
            "duration_secs",
            "waveform",
            "title",
            "is_remix",
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
