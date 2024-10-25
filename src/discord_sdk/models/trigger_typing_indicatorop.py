"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class TriggerTypingIndicatorRequestTypedDict(TypedDict):
    channel_id: str


class TriggerTypingIndicatorRequest(BaseModel):
    channel_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]