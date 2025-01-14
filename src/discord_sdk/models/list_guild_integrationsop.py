"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .discordintegrationresponse import (
    DiscordIntegrationResponse,
    DiscordIntegrationResponseTypedDict,
)
from .externalconnectionintegrationresponse import (
    ExternalConnectionIntegrationResponse,
    ExternalConnectionIntegrationResponseTypedDict,
)
from .guildsubscriptionintegrationresponse import (
    GuildSubscriptionIntegrationResponse,
    GuildSubscriptionIntegrationResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypedDict


class ListGuildIntegrationsRequestTypedDict(TypedDict):
    guild_id: str


class ListGuildIntegrationsRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


ListGuildIntegrationsResponseBodyTypedDict = Union[
    GuildSubscriptionIntegrationResponseTypedDict,
    DiscordIntegrationResponseTypedDict,
    ExternalConnectionIntegrationResponseTypedDict,
]


ListGuildIntegrationsResponseBody = Union[
    GuildSubscriptionIntegrationResponse,
    DiscordIntegrationResponse,
    ExternalConnectionIntegrationResponse,
]
