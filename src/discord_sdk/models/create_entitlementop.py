"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createentitlementrequestdata import (
    CreateEntitlementRequestData,
    CreateEntitlementRequestDataTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing_extensions import Annotated, TypedDict


class CreateEntitlementRequestTypedDict(TypedDict):
    application_id: str
    create_entitlement_request_data: CreateEntitlementRequestDataTypedDict


class CreateEntitlementRequest(BaseModel):
    application_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    create_entitlement_request_data: Annotated[
        CreateEntitlementRequestData,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
