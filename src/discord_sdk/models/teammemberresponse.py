"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .userresponse import UserResponse, UserResponseTypedDict
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal
from typing_extensions import Annotated, TypedDict


class TeamMemberResponseTypedDict(TypedDict):
    user: UserResponseTypedDict
    team_id: str
    membership_state: Literal[1]


class TeamMemberResponse(BaseModel):
    user: UserResponse

    team_id: str

    MEMBERSHIP_STATE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="membership_state"),
    ] = 1