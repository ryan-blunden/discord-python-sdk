# Commands
(*commands*)

## Overview

### Available Operations

* [list_permissions](#list_permissions)
* [set_permission](#set_permission)
* [bulk_set](#bulk_set)

## list_permissions

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.commands.list_permissions(security=discord_sdk.ListGuildApplicationCommandPermissionsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                               | Type                                                                                                                    | Required                                                                                                                | Description                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                              | [models.ListGuildApplicationCommandPermissionsSecurity](../../models/listguildapplicationcommandpermissionssecurity.md) | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `application_id`                                                                                                        | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `guild_id`                                                                                                              | *str*                                                                                                                   | :heavy_check_mark:                                                                                                      | N/A                                                                                                                     |
| `retries`                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                        | :heavy_minus_sign:                                                                                                      | Configuration to override the default retry behavior of the client.                                                     |

### Response

**[List[models.CommandPermissionsResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## set_permission

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.commands.set_permission(security=discord_sdk.SetGuildApplicationCommandPermissionsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", command_id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                  | [models.SetGuildApplicationCommandPermissionsSecurity](../../models/setguildapplicationcommandpermissionssecurity.md)       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `application_id`                                                                                                            | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `guild_id`                                                                                                                  | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `command_id`                                                                                                                | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `request_body`                                                                                                              | [models.SetGuildApplicationCommandPermissionsRequestBody](../../models/setguildapplicationcommandpermissionsrequestbody.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[models.CommandPermissionsResponse](../../models/commandpermissionsresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## bulk_set

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.commands.bulk_set(security=discord_sdk.BulkSetGuildApplicationCommandsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", request_body=[
    {
        "name": "<value>",
        "type": 1,
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                | [models.BulkSetGuildApplicationCommandsSecurity](../../models/bulksetguildapplicationcommandssecurity.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `application_id`                                                                                          | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `guild_id`                                                                                                | *str*                                                                                                     | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `request_body`                                                                                            | List[[models.ApplicationCommandUpdateRequest](../../models/applicationcommandupdaterequest.md)]           | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[List[models.ApplicationCommandResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |