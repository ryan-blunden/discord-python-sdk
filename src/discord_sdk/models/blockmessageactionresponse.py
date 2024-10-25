"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .blockmessageactionmetadataresponse import (
    BlockMessageActionMetadataResponse,
    BlockMessageActionMetadataResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class BlockMessageActionResponseTypedDict(TypedDict):
    metadata: BlockMessageActionMetadataResponseTypedDict
    type: Literal[1]


class BlockMessageActionResponse(BaseModel):
    metadata: BlockMessageActionMetadataResponse

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1
