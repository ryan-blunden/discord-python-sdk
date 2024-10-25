# GuildApplicationCommands
(*guild_application_commands*)

## Overview

### Available Operations

* [list](#list)

## list

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.guild_application_commands.list(security=discord_sdk.ListGuildApplicationCommandsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [models.ListGuildApplicationCommandsSecurity](../../models/listguildapplicationcommandssecurity.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `application_id`                                                                                    | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `guild_id`                                                                                          | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `with_localizations`                                                                                | *Optional[bool]*                                                                                    | :heavy_minus_sign:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[List[models.ApplicationCommandResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |