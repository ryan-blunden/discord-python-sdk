"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationcommandinteractionmetadataresponse import (
    ApplicationCommandInteractionMetadataResponse,
    ApplicationCommandInteractionMetadataResponseTypedDict,
)
from .basicapplicationresponse import (
    BasicApplicationResponse,
    BasicApplicationResponseTypedDict,
)
from .guildstickerresponse import GuildStickerResponse, GuildStickerResponseTypedDict
from .messageactivityresponse import (
    MessageActivityResponse,
    MessageActivityResponseTypedDict,
)
from .messageattachmentresponse import (
    MessageAttachmentResponse,
    MessageAttachmentResponseTypedDict,
)
from .messagecallresponse import MessageCallResponse, MessageCallResponseTypedDict
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
from .messagecomponentinteractionmetadataresponse import (
    MessageComponentInteractionMetadataResponse,
    MessageComponentInteractionMetadataResponseTypedDict,
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
from .messageinteractionresponse import (
    MessageInteractionResponse,
    MessageInteractionResponseTypedDict,
)
from .messagementionchannelresponse import (
    MessageMentionChannelResponse,
    MessageMentionChannelResponseTypedDict,
)
from .messagereferenceresponse import (
    MessageReferenceResponse,
    MessageReferenceResponseTypedDict,
)
from .messagerolesubscriptiondataresponse import (
    MessageRoleSubscriptionDataResponse,
    MessageRoleSubscriptionDataResponseTypedDict,
)
from .messagesnapshotresponse import (
    MessageSnapshotResponse,
    MessageSnapshotResponseTypedDict,
)
from .messagestickeritemresponse import (
    MessageStickerItemResponse,
    MessageStickerItemResponseTypedDict,
)
from .modalsubmitinteractionmetadataresponse import (
    ModalSubmitInteractionMetadataResponse,
    ModalSubmitInteractionMetadataResponseTypedDict,
)
from .pollresponse import PollResponse, PollResponseTypedDict
from .purchasenotificationresponse import (
    PurchaseNotificationResponse,
    PurchaseNotificationResponseTypedDict,
)
from .resolvedobjectsresponse import (
    ResolvedObjectsResponse,
    ResolvedObjectsResponseTypedDict,
)
from .standardstickerresponse import (
    StandardStickerResponse,
    StandardStickerResponseTypedDict,
)
from .threadresponse import ThreadResponse, ThreadResponseTypedDict
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


BasicMessageResponseComponentsTypedDict = Union[
    MessageComponentActionRowResponseTypedDict,
    MessageComponentMentionableSelectResponseTypedDict,
    MessageComponentRoleSelectResponseTypedDict,
    MessageComponentStringSelectResponseTypedDict,
    MessageComponentUserSelectResponseTypedDict,
    MessageComponentButtonResponseTypedDict,
    MessageComponentChannelSelectResponseTypedDict,
    MessageComponentInputTextResponseTypedDict,
]


BasicMessageResponseComponents = Union[
    MessageComponentActionRowResponse,
    MessageComponentMentionableSelectResponse,
    MessageComponentRoleSelectResponse,
    MessageComponentStringSelectResponse,
    MessageComponentUserSelectResponse,
    MessageComponentButtonResponse,
    MessageComponentChannelSelectResponse,
    MessageComponentInputTextResponse,
]


BasicMessageResponseStickersTypedDict = Union[
    StandardStickerResponseTypedDict, GuildStickerResponseTypedDict
]


BasicMessageResponseStickers = Union[StandardStickerResponse, GuildStickerResponse]


BasicMessageResponseNonceTypedDict = Union[int, str]


BasicMessageResponseNonce = Union[int, str]


BasicMessageResponseInteractionMetadataTypedDict = Union[
    MessageComponentInteractionMetadataResponseTypedDict,
    ModalSubmitInteractionMetadataResponseTypedDict,
    ApplicationCommandInteractionMetadataResponseTypedDict,
]


BasicMessageResponseInteractionMetadata = Union[
    MessageComponentInteractionMetadataResponse,
    ModalSubmitInteractionMetadataResponse,
    ApplicationCommandInteractionMetadataResponse,
]


class BasicMessageResponseTypedDict(TypedDict):
    content: str
    mentions: List[UserResponseTypedDict]
    mention_roles: List[str]
    attachments: List[MessageAttachmentResponseTypedDict]
    embeds: List[MessageEmbedResponseTypedDict]
    timestamp: datetime
    flags: int
    components: List[BasicMessageResponseComponentsTypedDict]
    id: str
    channel_id: str
    author: UserResponseTypedDict
    pinned: bool
    mention_everyone: bool
    tts: bool
    type: Literal[0]
    edited_timestamp: NotRequired[Nullable[datetime]]
    resolved: NotRequired[Nullable[ResolvedObjectsResponseTypedDict]]
    stickers: NotRequired[Nullable[List[BasicMessageResponseStickersTypedDict]]]
    sticker_items: NotRequired[Nullable[List[MessageStickerItemResponseTypedDict]]]
    call: NotRequired[Nullable[MessageCallResponseTypedDict]]
    activity: NotRequired[Nullable[MessageActivityResponseTypedDict]]
    application: NotRequired[Nullable[BasicApplicationResponseTypedDict]]
    application_id: NotRequired[Nullable[str]]
    interaction: NotRequired[Nullable[MessageInteractionResponseTypedDict]]
    nonce: NotRequired[Nullable[BasicMessageResponseNonceTypedDict]]
    webhook_id: NotRequired[Nullable[str]]
    message_reference: NotRequired[Nullable[MessageReferenceResponseTypedDict]]
    thread: NotRequired[Nullable[ThreadResponseTypedDict]]
    mention_channels: NotRequired[
        Nullable[List[MessageMentionChannelResponseTypedDict]]
    ]
    role_subscription_data: NotRequired[
        Nullable[MessageRoleSubscriptionDataResponseTypedDict]
    ]
    purchase_notification: NotRequired[Nullable[PurchaseNotificationResponseTypedDict]]
    position: NotRequired[Nullable[int]]
    poll: NotRequired[Nullable[PollResponseTypedDict]]
    interaction_metadata: NotRequired[
        Nullable[BasicMessageResponseInteractionMetadataTypedDict]
    ]
    message_snapshots: NotRequired[Nullable[List[MessageSnapshotResponseTypedDict]]]


class BasicMessageResponse(BaseModel):
    content: str

    mentions: List[UserResponse]

    mention_roles: List[str]

    attachments: List[MessageAttachmentResponse]

    embeds: List[MessageEmbedResponse]

    timestamp: datetime

    flags: int

    components: List[BasicMessageResponseComponents]

    id: str

    channel_id: str

    author: UserResponse

    pinned: bool

    mention_everyone: bool

    tts: bool

    TYPE: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="type"),
    ] = 0

    edited_timestamp: OptionalNullable[datetime] = UNSET

    resolved: OptionalNullable[ResolvedObjectsResponse] = UNSET

    stickers: OptionalNullable[List[BasicMessageResponseStickers]] = UNSET

    sticker_items: OptionalNullable[List[MessageStickerItemResponse]] = UNSET

    call: OptionalNullable[MessageCallResponse] = UNSET

    activity: OptionalNullable[MessageActivityResponse] = UNSET

    application: OptionalNullable[BasicApplicationResponse] = UNSET

    application_id: OptionalNullable[str] = UNSET

    interaction: OptionalNullable[MessageInteractionResponse] = UNSET

    nonce: OptionalNullable[BasicMessageResponseNonce] = UNSET

    webhook_id: OptionalNullable[str] = UNSET

    message_reference: OptionalNullable[MessageReferenceResponse] = UNSET

    thread: OptionalNullable[ThreadResponse] = UNSET

    mention_channels: OptionalNullable[List[MessageMentionChannelResponse]] = UNSET

    role_subscription_data: OptionalNullable[MessageRoleSubscriptionDataResponse] = (
        UNSET
    )

    purchase_notification: OptionalNullable[PurchaseNotificationResponse] = UNSET

    position: OptionalNullable[int] = UNSET

    poll: OptionalNullable[PollResponse] = UNSET

    interaction_metadata: OptionalNullable[BasicMessageResponseInteractionMetadata] = (
        UNSET
    )

    message_snapshots: OptionalNullable[List[MessageSnapshotResponse]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "edited_timestamp",
            "resolved",
            "stickers",
            "sticker_items",
            "call",
            "activity",
            "application",
            "application_id",
            "interaction",
            "nonce",
            "webhook_id",
            "message_reference",
            "thread",
            "mention_channels",
            "role_subscription_data",
            "purchase_notification",
            "position",
            "poll",
            "interaction_metadata",
            "message_snapshots",
        ]
        nullable_fields = [
            "edited_timestamp",
            "resolved",
            "stickers",
            "sticker_items",
            "call",
            "activity",
            "application",
            "application_id",
            "interaction",
            "nonce",
            "webhook_id",
            "message_reference",
            "thread",
            "mention_channels",
            "role_subscription_data",
            "purchase_notification",
            "position",
            "poll",
            "interaction_metadata",
            "message_snapshots",
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
