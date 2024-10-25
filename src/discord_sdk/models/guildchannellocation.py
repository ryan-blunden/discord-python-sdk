"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class GuildChannelLocationTypedDict(TypedDict):
    id: str
    channel_id: str
    guild_id: str
    kind: Literal["gc"]


class GuildChannelLocation(BaseModel):
    id: str

    channel_id: str

    guild_id: str

    KIND: Annotated[
        Annotated[Literal["gc"], AfterValidator(validate_const("gc"))],
        pydantic.Field(alias="kind"),
    ] = "gc"
