# DiscordGuilds
(*applications.guilds*)

## Overview

### Available Operations

* [update_command](#update_command)

## update_command

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.guilds.update_command(security=discord_sdk.UpdateGuildApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", command_id="<value>", application_command_patch_request_partial={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.UpdateGuildApplicationCommandSecurity](../../models/updateguildapplicationcommandsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `guild_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `command_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_command_patch_request_partial`                                                           | [models.ApplicationCommandPatchRequestPartial](../../models/applicationcommandpatchrequestpartial.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ApplicationCommandResponse](../../models/applicationcommandresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |