"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .messageembedauthorresponse import (
    MessageEmbedAuthorResponse,
    MessageEmbedAuthorResponseTypedDict,
)
from .messageembedfieldresponse import (
    MessageEmbedFieldResponse,
    MessageEmbedFieldResponseTypedDict,
)
from .messageembedfooterresponse import (
    MessageEmbedFooterResponse,
    MessageEmbedFooterResponseTypedDict,
)
from .messageembedimageresponse import (
    MessageEmbedImageResponse,
    MessageEmbedImageResponseTypedDict,
)
from .messageembedproviderresponse import (
    MessageEmbedProviderResponse,
    MessageEmbedProviderResponseTypedDict,
)
from .messageembedvideoresponse import (
    MessageEmbedVideoResponse,
    MessageEmbedVideoResponseTypedDict,
)
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


class MessageEmbedResponseTypedDict(TypedDict):
    type: str
    url: NotRequired[Nullable[str]]
    title: NotRequired[Nullable[str]]
    description: NotRequired[Nullable[str]]
    color: NotRequired[Nullable[int]]
    timestamp: NotRequired[Nullable[datetime]]
    fields: NotRequired[Nullable[List[MessageEmbedFieldResponseTypedDict]]]
    author: NotRequired[Nullable[MessageEmbedAuthorResponseTypedDict]]
    provider: NotRequired[Nullable[MessageEmbedProviderResponseTypedDict]]
    image: NotRequired[Nullable[MessageEmbedImageResponseTypedDict]]
    thumbnail: NotRequired[Nullable[MessageEmbedImageResponseTypedDict]]
    video: NotRequired[Nullable[MessageEmbedVideoResponseTypedDict]]
    footer: NotRequired[Nullable[MessageEmbedFooterResponseTypedDict]]


class MessageEmbedResponse(BaseModel):
    type: str

    url: OptionalNullable[str] = UNSET

    title: OptionalNullable[str] = UNSET

    description: OptionalNullable[str] = UNSET

    color: OptionalNullable[int] = UNSET

    timestamp: OptionalNullable[datetime] = UNSET

    fields: OptionalNullable[List[MessageEmbedFieldResponse]] = UNSET

    author: OptionalNullable[MessageEmbedAuthorResponse] = UNSET

    provider: OptionalNullable[MessageEmbedProviderResponse] = UNSET

    image: OptionalNullable[MessageEmbedImageResponse] = UNSET

    thumbnail: OptionalNullable[MessageEmbedImageResponse] = UNSET

    video: OptionalNullable[MessageEmbedVideoResponse] = UNSET

    footer: OptionalNullable[MessageEmbedFooterResponse] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "url",
            "title",
            "description",
            "color",
            "timestamp",
            "fields",
            "author",
            "provider",
            "image",
            "thumbnail",
            "video",
            "footer",
        ]
        nullable_fields = [
            "url",
            "title",
            "description",
            "color",
            "timestamp",
            "fields",
            "author",
            "provider",
            "image",
            "thumbnail",
            "video",
            "footer",
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