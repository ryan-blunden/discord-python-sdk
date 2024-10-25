"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .soundboardpatchrequestpartial import (
    SoundboardPatchRequestPartial,
    SoundboardPatchRequestPartialTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class UpdateGuildSoundboardSoundRequestTypedDict(TypedDict):
    guild_id: str
    sound_id: str
    soundboard_patch_request_partial: SoundboardPatchRequestPartialTypedDict


class UpdateGuildSoundboardSoundRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    sound_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    soundboard_patch_request_partial: Annotated[
        SoundboardPatchRequestPartial,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]