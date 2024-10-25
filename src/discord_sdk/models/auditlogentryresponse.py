"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .auditlogobjectchangeresponse import (
    AuditLogObjectChangeResponse,
    AuditLogObjectChangeResponseTypedDict,
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
from typing import Dict, List, Literal
from typing_extensions import Annotated, NotRequired, TypedDict


class AuditLogEntryResponseTypedDict(TypedDict):
    id: str
    action_type: Literal[1]
    user_id: NotRequired[Nullable[str]]
    target_id: NotRequired[Nullable[str]]
    changes: NotRequired[Nullable[List[AuditLogObjectChangeResponseTypedDict]]]
    options: NotRequired[Nullable[Dict[str, str]]]
    reason: NotRequired[Nullable[str]]


class AuditLogEntryResponse(BaseModel):
    id: str

    ACTION_TYPE: Annotated[
        Annotated[Literal[1], AfterValidator(validate_const(1))],
        pydantic.Field(alias="action_type"),
    ] = 1

    user_id: OptionalNullable[str] = UNSET

    target_id: OptionalNullable[str] = UNSET

    changes: OptionalNullable[List[AuditLogObjectChangeResponse]] = UNSET

    options: OptionalNullable[Dict[str, str]] = UNSET

    reason: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["user_id", "target_id", "changes", "options", "reason"]
        nullable_fields = ["user_id", "target_id", "changes", "options", "reason"]
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
