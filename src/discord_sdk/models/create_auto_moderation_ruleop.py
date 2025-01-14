"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .defaultkeywordlistupsertrequest import (
    DefaultKeywordListUpsertRequest,
    DefaultKeywordListUpsertRequestTypedDict,
)
from .defaultkeywordruleresponse import (
    DefaultKeywordRuleResponse,
    DefaultKeywordRuleResponseTypedDict,
)
from .keywordruleresponse import KeywordRuleResponse, KeywordRuleResponseTypedDict
from .keywordupsertrequest import KeywordUpsertRequest, KeywordUpsertRequestTypedDict
from .mentionspamruleresponse import (
    MentionSpamRuleResponse,
    MentionSpamRuleResponseTypedDict,
)
from .mentionspamupsertrequest import (
    MentionSpamUpsertRequest,
    MentionSpamUpsertRequestTypedDict,
)
from .mlspamruleresponse import MLSpamRuleResponse, MLSpamRuleResponseTypedDict
from .mlspamupsertrequest import MLSpamUpsertRequest, MLSpamUpsertRequestTypedDict
from .spamlinkruleresponse import SpamLinkRuleResponse, SpamLinkRuleResponseTypedDict
from discord_sdk.types import BaseModel
from discord_sdk.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Union
from typing_extensions import Annotated, TypedDict


CreateAutoModerationRuleRequestBodyTypedDict = Union[
    DefaultKeywordListUpsertRequestTypedDict,
    KeywordUpsertRequestTypedDict,
    MLSpamUpsertRequestTypedDict,
    MentionSpamUpsertRequestTypedDict,
]


CreateAutoModerationRuleRequestBody = Union[
    DefaultKeywordListUpsertRequest,
    KeywordUpsertRequest,
    MLSpamUpsertRequest,
    MentionSpamUpsertRequest,
]


class CreateAutoModerationRuleRequestTypedDict(TypedDict):
    guild_id: str
    request_body: CreateAutoModerationRuleRequestBodyTypedDict


class CreateAutoModerationRuleRequest(BaseModel):
    guild_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]

    request_body: Annotated[
        CreateAutoModerationRuleRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]


CreateAutoModerationRuleResponseBodyTypedDict = Union[
    DefaultKeywordRuleResponseTypedDict,
    KeywordRuleResponseTypedDict,
    MLSpamRuleResponseTypedDict,
    MentionSpamRuleResponseTypedDict,
    SpamLinkRuleResponseTypedDict,
]
r"""200 response for create_auto_moderation_rule"""


CreateAutoModerationRuleResponseBody = Union[
    DefaultKeywordRuleResponse,
    KeywordRuleResponse,
    MLSpamRuleResponse,
    MentionSpamRuleResponse,
    SpamLinkRuleResponse,
]
r"""200 response for create_auto_moderation_rule"""
