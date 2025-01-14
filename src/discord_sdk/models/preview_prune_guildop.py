"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypedDict


QueryParamIncludeRolesTypedDict = Union[str, List[str]]


QueryParamIncludeRoles = Union[str, List[str]]


class PreviewPruneGuildRequestTypedDict(TypedDict):
    guild_id: str
    days: NotRequired[int]
    include_roles: NotRequired[QueryParamIncludeRolesTypedDict]


class PreviewPruneGuildRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    days: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    include_roles: Annotated[
        Optional[QueryParamIncludeRoles],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
