# Emojis
(*emojis*)

## Overview

### Available Operations

* [delete](#delete)

## delete

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

s.emojis.delete(application_id="<value>", emoji_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `emoji_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |