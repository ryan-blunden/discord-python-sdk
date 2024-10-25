"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .errordetails import ErrorDetails
from discord_sdk import utils
from discord_sdk.types import BaseModel
from typing import Optional


class ErrorResponseData(BaseModel):
    code: int
    r"""Discord internal error code. See error code reference"""

    message: str
    r"""Human-readable error message"""

    errors: Optional[ErrorDetails] = None


class ErrorResponse(Exception):
    r"""Errors object returned by the Discord API"""

    data: ErrorResponseData

    def __init__(self, data: ErrorResponseData):
        self.data = data

    def __str__(self) -> str:
        return utils.marshal_json(self.data, ErrorResponseData)