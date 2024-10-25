"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .applicationintegrationtypeconfigurationresponse import (
    ApplicationIntegrationTypeConfigurationResponse,
    ApplicationIntegrationTypeConfigurationResponseTypedDict,
)
from .applicationoauth2installparamsresponse import (
    ApplicationOAuth2InstallParamsResponse,
    ApplicationOAuth2InstallParamsResponseTypedDict,
)
from .userresponse import UserResponse, UserResponseTypedDict
from discord_sdk.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from discord_sdk.utils import validate_const
import pydantic
from pydantic import model_serializer
from pydantic.functional_validators import AfterValidator
from typing import Dict, List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class ApplicationResponseTypedDict(TypedDict):
    id: str
    name: str
    description: str
    verify_key: str
    flags: int
    icon: NotRequired[Nullable[str]]
    type: Nullable[Literal[4]]
    cover_image: NotRequired[Nullable[str]]
    primary_sku_id: NotRequired[Nullable[str]]
    bot: NotRequired[Nullable[UserResponseTypedDict]]
    slug: NotRequired[Nullable[str]]
    guild_id: NotRequired[Nullable[str]]
    rpc_origins: NotRequired[Nullable[List[str]]]
    bot_public: NotRequired[Nullable[bool]]
    bot_require_code_grant: NotRequired[Nullable[bool]]
    terms_of_service_url: NotRequired[Nullable[str]]
    privacy_policy_url: NotRequired[Nullable[str]]
    custom_install_url: NotRequired[Nullable[str]]
    install_params: NotRequired[
        Nullable[ApplicationOAuth2InstallParamsResponseTypedDict]
    ]
    integration_types_config: NotRequired[
        Nullable[Dict[str, ApplicationIntegrationTypeConfigurationResponseTypedDict]]
    ]
    max_participants: NotRequired[Nullable[int]]
    tags: NotRequired[Nullable[List[str]]]


class ApplicationResponse(BaseModel):
    id: str

    name: str

    description: str

    verify_key: str

    flags: int

    icon: OptionalNullable[str] = UNSET

    TYPE: Annotated[
        Annotated[OptionalNullable[Literal[4]], AfterValidator(validate_const(4))],
        pydantic.Field(alias="type"),
    ] = 4

    cover_image: OptionalNullable[str] = UNSET

    primary_sku_id: OptionalNullable[str] = UNSET

    bot: OptionalNullable[UserResponse] = UNSET

    slug: OptionalNullable[str] = UNSET

    guild_id: OptionalNullable[str] = UNSET

    rpc_origins: OptionalNullable[List[str]] = UNSET

    bot_public: OptionalNullable[bool] = UNSET

    bot_require_code_grant: OptionalNullable[bool] = UNSET

    terms_of_service_url: OptionalNullable[str] = UNSET

    privacy_policy_url: OptionalNullable[str] = UNSET

    custom_install_url: OptionalNullable[str] = UNSET

    install_params: OptionalNullable[ApplicationOAuth2InstallParamsResponse] = UNSET

    integration_types_config: OptionalNullable[
        Dict[str, ApplicationIntegrationTypeConfigurationResponse]
    ] = UNSET

    max_participants: OptionalNullable[int] = UNSET

    tags: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "icon",
            "type",
            "cover_image",
            "primary_sku_id",
            "bot",
            "slug",
            "guild_id",
            "rpc_origins",
            "bot_public",
            "bot_require_code_grant",
            "terms_of_service_url",
            "privacy_policy_url",
            "custom_install_url",
            "install_params",
            "integration_types_config",
            "max_participants",
            "tags",
        ]
        nullable_fields = [
            "icon",
            "type",
            "cover_image",
            "primary_sku_id",
            "bot",
            "slug",
            "guild_id",
            "rpc_origins",
            "bot_public",
            "bot_require_code_grant",
            "terms_of_service_url",
            "privacy_policy_url",
            "custom_install_url",
            "install_params",
            "integration_types_config",
            "max_participants",
            "tags",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
