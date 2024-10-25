"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .blockmessageaction import BlockMessageAction, BlockMessageActionTypedDict
from .flagtochannelaction import FlagToChannelAction, FlagToChannelActionTypedDict
from .mentionspamtriggermetadata import (
    MentionSpamTriggerMetadata,
    MentionSpamTriggerMetadataTypedDict,
)
from .quarantineuseraction import QuarantineUserAction, QuarantineUserActionTypedDict
from .usercommunicationdisabledaction import (
    UserCommunicationDisabledAction,
    UserCommunicationDisabledActionTypedDict,
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
from typing import List, Literal, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


MentionSpamUpsertRequestPartialActionsTypedDict = Union[
    BlockMessageActionTypedDict,
    FlagToChannelActionTypedDict,
    QuarantineUserActionTypedDict,
    UserCommunicationDisabledActionTypedDict,
]


MentionSpamUpsertRequestPartialActions = Union[
    BlockMessageAction,
    FlagToChannelAction,
    QuarantineUserAction,
    UserCommunicationDisabledAction,
]


class MentionSpamUpsertRequestPartialTypedDict(TypedDict):
    name: NotRequired[str]
    event_type: Literal[1]
    actions: NotRequired[
        Nullable[List[MentionSpamUpsertRequestPartialActionsTypedDict]]
    ]
    enabled: NotRequired[Nullable[bool]]
    exempt_roles: NotRequired[Nullable[List[str]]]
    exempt_channels: NotRequired[Nullable[List[str]]]
    trigger_type: Literal[1]
    trigger_metadata: NotRequired[Nullable[MentionSpamTriggerMetadataTypedDict]]


class MentionSpamUpsertRequestPartial(BaseModel):
    name: Optional[str] = None

    EVENT_TYPE: Annotated[
        Annotated[Optional[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="event_type"),
    ] = 1

    actions: OptionalNullable[List[MentionSpamUpsertRequestPartialActions]] = UNSET

    enabled: OptionalNullable[bool] = UNSET

    exempt_roles: OptionalNullable[List[str]] = UNSET

    exempt_channels: OptionalNullable[List[str]] = UNSET

    TRIGGER_TYPE: Annotated[
        Annotated[Optional[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="trigger_type"),
    ] = 1

    trigger_metadata: OptionalNullable[MentionSpamTriggerMetadata] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "name",
            "event_type",
            "actions",
            "enabled",
            "exempt_roles",
            "exempt_channels",
            "trigger_type",
            "trigger_metadata",
        ]
        nullable_fields = [
            "actions",
            "enabled",
            "exempt_roles",
            "exempt_channels",
            "trigger_metadata",
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
