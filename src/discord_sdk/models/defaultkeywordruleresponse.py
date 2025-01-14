"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .blockmessageactionresponse import (
    BlockMessageActionResponse,
    BlockMessageActionResponseTypedDict,
)
from .defaultkeywordlisttriggermetadataresponse import (
    DefaultKeywordListTriggerMetadataResponse,
    DefaultKeywordListTriggerMetadataResponseTypedDict,
)
from .flagtochannelactionresponse import (
    FlagToChannelActionResponse,
    FlagToChannelActionResponseTypedDict,
)
from .quarantineuseractionresponse import (
    QuarantineUserActionResponse,
    QuarantineUserActionResponseTypedDict,
)
from .usercommunicationdisabledactionresponse import (
    UserCommunicationDisabledActionResponse,
    UserCommunicationDisabledActionResponseTypedDict,
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
from typing import List, Literal, Union
from typing_extensions import Annotated, NotRequired, TypedDict


ActionsTypedDict = Union[
    BlockMessageActionResponseTypedDict,
    FlagToChannelActionResponseTypedDict,
    QuarantineUserActionResponseTypedDict,
    UserCommunicationDisabledActionResponseTypedDict,
]


Actions = Union[
    BlockMessageActionResponse,
    FlagToChannelActionResponse,
    QuarantineUserActionResponse,
    UserCommunicationDisabledActionResponse,
]


class DefaultKeywordRuleResponseTypedDict(TypedDict):
    id: str
    guild_id: str
    creator_id: str
    name: str
    actions: List[ActionsTypedDict]
    trigger_metadata: DefaultKeywordListTriggerMetadataResponseTypedDict
    event_type: Literal[1]
    trigger_type: Literal[1]
    enabled: NotRequired[Nullable[bool]]
    exempt_roles: NotRequired[Nullable[List[str]]]
    exempt_channels: NotRequired[Nullable[List[str]]]


class DefaultKeywordRuleResponse(BaseModel):
    id: str

    guild_id: str

    creator_id: str

    name: str

    actions: List[Actions]

    trigger_metadata: DefaultKeywordListTriggerMetadataResponse

    EVENT_TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="event_type"),
    ] = 1

    TRIGGER_TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="trigger_type"),
    ] = 1

    enabled: OptionalNullable[bool] = UNSET

    exempt_roles: OptionalNullable[List[str]] = UNSET

    exempt_channels: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["enabled", "exempt_roles", "exempt_channels"]
        nullable_fields = ["enabled", "exempt_roles", "exempt_channels"]
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
