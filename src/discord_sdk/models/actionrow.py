"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .button import Button, ButtonTypedDict
from .channelselect import ChannelSelect, ChannelSelectTypedDict
from .inputtext import InputText, InputTextTypedDict
from .mentionableselect import MentionableSelect, MentionableSelectTypedDict
from .roleselect import RoleSelect, RoleSelectTypedDict
from .stringselect import StringSelect, StringSelectTypedDict
from .userselect import UserSelect, UserSelectTypedDict
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal, Union
from typing_extensions import Annotated, TypedDict


ActionRowComponentsTypedDict = Union[
    MentionableSelectTypedDict,
    RoleSelectTypedDict,
    StringSelectTypedDict,
    UserSelectTypedDict,
    ButtonTypedDict,
    ChannelSelectTypedDict,
    InputTextTypedDict,
]


ActionRowComponents = Union[
    MentionableSelect,
    RoleSelect,
    StringSelect,
    UserSelect,
    Button,
    ChannelSelect,
    InputText,
]


class ActionRowTypedDict(TypedDict):
    components: List[ActionRowComponentsTypedDict]
    type: Literal[1]


class ActionRow(BaseModel):
    components: List[ActionRowComponents]

    TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="type"),
    ] = 1
