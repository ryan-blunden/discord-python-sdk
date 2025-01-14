"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .sdkconfiguration import SDKConfiguration
from discord_sdk import models, utils
from discord_sdk._hooks import HookContext
from discord_sdk.discord_commands import DiscordCommands
from discord_sdk.types import OptionalNullable, UNSET
from discord_sdk.utils import get_security_from_env
from typing import Any, Optional, Union


class DiscordGuilds(BaseSDK):
    commands: DiscordCommands

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        BaseSDK.__init__(self, sdk_config)
        self.sdk_configuration = sdk_config
        self._init_sdks()

    def _init_sdks(self):
        self.commands = DiscordCommands(self.sdk_configuration)

    def update_command(
        self,
        *,
        security: Union[
            models.UpdateGuildApplicationCommandSecurity,
            models.UpdateGuildApplicationCommandSecurityTypedDict,
        ],
        application_id: str,
        guild_id: str,
        command_id: str,
        application_command_patch_request_partial: Union[
            models.ApplicationCommandPatchRequestPartial,
            models.ApplicationCommandPatchRequestPartialTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ApplicationCommandResponse:
        r"""
        :param security:
        :param application_id:
        :param guild_id:
        :param command_id:
        :param application_command_patch_request_partial:
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

        request = models.UpdateGuildApplicationCommandRequest(
            application_id=application_id,
            guild_id=guild_id,
            command_id=command_id,
            application_command_patch_request_partial=utils.get_pydantic_model(
                application_command_patch_request_partial,
                models.ApplicationCommandPatchRequestPartial,
            ),
        )

        req = self.build_request(
            method="PATCH",
            path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(
                security, models.UpdateGuildApplicationCommandSecurity
            ),
            get_serialized_body=lambda: utils.serialize_request_body(
                request.application_command_patch_request_partial,
                False,
                False,
                "json",
                models.ApplicationCommandPatchRequestPartial,
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
                operation_id="update_guild_application_command",
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
                http_res.text, models.ApplicationCommandResponse
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

    async def update_command_async(
        self,
        *,
        security: Union[
            models.UpdateGuildApplicationCommandSecurity,
            models.UpdateGuildApplicationCommandSecurityTypedDict,
        ],
        application_id: str,
        guild_id: str,
        command_id: str,
        application_command_patch_request_partial: Union[
            models.ApplicationCommandPatchRequestPartial,
            models.ApplicationCommandPatchRequestPartialTypedDict,
        ],
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> models.ApplicationCommandResponse:
        r"""
        :param security:
        :param application_id:
        :param guild_id:
        :param command_id:
        :param application_command_patch_request_partial:
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

        request = models.UpdateGuildApplicationCommandRequest(
            application_id=application_id,
            guild_id=guild_id,
            command_id=command_id,
            application_command_patch_request_partial=utils.get_pydantic_model(
                application_command_patch_request_partial,
                models.ApplicationCommandPatchRequestPartial,
            ),
        )

        req = self.build_request_async(
            method="PATCH",
            path="/applications/{application_id}/guilds/{guild_id}/commands/{command_id}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=utils.get_pydantic_model(
                security, models.UpdateGuildApplicationCommandSecurity
            ),
            get_serialized_body=lambda: utils.serialize_request_body(
                request.application_command_patch_request_partial,
                False,
                False,
                "json",
                models.ApplicationCommandPatchRequestPartial,
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
                operation_id="update_guild_application_command",
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
                http_res.text, models.ApplicationCommandResponse
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
