"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from discord_sdk import models, utils
from discord_sdk._hooks import HookContext
from discord_sdk.types import OptionalNullable, UNSET
from discord_sdk.utils import get_security_from_env
from typing import Any, List, Optional, Union


class GuildApplicationCommands(BaseSDK):
    def list(
        self,
        *,
        security: Union[
            models.ListGuildApplicationCommandsSecurity,
            models.ListGuildApplicationCommandsSecurityTypedDict,
        ],
        application_id: str,
        guild_id: str,
        with_localizations: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> List[models.ApplicationCommandResponse]:
        r"""
        :param security:
        :param application_id:
        :param guild_id:
        :param with_localizations:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListGuildApplicationCommandsRequest(
            application_id=application_id,
            guild_id=guild_id,
            with_localizations=with_localizations,
        )

        req = self.build_request(
            method="GET",
            path="/applications/{application_id}/guilds/{guild_id}/commands",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(
                security, models.ListGuildApplicationCommandsSecurity
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="list_guild_application_commands",
                oauth2_scopes=["applications.commands.update"],
                security_source=get_security_from_env(security, models.Security),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, List[models.ApplicationCommandResponse]
            )
        if utils.match_response(http_res, "4XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def list_async(
        self,
        *,
        security: Union[
            models.ListGuildApplicationCommandsSecurity,
            models.ListGuildApplicationCommandsSecurityTypedDict,
        ],
        application_id: str,
        guild_id: str,
        with_localizations: Optional[bool] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> List[models.ApplicationCommandResponse]:
        r"""
        :param security:
        :param application_id:
        :param guild_id:
        :param with_localizations:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListGuildApplicationCommandsRequest(
            application_id=application_id,
            guild_id=guild_id,
            with_localizations=with_localizations,
        )

        req = self.build_request_async(
            method="GET",
            path="/applications/{application_id}/guilds/{guild_id}/commands",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(
                security, models.ListGuildApplicationCommandsSecurity
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="list_guild_application_commands",
                oauth2_scopes=["applications.commands.update"],
                security_source=get_security_from_env(security, models.Security),
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, List[models.ApplicationCommandResponse]
            )
        if utils.match_response(http_res, "4XX", "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ErrorResponseData)
            raise models.ErrorResponse(data=data)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
