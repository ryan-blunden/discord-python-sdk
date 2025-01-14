"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .guildstickerresponse import GuildStickerResponse, GuildStickerResponseTypedDict
from .messageattachmentresponse import (
    MessageAttachmentResponse,
    MessageAttachmentResponseTypedDict,
)
from .messagecomponentactionrowresponse import (
    MessageComponentActionRowResponse,
    MessageComponentActionRowResponseTypedDict,
)
from .messagecomponentbuttonresponse import (
    MessageComponentButtonResponse,
    MessageComponentButtonResponseTypedDict,
)
from .messagecomponentchannelselectresponse import (
    MessageComponentChannelSelectResponse,
    MessageComponentChannelSelectResponseTypedDict,
)
from .messagecomponentinputtextresponse import (
    MessageComponentInputTextResponse,
    MessageComponentInputTextResponseTypedDict,
)
from .messagecomponentmentionableselectresponse import (
    MessageComponentMentionableSelectResponse,
    MessageComponentMentionableSelectResponseTypedDict,
)
from .messagecomponentroleselectresponse import (
    MessageComponentRoleSelectResponse,
    MessageComponentRoleSelectResponseTypedDict,
)
from .messagecomponentstringselectresponse import (
    MessageComponentStringSelectResponse,
    MessageComponentStringSelectResponseTypedDict,
)
from .messagecomponentuserselectresponse import (
    MessageComponentUserSelectResponse,
    MessageComponentUserSelectResponseTypedDict,
)
from .messageembedresponse import MessageEmbedResponse, MessageEmbedResponseTypedDict
from .messagestickeritemresponse import (
    MessageStickerItemResponse,
    MessageStickerItemResponseTypedDict,
)
from .resolvedobjectsresponse import (
    ResolvedObjectsResponse,
    ResolvedObjectsResponseTypedDict,
)
from .standardstickerresponse import (
    StandardStickerResponse,
    StandardStickerResponseTypedDict,
)
from .userresponse import UserResponse, UserResponseTypedDict
from datetime import datetime
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
from typing import List, Literal, Union
from typing_extensions import Annotated, NotRequired, TypedDict


MinimalContentMessageResponseComponentsTypedDict = Union[
    MessageComponentActionRowResponseTypedDict,
    MessageComponentMentionableSelectResponseTypedDict,
    MessageComponentRoleSelectResponseTypedDict,
    MessageComponentStringSelectResponseTypedDict,
    MessageComponentUserSelectResponseTypedDict,
    MessageComponentButtonResponseTypedDict,
    MessageComponentChannelSelectResponseTypedDict,
    MessageComponentInputTextResponseTypedDict,
]


MinimalContentMessageResponseComponents = Union[
    MessageComponentActionRowResponse,
    MessageComponentMentionableSelectResponse,
    MessageComponentRoleSelectResponse,
    MessageComponentStringSelectResponse,
    MessageComponentUserSelectResponse,
    MessageComponentButtonResponse,
    MessageComponentChannelSelectResponse,
    MessageComponentInputTextResponse,
]


MinimalContentMessageResponseStickersTypedDict = Union[
    StandardStickerResponseTypedDict, GuildStickerResponseTypedDict
]


MinimalContentMessageResponseStickers = Union[
    StandardStickerResponse, GuildStickerResponse
]


class MinimalContentMessageResponseTypedDict(TypedDict):
    content: str
    mentions: List[UserResponseTypedDict]
    mention_roles: List[str]
    attachments: List[MessageAttachmentResponseTypedDict]
    embeds: List[MessageEmbedResponseTypedDict]
    timestamp: datetime
    flags: int
    components: List[MinimalContentMessageResponseComponentsTypedDict]
    type: Literal[0]
    edited_timestamp: NotRequired[Nullable[datetime]]
    resolved: NotRequired[Nullable[ResolvedObjectsResponseTypedDict]]
    stickers: NotRequired[
        Nullable[List[MinimalContentMessageResponseStickersTypedDict]]
    ]
    sticker_items: NotRequired[Nullable[List[MessageStickerItemResponseTypedDict]]]


class MinimalContentMessageResponse(BaseModel):
    content: str

    mentions: List[UserResponse]

    mention_roles: List[str]

    attachments: List[MessageAttachmentResponse]

    embeds: List[MessageEmbedResponse]

    timestamp: datetime

    flags: int

    components: List[MinimalContentMessageResponseComponents]

    TYPE: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="type"),
    ] = 0

    edited_timestamp: OptionalNullable[datetime] = UNSET

    resolved: OptionalNullable[ResolvedObjectsResponse] = UNSET

    stickers: OptionalNullable[List[MinimalContentMessageResponseStickers]] = UNSET

    sticker_items: OptionalNullable[List[MessageStickerItemResponse]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["edited_timestamp", "resolved", "stickers", "sticker_items"]
        nullable_fields = ["edited_timestamp", "resolved", "stickers", "sticker_items"]
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
