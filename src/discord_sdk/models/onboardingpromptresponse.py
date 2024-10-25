"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .onboardingpromptoptionresponse import (
    OnboardingPromptOptionResponse,
    OnboardingPromptOptionResponseTypedDict,
)
from discord_sdk.types import BaseModel
from discord_sdk.utils import validate_const
import pydantic
from pydantic.functional_validators import AfterValidator
from typing import List, Literal
from typing_extensions import Annotated, TypedDict


class OnboardingPromptResponseTypedDict(TypedDict):
    id: str
    title: str
    options: List[OnboardingPromptOptionResponseTypedDict]
    single_select: bool
    required: bool
    in_onboarding: bool
    type: Literal[0]


class OnboardingPromptResponse(BaseModel):
    id: str

    title: str

    options: List[OnboardingPromptOptionResponse]

    single_select: bool

    required: bool

    in_onboarding: bool

    TYPE: Annotated[
        Annotated[Literal[0], AfterValidator(validate_const(0))],
        pydantic.Field(alias="type"),
    ] = 0
