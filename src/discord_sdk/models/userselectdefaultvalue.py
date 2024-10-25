"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class UserSelectDefaultValueTypedDict(TypedDict):
    id: str
    type: Literal["user"]


class UserSelectDefaultValue(BaseModel):
    id: str

    TYPE: Annotated[
        Annotated[Literal["user"], AfterValidator(validate_const("user"))],
        pydantic.Field(alias="type"),
    ] = "user"