"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationresponse import ApplicationResponse, ApplicationResponseTypedDict
from .userresponse import UserResponse, UserResponseTypedDict
from datetime import datetime
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List
from typing_extensions import NotRequired, TypedDict


class AttachmentResponseTypedDict(TypedDict):
    id: str
    filename: str
    size: int
    url: str
    proxy_url: str
    width: NotRequired[Nullable[int]]
    height: NotRequired[Nullable[int]]
    duration_secs: NotRequired[Nullable[float]]
    waveform: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    content_type: NotRequired[Nullable[str]]
    ephemeral: NotRequired[Nullable[bool]]
    title: NotRequired[Nullable[str]]
    application: NotRequired[Nullable[ApplicationResponseTypedDict]]
    clip_created_at: NotRequired[Nullable[datetime]]
    clip_participants: NotRequired[Nullable[List[UserResponseTypedDict]]]


class AttachmentResponse(BaseModel):
    id: str

    filename: str

    size: int

    url: str

    proxy_url: str

    width: OptionalNullable[int] = UNSET

    height: OptionalNullable[int] = UNSET

    duration_secs: OptionalNullable[float] = UNSET

    waveform: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET

    content_type: OptionalNullable[str] = UNSET

    ephemeral: OptionalNullable[bool] = UNSET

    title: OptionalNullable[str] = UNSET

    application: OptionalNullable[ApplicationResponse] = UNSET

    clip_created_at: OptionalNullable[datetime] = UNSET

    clip_participants: OptionalNullable[List[UserResponse]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "width",
            "height",
            "duration_secs",
            "waveform",
            "description",
            "content_type",
            "ephemeral",
            "title",
            "application",
            "clip_created_at",
            "clip_participants",
        ]
        nullable_fields = [
            "width",
            "height",
            "duration_secs",
            "waveform",
            "description",
            "content_type",
            "ephemeral",
            "title",
            "application",
            "clip_created_at",
            "clip_participants",
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
