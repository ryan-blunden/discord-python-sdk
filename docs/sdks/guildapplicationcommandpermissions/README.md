# GuildApplicationCommandPermissions
(*guild_application_command_permissions*)

## Overview

### Available Operations

* [get](#get)

## get

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.guild_application_command_permissions.get(security=discord_sdk.GetGuildApplicationCommandPermissionsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", command_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                            | [models.GetGuildApplicationCommandPermissionsSecurity](../../models/getguildapplicationcommandpermissionssecurity.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `application_id`                                                                                                      | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `guild_id`                                                                                                            | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `command_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.CommandPermissionsResponse](../../models/commandpermissionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |