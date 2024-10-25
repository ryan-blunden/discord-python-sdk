"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .oauth2key import OAuth2Key, OAuth2KeyTypedDict
from discord_sdk.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OAuth2GetKeysTypedDict(TypedDict):
    keys: List[OAuth2KeyTypedDict]


class OAuth2GetKeys(BaseModel):
    keys: List[OAuth2Key]