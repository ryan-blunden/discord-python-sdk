"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .usercommunicationdisabledactionmetadataresponse import (
    UserCommunicationDisabledActionMetadataResponse,
    UserCommunicationDisabledActionMetadataResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class UserCommunicationDisabledActionResponseTypedDict(TypedDict):
    metadata: UserCommunicationDisabledActionMetadataResponseTypedDict
    type: Literal[1]


class UserCommunicationDisabledActionResponse(BaseModel):
    metadata: UserCommunicationDisabledActionMetadataResponse

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1