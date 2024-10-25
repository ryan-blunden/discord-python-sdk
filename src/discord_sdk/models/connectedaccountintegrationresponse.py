"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accountresponse import AccountResponse, AccountResponseTypedDict
from .connectedaccountguildresponse import (
    ConnectedAccountGuildResponse,
    ConnectedAccountGuildResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class ConnectedAccountIntegrationResponseTypedDict(TypedDict):
    id: str
    account: AccountResponseTypedDict
    guild: ConnectedAccountGuildResponseTypedDict
    type: Literal["discord"]


class ConnectedAccountIntegrationResponse(BaseModel):
    id: str

    account: AccountResponse

    guild: ConnectedAccountGuildResponse

    TYPE: Annotated[
        Annotated[Literal["discord"], AfterValidator(validate_const("discord"))],
        pydantic.Field(alias="type"),
    ] = "discord"