"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class MessageStickerItemResponseTypedDict(TypedDict):
    id: str
    name: str
    format_type: Literal[1]


class MessageStickerItemResponse(BaseModel):
    id: str

    name: str

    FORMAT_TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="format_type"),
    ] = 1
