"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .webhookslackembedfield import (
    WebhookSlackEmbedField,
    WebhookSlackEmbedFieldTypedDict,
)
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


class WebhookSlackEmbedTypedDict(TypedDict):
    title: NotRequired[Nullable[str]]
    title_link: NotRequired[Nullable[str]]
    text: NotRequired[Nullable[str]]
    color: NotRequired[Nullable[str]]
    ts: NotRequired[Nullable[int]]
    pretext: NotRequired[Nullable[str]]
    footer: NotRequired[Nullable[str]]
    footer_icon: NotRequired[Nullable[str]]
    author_name: NotRequired[Nullable[str]]
    author_link: NotRequired[Nullable[str]]
    author_icon: NotRequired[Nullable[str]]
    image_url: NotRequired[Nullable[str]]
    thumb_url: NotRequired[Nullable[str]]
    fields: NotRequired[Nullable[List[WebhookSlackEmbedFieldTypedDict]]]


class WebhookSlackEmbed(BaseModel):
    title: OptionalNullable[str] = UNSET

    title_link: OptionalNullable[str] = UNSET

    text: OptionalNullable[str] = UNSET

    color: OptionalNullable[str] = UNSET

    ts: OptionalNullable[int] = UNSET

    pretext: OptionalNullable[str] = UNSET

    footer: OptionalNullable[str] = UNSET

    footer_icon: OptionalNullable[str] = UNSET

    author_name: OptionalNullable[str] = UNSET

    author_link: OptionalNullable[str] = UNSET

    author_icon: OptionalNullable[str] = UNSET

    image_url: OptionalNullable[str] = UNSET

    thumb_url: OptionalNullable[str] = UNSET

    fields: OptionalNullable[List[WebhookSlackEmbedField]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "title",
            "title_link",
            "text",
            "color",
            "ts",
            "pretext",
            "footer",
            "footer_icon",
            "author_name",
            "author_link",
            "author_icon",
            "image_url",
            "thumb_url",
            "fields",
        ]
        nullable_fields = [
            "title",
            "title_link",
            "text",
            "color",
            "ts",
            "pretext",
            "footer",
            "footer_icon",
            "author_name",
            "author_link",
            "author_icon",
            "image_url",
            "thumb_url",
            "fields",
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