"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .richembedauthor import RichEmbedAuthor, RichEmbedAuthorTypedDict
from .richembedfield import RichEmbedField, RichEmbedFieldTypedDict
from .richembedfooter import RichEmbedFooter, RichEmbedFooterTypedDict
from .richembedimage import RichEmbedImage, RichEmbedImageTypedDict
from .richembedprovider import RichEmbedProvider, RichEmbedProviderTypedDict
from .richembedthumbnail import RichEmbedThumbnail, RichEmbedThumbnailTypedDict
from .richembedvideo import RichEmbedVideo, RichEmbedVideoTypedDict
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


class RichEmbedTypedDict(TypedDict):
    type: NotRequired[Nullable[str]]
    url: NotRequired[Nullable[str]]
    title: NotRequired[Nullable[str]]
    color: NotRequired[Nullable[int]]
    timestamp: NotRequired[Nullable[datetime]]
    description: NotRequired[Nullable[str]]
    author: NotRequired[Nullable[RichEmbedAuthorTypedDict]]
    image: NotRequired[Nullable[RichEmbedImageTypedDict]]
    thumbnail: NotRequired[Nullable[RichEmbedThumbnailTypedDict]]
    footer: NotRequired[Nullable[RichEmbedFooterTypedDict]]
    fields: NotRequired[Nullable[List[RichEmbedFieldTypedDict]]]
    provider: NotRequired[Nullable[RichEmbedProviderTypedDict]]
    video: NotRequired[Nullable[RichEmbedVideoTypedDict]]


class RichEmbed(BaseModel):
    type: OptionalNullable[str] = UNSET

    url: OptionalNullable[str] = UNSET

    title: OptionalNullable[str] = UNSET

    color: OptionalNullable[int] = UNSET

    timestamp: OptionalNullable[datetime] = UNSET

    description: OptionalNullable[str] = UNSET

    author: OptionalNullable[RichEmbedAuthor] = UNSET

    image: OptionalNullable[RichEmbedImage] = UNSET

    thumbnail: OptionalNullable[RichEmbedThumbnail] = UNSET

    footer: OptionalNullable[RichEmbedFooter] = UNSET

    fields: OptionalNullable[List[RichEmbedField]] = UNSET

    provider: OptionalNullable[RichEmbedProvider] = UNSET

    video: OptionalNullable[RichEmbedVideo] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "type",
            "url",
            "title",
            "color",
            "timestamp",
            "description",
            "author",
            "image",
            "thumbnail",
            "footer",
            "fields",
            "provider",
            "video",
        ]
        nullable_fields = [
            "type",
            "url",
            "title",
            "color",
            "timestamp",
            "description",
            "author",
            "image",
            "thumbnail",
            "footer",
            "fields",
            "provider",
            "video",
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
