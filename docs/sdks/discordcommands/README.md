# DiscordCommands
(*applications.guilds.commands*)

## Overview

### Available Operations

* [delete](#delete)

## delete

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

s.applications.guilds.commands.delete(security=discord_sdk.DeleteGuildApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", command_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.DeleteGuildApplicationCommandSecurity](../../models/deleteguildapplicationcommandsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `guild_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `command_id`                                                                                          | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |