# ApplicationCommands
(*application_commands*)

## Overview

### Available Operations

* [get](#get)
* [update](#update)
* [create](#create)

## get

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.application_commands.get(security=discord_sdk.GetApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", command_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `security`                                                                            | [models.GetApplicationCommandSecurity](../../models/getapplicationcommandsecurity.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `application_id`                                                                      | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `command_id`                                                                          | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.ApplicationCommandResponse](../../models/applicationcommandresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.application_commands.update(security=discord_sdk.UpdateApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", command_id="<value>", application_command_patch_request_partial={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.UpdateApplicationCommandSecurity](../../models/updateapplicationcommandsecurity.md)           | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
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

## create

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.application_commands.create(security=discord_sdk.CreateApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", application_command_create_request={
    "name": "<value>",
    "type": 1,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.CreateApplicationCommandSecurity](../../models/createapplicationcommandsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `application_id`                                                                            | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `application_command_create_request`                                                        | [models.ApplicationCommandCreateRequest](../../models/applicationcommandcreaterequest.md)   | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Response

**[models.ApplicationCommandResponse](../../models/applicationcommandresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |