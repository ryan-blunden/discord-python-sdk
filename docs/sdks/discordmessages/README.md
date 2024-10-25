# DiscordMessages
(*webhooks.messages*)

## Overview

### Available Operations

* [delete_original](#delete_original)
* [get](#get)

## delete_original

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

s.webhooks.messages.delete_original(webhook_id="<value>", webhook_token="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                                  | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `webhook_token`                                                                                               | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `thread_id`                                                                                                   | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `security`                                                                                                    | [Optional[models.DeleteOriginalWebhookMessageSecurity]](../../models/deleteoriginalwebhookmessagesecurity.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhooks.messages.get(webhook_id="<value>", webhook_token="<value>", message_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `webhook_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `webhook_token`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `message_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `thread_id`                                                                             | *Optional[str]*                                                                         | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `security`                                                                              | [Optional[models.GetWebhookMessageSecurity]](../../models/getwebhookmessagesecurity.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |