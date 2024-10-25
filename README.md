# discord-sdk

Developer-friendly & type-safe Python SDK specifically catered to leverage *discord-sdk* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=discord-sdk&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/ryan-blunden-l5y/ryan-blunden). Delete this section before > publishing to a package manager.

<!-- Start Summary [summary] -->
## Summary

Discord HTTP API (Preview): Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

For more information about the API: [Discord Developer Documentation](https://discord.com/developers/docs)
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents

* [SDK Installation](#sdk-installation)
* [IDE Support](#ide-support)
* [SDK Example Usage](#sdk-example-usage)
* [Available Resources and Operations](#available-resources-and-operations)
* [Retries](#retries)
* [Error Handling](#error-handling)
* [Server Selection](#server-selection)
* [Custom HTTP Client](#custom-http-client)
* [Authentication](#authentication)
* [Debugging](#debugging)
<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from discord_sdk import Discord
import os

async def main():
    s = Discord(
        bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
    )
    res = await s.oauth2_applications.get_my_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [application_commands](docs/sdks/applicationcommands/README.md)

* [get](docs/sdks/applicationcommands/README.md#get)
* [update](docs/sdks/applicationcommands/README.md#update)
* [create](docs/sdks/applicationcommands/README.md#create)

### [application_emojis](docs/sdks/applicationemojis/README.md)

* [get](docs/sdks/applicationemojis/README.md#get)
* [list](docs/sdks/applicationemojis/README.md#list)
* [create](docs/sdks/applicationemojis/README.md#create)

### [application_entitlements](docs/sdks/applicationentitlements/README.md)

* [consume](docs/sdks/applicationentitlements/README.md#consume)

### [application_role_connections](docs/sdks/applicationroleconnections/README.md)

* [update](docs/sdks/applicationroleconnections/README.md#update)
* [get_metadata](docs/sdks/applicationroleconnections/README.md#get_metadata)

### [applications](docs/sdks/applications/README.md)

* [get_my](docs/sdks/applications/README.md#get_my)
* [update_role_connections_metadata](docs/sdks/applications/README.md#update_role_connections_metadata)
* [get_guild_command](docs/sdks/applications/README.md#get_guild_command)
* [create_command](docs/sdks/applications/README.md#create_command)
* [get_activity_instance](docs/sdks/applications/README.md#get_activity_instance)
* [delete_entitlement](docs/sdks/applications/README.md#delete_entitlement)
* [create_entitlement](docs/sdks/applications/README.md#create_entitlement)
* [upload_attachment](docs/sdks/applications/README.md#upload_attachment)
* [delete_command](docs/sdks/applications/README.md#delete_command)
* [list_commands](docs/sdks/applications/README.md#list_commands)
* [bulk_set_commands](docs/sdks/applications/README.md#bulk_set_commands)
* [get](docs/sdks/applications/README.md#get)
* [update](docs/sdks/applications/README.md#update)

#### [applications.emojis](docs/sdks/discordemojis/README.md)

* [update](docs/sdks/discordemojis/README.md#update)

#### [applications.entitlements](docs/sdks/discordentitlements/README.md)

* [get](docs/sdks/discordentitlements/README.md#get)

#### [applications.guilds](docs/sdks/discordguilds/README.md)

* [update_command](docs/sdks/discordguilds/README.md#update_command)

#### [applications.guilds.commands](docs/sdks/discordcommands/README.md)

* [delete](docs/sdks/discordcommands/README.md#delete)

#### [applications.role_connection](docs/sdks/roleconnection/README.md)

* [get_user](docs/sdks/roleconnection/README.md#get_user)
* [delete_user](docs/sdks/roleconnection/README.md#delete_user)

### [auto_moderation_rules](docs/sdks/automoderationrules/README.md)

* [delete](docs/sdks/automoderationrules/README.md#delete)
* [create](docs/sdks/automoderationrules/README.md#create)

### [bans](docs/sdks/bans/README.md)

* [get](docs/sdks/bans/README.md#get)

### [channel_followers](docs/sdks/channelfollowers/README.md)

* [follow](docs/sdks/channelfollowers/README.md#follow)

### [channel_invites](docs/sdks/channelinvites/README.md)

* [list](docs/sdks/channelinvites/README.md#list)
* [create](docs/sdks/channelinvites/README.md#create)

### [channel_message_reactions](docs/sdks/channelmessagereactions/README.md)

* [add_self](docs/sdks/channelmessagereactions/README.md#add_self)

### [channel_messages](docs/sdks/channelmessages/README.md)

* [create_thread_from_message](docs/sdks/channelmessages/README.md#create_thread_from_message)
* [update_json](docs/sdks/channelmessages/README.md#update_json)
* [update_form](docs/sdks/channelmessages/README.md#update_form)
* [update_multipart](docs/sdks/channelmessages/README.md#update_multipart)
* [delete](docs/sdks/channelmessages/README.md#delete)

### [channel_permissions](docs/sdks/channelpermissions/README.md)

* [delete_overwrite](docs/sdks/channelpermissions/README.md#delete_overwrite)

### [channel_pins](docs/sdks/channelpins/README.md)

* [pin](docs/sdks/channelpins/README.md#pin)

### [channel_recipients](docs/sdks/channelrecipients/README.md)

* [add](docs/sdks/channelrecipients/README.md#add)

### [channel_thread_members](docs/sdks/channelthreadmembers/README.md)

* [delete](docs/sdks/channelthreadmembers/README.md#delete)
* [list](docs/sdks/channelthreadmembers/README.md#list)

### [channels](docs/sdks/channels/README.md)

* [get_thread_member](docs/sdks/channels/README.md#get_thread_member)
* [create_webhook](docs/sdks/channels/README.md#create_webhook)
* [trigger_typing_indicator](docs/sdks/channels/README.md#trigger_typing_indicator)
* [list_pinned_messages](docs/sdks/channels/README.md#list_pinned_messages)
* [get](docs/sdks/channels/README.md#get)
* [delete](docs/sdks/channels/README.md#delete)
* [update](docs/sdks/channels/README.md#update)

#### [channels.messages](docs/sdks/discordchannelsmessages/README.md)

* [list](docs/sdks/discordchannelsmessages/README.md#list)
* [create_json](docs/sdks/discordchannelsmessages/README.md#create_json)
* [create_form](docs/sdks/discordchannelsmessages/README.md#create_form)
* [create_multipart](docs/sdks/discordchannelsmessages/README.md#create_multipart)

#### [channels.permissions](docs/sdks/permissions/README.md)

* [set_overwrite](docs/sdks/permissions/README.md#set_overwrite)

#### [channels.polls](docs/sdks/polls/README.md)

* [expire](docs/sdks/polls/README.md#expire)

#### [channels.threads](docs/sdks/discordthreads/README.md)

* [list_private_archived](docs/sdks/discordthreads/README.md#list_private_archived)

#### [channels.webhooks](docs/sdks/discordwebhooks/README.md)

* [list](docs/sdks/discordwebhooks/README.md#list)

### [commands](docs/sdks/commands/README.md)

* [list_permissions](docs/sdks/commands/README.md#list_permissions)
* [set_permission](docs/sdks/commands/README.md#set_permission)
* [bulk_set](docs/sdks/commands/README.md#bulk_set)


### [dms](docs/sdks/dms/README.md)

* [delete_user](docs/sdks/dms/README.md#delete_user)

### [emojis](docs/sdks/emojis/README.md)

* [delete](docs/sdks/emojis/README.md#delete)

### [entitlements](docs/sdks/entitlements/README.md)

* [get](docs/sdks/entitlements/README.md#get)

### [gateway](docs/sdks/gateway/README.md)

* [get](docs/sdks/gateway/README.md#get)

### [gateway_bot](docs/sdks/gatewaybot/README.md)

* [get](docs/sdks/gatewaybot/README.md#get)

### [guild_application_command_permissions](docs/sdks/guildapplicationcommandpermissions/README.md)

* [get](docs/sdks/guildapplicationcommandpermissions/README.md#get)

### [guild_application_commands](docs/sdks/guildapplicationcommands/README.md)

* [list](docs/sdks/guildapplicationcommands/README.md#list)

### [guild_bans](docs/sdks/guildbans/README.md)

* [list](docs/sdks/guildbans/README.md#list)

### [guild_channels](docs/sdks/guildchannels/README.md)

* [list](docs/sdks/guildchannels/README.md#list)

### [guild_emojis](docs/sdks/guildemojis/README.md)

* [delete](docs/sdks/guildemojis/README.md#delete)
* [create](docs/sdks/guildemojis/README.md#create)

### [guild_integrations](docs/sdks/guildintegrations/README.md)

* [delete](docs/sdks/guildintegrations/README.md#delete)
* [list](docs/sdks/guildintegrations/README.md#list)

### [guild_members](docs/sdks/guildmembers/README.md)

* [search](docs/sdks/guildmembers/README.md#search)
* [update_self](docs/sdks/guildmembers/README.md#update_self)
* [add](docs/sdks/guildmembers/README.md#add)
* [delete](docs/sdks/guildmembers/README.md#delete)
* [list](docs/sdks/guildmembers/README.md#list)

### [guild_mfa](docs/sdks/guildmfa/README.md)

* [set_level](docs/sdks/guildmfa/README.md#set_level)

### [guild_preview](docs/sdks/guildpreview/README.md)

* [get](docs/sdks/guildpreview/README.md#get)

### [guild_soundboard_sounds](docs/sdks/guildsoundboardsounds/README.md)

* [update](docs/sdks/guildsoundboardsounds/README.md#update)
* [create](docs/sdks/guildsoundboardsounds/README.md#create)

### [guild_stickers](docs/sdks/guildstickers/README.md)

* [update](docs/sdks/guildstickers/README.md#update)
* [list](docs/sdks/guildstickers/README.md#list)
* [create](docs/sdks/guildstickers/README.md#create)

### [guild_templates](docs/sdks/guildtemplates/README.md)

* [delete](docs/sdks/guildtemplates/README.md#delete)
* [create](docs/sdks/guildtemplates/README.md#create)

### [guild_voice_regions](docs/sdks/guildvoiceregions/README.md)

* [list](docs/sdks/guildvoiceregions/README.md#list)

### [guild_voice_states](docs/sdks/guildvoicestates/README.md)

* [get_self](docs/sdks/guildvoicestates/README.md#get_self)
* [update_self](docs/sdks/guildvoicestates/README.md#update_self)
* [get](docs/sdks/guildvoicestates/README.md#get)

### [guild_webhooks](docs/sdks/guildwebhooks/README.md)

* [get](docs/sdks/guildwebhooks/README.md#get)

### [guild_welcome_screen](docs/sdks/guildwelcomescreen/README.md)

* [get](docs/sdks/guildwelcomescreen/README.md#get)

### [guilds](docs/sdks/guilds/README.md)

* [create](docs/sdks/guilds/README.md#create)
* [leave](docs/sdks/guilds/README.md#leave)
* [create_from_template](docs/sdks/guilds/README.md#create_from_template)
* [get_new_member_welcome](docs/sdks/guilds/README.md#get_new_member_welcome)
* [get_scheduled_event](docs/sdks/guilds/README.md#get_scheduled_event)
* [create_scheduled_event](docs/sdks/guilds/README.md#create_scheduled_event)
* [update_welcome_screen](docs/sdks/guilds/README.md#update_welcome_screen)
* [get_widget](docs/sdks/guilds/README.md#get_widget)
* [update_onboarding](docs/sdks/guilds/README.md#update_onboarding)
* [get_vanity_url](docs/sdks/guilds/README.md#get_vanity_url)
* [update_template](docs/sdks/guilds/README.md#update_template)
* [list_templates](docs/sdks/guilds/README.md#list_templates)
* [bulk_ban_users](docs/sdks/guilds/README.md#bulk_ban_users)
* [create_channel](docs/sdks/guilds/README.md#create_channel)
* [bulk_update_channels](docs/sdks/guilds/README.md#bulk_update_channels)
* [get_member](docs/sdks/guilds/README.md#get_member)
* [get_emoji](docs/sdks/guilds/README.md#get_emoji)
* [update_emoji](docs/sdks/guilds/README.md#update_emoji)
* [list_emojis](docs/sdks/guilds/README.md#list_emojis)
* [get_widget_settings](docs/sdks/guilds/README.md#get_widget_settings)
* [create_role](docs/sdks/guilds/README.md#create_role)
* [preview_prune](docs/sdks/guilds/README.md#preview_prune)
* [prune](docs/sdks/guilds/README.md#prune)
* [ban_user](docs/sdks/guilds/README.md#ban_user)
* [unban_user](docs/sdks/guilds/README.md#unban_user)
* [get](docs/sdks/guilds/README.md#get)
* [delete](docs/sdks/guilds/README.md#delete)
* [update](docs/sdks/guilds/README.md#update)

#### [guilds.audit_logs](docs/sdks/auditlogs/README.md)

* [list_entries](docs/sdks/auditlogs/README.md#list_entries)

#### [guilds.auto_moderation](docs/sdks/automoderation/README.md)

* [get_rule](docs/sdks/automoderation/README.md#get_rule)
* [update_rule](docs/sdks/automoderation/README.md#update_rule)
* [list_rules](docs/sdks/automoderation/README.md#list_rules)

#### [guilds.members](docs/sdks/members/README.md)

* [update](docs/sdks/members/README.md#update)

#### [guilds.members.roles](docs/sdks/discordguildsroles/README.md)

* [add](docs/sdks/discordguildsroles/README.md#add)

#### [guilds.onboarding](docs/sdks/onboarding/README.md)

* [get](docs/sdks/onboarding/README.md#get)

#### [guilds.roles](docs/sdks/discordroles/README.md)

* [delete](docs/sdks/discordroles/README.md#delete)
* [update](docs/sdks/discordroles/README.md#update)
* [bulk_update](docs/sdks/discordroles/README.md#bulk_update)

#### [guilds.scheduled_events](docs/sdks/discordscheduledevents/README.md)

* [update](docs/sdks/discordscheduledevents/README.md#update)
* [list](docs/sdks/discordscheduledevents/README.md#list)

#### [guilds.soundboard_sounds](docs/sdks/discordguildssoundboardsounds/README.md)

* [get](docs/sdks/discordguildssoundboardsounds/README.md#get)

#### [guilds.soundboards](docs/sdks/soundboards/README.md)

* [list](docs/sdks/soundboards/README.md#list)

#### [guilds.templates](docs/sdks/discordtemplates/README.md)

* [sync](docs/sdks/discordtemplates/README.md#sync)

#### [guilds.threads](docs/sdks/discordguildsthreads/README.md)

* [list_active](docs/sdks/discordguildsthreads/README.md#list_active)

#### [guilds.voice_states](docs/sdks/voicestates/README.md)

* [update](docs/sdks/voicestates/README.md#update)

#### [guilds.widget](docs/sdks/widget/README.md)

* [get_png](docs/sdks/widget/README.md#get_png)

#### [guilds.widgets](docs/sdks/widgets/README.md)

* [update_settings](docs/sdks/widgets/README.md#update_settings)

### [invites](docs/sdks/invites/README.md)

* [list](docs/sdks/invites/README.md#list)
* [resolve](docs/sdks/invites/README.md#resolve)
* [revoke](docs/sdks/invites/README.md#revoke)

### [message_reactions](docs/sdks/messagereactions/README.md)

* [delete_all_by_emoji](docs/sdks/messagereactions/README.md#delete_all_by_emoji)

### [messages](docs/sdks/messages/README.md)

* [delete_my_reaction](docs/sdks/messages/README.md#delete_my_reaction)
* [bulk_delete](docs/sdks/messages/README.md#bulk_delete)
* [delete_user_reaction](docs/sdks/messages/README.md#delete_user_reaction)
* [delete_all_reactions](docs/sdks/messages/README.md#delete_all_reactions)
* [crosspost](docs/sdks/messages/README.md#crosspost)
* [get](docs/sdks/messages/README.md#get)

#### [messages.pins](docs/sdks/pins/README.md)

* [unpin](docs/sdks/pins/README.md#unpin)

#### [messages.reactions](docs/sdks/reactions/README.md)

* [list_by_emoji](docs/sdks/reactions/README.md#list_by_emoji)

### [my_applications](docs/sdks/myapplications/README.md)

* [update](docs/sdks/myapplications/README.md#update)

### [my_guilds](docs/sdks/myguilds/README.md)

* [list](docs/sdks/myguilds/README.md#list)

### [oauth2](docs/sdks/oauth2/README.md)

* [get_my_authorization](docs/sdks/oauth2/README.md#get_my_authorization)

### [oauth2_applications](docs/sdks/oauth2applications/README.md)

* [get_my](docs/sdks/oauth2applications/README.md#get_my)

### [oauth2_keys](docs/sdks/oauth2keys/README.md)

* [get](docs/sdks/oauth2keys/README.md#get)

### [poll_answers](docs/sdks/pollanswers/README.md)

* [get_voters](docs/sdks/pollanswers/README.md#get_voters)

### [roles](docs/sdks/roles/README.md)

* [delete_member_role](docs/sdks/roles/README.md#delete_member_role)
* [get](docs/sdks/roles/README.md#get)
* [list](docs/sdks/roles/README.md#list)

### [scheduled_events](docs/sdks/scheduledevents/README.md)

* [list_users](docs/sdks/scheduledevents/README.md#list_users)
* [delete](docs/sdks/scheduledevents/README.md#delete)

### [soundboard_default_sounds](docs/sdks/soundboarddefaultsounds/README.md)

* [list](docs/sdks/soundboarddefaultsounds/README.md#list)

### [soundboard_sounds](docs/sdks/soundboardsounds/README.md)

* [send](docs/sdks/soundboardsounds/README.md#send)
* [delete](docs/sdks/soundboardsounds/README.md#delete)

### [stage_instances](docs/sdks/stageinstances/README.md)

* [create](docs/sdks/stageinstances/README.md#create)
* [get](docs/sdks/stageinstances/README.md#get)
* [delete](docs/sdks/stageinstances/README.md#delete)
* [update](docs/sdks/stageinstances/README.md#update)

### [sticker_packs](docs/sdks/stickerpacks/README.md)

* [list](docs/sdks/stickerpacks/README.md#list)
* [get](docs/sdks/stickerpacks/README.md#get)

### [stickers](docs/sdks/stickers/README.md)

* [get](docs/sdks/stickers/README.md#get)
* [delete](docs/sdks/stickers/README.md#delete)
* [fetch_by_id](docs/sdks/stickers/README.md#fetch_by_id)

### [templates](docs/sdks/templates/README.md)

* [get](docs/sdks/templates/README.md#get)

### [threads](docs/sdks/threads/README.md)

* [list_my_private_archived](docs/sdks/threads/README.md#list_my_private_archived)
* [list_public_archived](docs/sdks/threads/README.md#list_public_archived)
* [join](docs/sdks/threads/README.md#join)
* [leave](docs/sdks/threads/README.md#leave)
* [add_member](docs/sdks/threads/README.md#add_member)
* [create](docs/sdks/threads/README.md#create)

### [users](docs/sdks/users/README.md)

* [list_my_connections](docs/sdks/users/README.md#list_my_connections)
* [create_dm](docs/sdks/users/README.md#create_dm)
* [get_me](docs/sdks/users/README.md#get_me)
* [update_my](docs/sdks/users/README.md#update_my)
* [get_my_guild_member](docs/sdks/users/README.md#get_my_guild_member)
* [get](docs/sdks/users/README.md#get)

### [voice_regions](docs/sdks/voiceregions/README.md)

* [list](docs/sdks/voiceregions/README.md#list)

### [webhook_messages](docs/sdks/webhookmessages/README.md)

* [get_original](docs/sdks/webhookmessages/README.md#get_original)
* [update_original_json](docs/sdks/webhookmessages/README.md#update_original_json)
* [update_original_form](docs/sdks/webhookmessages/README.md#update_original_form)
* [update_original_multipart](docs/sdks/webhookmessages/README.md#update_original_multipart)
* [update_json](docs/sdks/webhookmessages/README.md#update_json)
* [update_form](docs/sdks/webhookmessages/README.md#update_form)
* [update_multipart](docs/sdks/webhookmessages/README.md#update_multipart)

### [webhooks](docs/sdks/webhooks/README.md)

* [delete_message](docs/sdks/webhooks/README.md#delete_message)
* [execute_github_compatible](docs/sdks/webhooks/README.md#execute_github_compatible)
* [execute_slack_compatible](docs/sdks/webhooks/README.md#execute_slack_compatible)
* [get_by_token](docs/sdks/webhooks/README.md#get_by_token)
* [delete_by_token](docs/sdks/webhooks/README.md#delete_by_token)
* [update_by_token](docs/sdks/webhooks/README.md#update_by_token)
* [get](docs/sdks/webhooks/README.md#get)
* [delete](docs/sdks/webhooks/README.md#delete)
* [update](docs/sdks/webhooks/README.md#update)

#### [webhooks.messages](docs/sdks/discordmessages/README.md)

* [delete_original](docs/sdks/discordmessages/README.md#delete_original)
* [get](docs/sdks/discordmessages/README.md#get)

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from discord.utils import BackoffStrategy, RetryConfig
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my(,
    RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

if res is not None:
    # handle response
    pass

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from discord.utils import BackoffStrategy, RetryConfig
from discord_sdk import Discord
import os

s = Discord(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a models.SDKError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `get_my_async` method may raise the following exceptions:

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

### Example

```python
from discord_sdk import Discord, models
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = None
try:
    res = s.oauth2_applications.get_my()

    if res is not None:
        # handle response
        pass

except models.ErrorResponse as e:
    # handle e.data: models.ErrorResponseData
    raise(e)
except models.SDKError as e:
    # handle exception
    raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://discord.com/api/v10` | None |

#### Example

```python
from discord_sdk import Discord
import os

s = Discord(
    server_idx=0,
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from discord_sdk import Discord
import os

s = Discord(
    server_url="https://discord.com/api/v10",
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from discord_sdk import Discord
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Discord(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from discord_sdk import Discord
from discord_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Discord(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name                 | Type                 | Scheme               | Environment Variable |
| -------------------- | -------------------- | -------------------- | -------------------- |
| `bot_token`          | apiKey               | API key              | `DISCORD_BOT_TOKEN`  |

To authenticate with the API the `bot_token` parameter must be set when initializing the SDK client instance. For example:
```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass

```

### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.users.list_my_connections(security=discord_sdk.ListMyConnectionsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
))

if res is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from discord_sdk import Discord
import logging

logging.basicConfig(level=logging.DEBUG)
s = Discord(debug_logger=logging.getLogger("discord_sdk"))
```

You can also enable a default debug logger by setting an environment variable `DISCORD_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=discord-sdk&utm_campaign=python)
