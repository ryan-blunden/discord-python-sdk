"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .externalscheduledeventresponse import (
    ExternalScheduledEventResponse,
    ExternalScheduledEventResponseTypedDict,
)
from .stagescheduledeventresponse import (
    StageScheduledEventResponse,
    StageScheduledEventResponseTypedDict,
)
from .voicescheduledeventresponse import (
    VoiceScheduledEventResponse,
    VoiceScheduledEventResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


class ListGuildScheduledEventsRequestTypedDict(TypedDict):
    guild_id: str
    with_user_count: NotRequired[bool]


class ListGuildScheduledEventsRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    with_user_count: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None


ListGuildScheduledEventsResponseBodyTypedDict = Union[
    ExternalScheduledEventResponseTypedDict,
    StageScheduledEventResponseTypedDict,
    VoiceScheduledEventResponseTypedDict,
]


ListGuildScheduledEventsResponseBody = Union[
    ExternalScheduledEventResponse,
    StageScheduledEventResponse,
    VoiceScheduledEventResponse,
]