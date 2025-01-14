"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .onboardingpromptoptionrequest import (
    OnboardingPromptOptionRequest,
    OnboardingPromptOptionRequestTypedDict,
)
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
from typing import List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateOnboardingPromptRequestTypedDict(TypedDict):
    title: str
    options: List[OnboardingPromptOptionRequestTypedDict]
    id: str
    single_select: NotRequired[Nullable[bool]]
    required: NotRequired[Nullable[bool]]
    in_onboarding: NotRequired[Nullable[bool]]
    type: Nullable[Literal[0]]


class UpdateOnboardingPromptRequest(BaseModel):
    title: str

    options: List[OnboardingPromptOptionRequest]

    id: str

    single_select: OptionalNullable[bool] = UNSET

    required: OptionalNullable[bool] = UNSET

    in_onboarding: OptionalNullable[bool] = UNSET

    TYPE: Annotated[
        Annotated[OptionalNullable[Literal[0]], AfterValidator(validate_const(0))],
        pydantic.Field(alias="type"),
    ] = 0

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["single_select", "required", "in_onboarding", "type"]
        nullable_fields = ["single_select", "required", "in_onboarding", "type"]
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
