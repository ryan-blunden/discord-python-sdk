# Permissions
(*channels.permissions*)

## Overview

### Available Operations

* [set_overwrite](#set_overwrite)

## set_overwrite

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

s.channels.permissions.set_overwrite(channel_id="<value>", overwrite_id="<value>", request_body={
    "type": 0,
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `channel_id`                                                                                                | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `overwrite_id`                                                                                              | *str*                                                                                                       | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `request_body`                                                                                              | [models.SetChannelPermissionOverwriteRequestBody](../../models/setchannelpermissionoverwriterequestbody.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |