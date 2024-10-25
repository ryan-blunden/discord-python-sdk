"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .guildchannelresponse import GuildChannelResponse, GuildChannelResponseTypedDict
from .privatechannelresponse import (
    PrivateChannelResponse,
    PrivateChannelResponseTypedDict,
)
from .privategroupchannelresponse import (
    PrivateGroupChannelResponse,
    PrivateGroupChannelResponseTypedDict,
)
from .threadresponse import ThreadResponse, ThreadResponseTypedDict
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata
from typing import Union
from typing_extensions import Annotated, TypedDict


class GetChannelRequestTypedDict(TypedDict):
    channel_id: str


class GetChannelRequest(BaseModel):
    channel_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]


GetChannelResponseBodyTypedDict = Union[
    PrivateChannelResponseTypedDict,
    PrivateGroupChannelResponseTypedDict,
    ThreadResponseTypedDict,
    GuildChannelResponseTypedDict,
]
r"""200 response for get_channel"""


GetChannelResponseBody = Union[
    PrivateChannelResponse,
    PrivateGroupChannelResponse,
    ThreadResponse,
    GuildChannelResponse,
]
r"""200 response for get_channel"""