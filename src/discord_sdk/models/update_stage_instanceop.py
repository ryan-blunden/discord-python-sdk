"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import (
    FieldMetadata,
    PathParamMetadata,
    RequestMetadata,
    validate_const,
)
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import Literal, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateStageInstanceRequestBodyTypedDict(TypedDict):
    topic: NotRequired[str]
    privacy_level: Literal[1]


class UpdateStageInstanceRequestBody(BaseModel):
    topic: Optional[str] = None

    PRIVACY_LEVEL: Annotated[
        Annotated[Optional[Literal[1]], AfterValidator(validate_const(1))],
        pydantic.Field(alias="privacy_level"),
    ] = 1


class UpdateStageInstanceRequestTypedDict(TypedDict):
    channel_id: str
    request_body: UpdateStageInstanceRequestBodyTypedDict


class UpdateStageInstanceRequest(BaseModel):
    channel_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        UpdateStageInstanceRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
