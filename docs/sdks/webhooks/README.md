# Webhooks
(*webhooks*)

## Overview

### Available Operations

* [delete_message](#delete_message)
* [execute_github_compatible](#execute_github_compatible)
* [execute_slack_compatible](#execute_slack_compatible)
* [get_by_token](#get_by_token)
* [delete_by_token](#delete_by_token)
* [update_by_token](#update_by_token)
* [get](#get)
* [delete](#delete)
* [update](#update)

## delete_message

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

s.webhooks.delete_message(webhook_id="<value>", webhook_token="<value>", message_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `webhook_token`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `message_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `thread_id`                                                                                   | *Optional[str]*                                                                               | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `security`                                                                                    | [Optional[models.DeleteWebhookMessageSecurity]](../../models/deletewebhookmessagesecurity.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## execute_github_compatible

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

s.webhooks.execute_github_compatible(request={
    "webhook_id": "<value>",
    "webhook_token": "<value>",
    "github_webhook": {
        "sender": {
            "id": 61384,
            "login": "Erica.Hodkiewicz",
            "html_url": "https://muddy-bob.com",
            "avatar_url": "https://pretty-mantua.net",
        },
    },
})

# Use the SDK ...

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `request`                                                                                             | [models.ExecuteGithubCompatibleWebhookRequest](../../models/executegithubcompatiblewebhookrequest.md) | :heavy_check_mark:                                                                                    | The request object to use for the request.                                                            |
| `security`                                                                                            | [models.ExecuteGithubCompatibleWebhookSecurity](../../executegithubcompatiblewebhooksecurity.md)      | :heavy_check_mark:                                                                                    | The security requirements to use for the request.                                                     |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## execute_slack_compatible

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhooks.execute_slack_compatible(request={
    "webhook_id": "<value>",
    "webhook_token": "<value>",
    "slack_webhook": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.ExecuteSlackCompatibleWebhookRequest](../../models/executeslackcompatiblewebhookrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `security`                                                                                          | [models.ExecuteSlackCompatibleWebhookSecurity](../../executeslackcompatiblewebhooksecurity.md)      | :heavy_check_mark:                                                                                  | The security requirements to use for the request.                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[str](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get_by_token

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhooks.get_by_token(webhook_id="<value>", webhook_token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `webhook_id`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `webhook_token`                                                                         | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `security`                                                                              | [Optional[models.GetWebhookByTokenSecurity]](../../models/getwebhookbytokensecurity.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[models.GetWebhookByTokenResponseBody](../../models/getwebhookbytokenresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## delete_by_token

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

s.webhooks.delete_by_token(webhook_id="<value>", webhook_token="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `webhook_token`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `security`                                                                                    | [Optional[models.DeleteWebhookByTokenSecurity]](../../models/deletewebhookbytokensecurity.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_by_token

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhooks.update_by_token(webhook_id="<value>", webhook_token="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                  | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `webhook_token`                                                                               | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `request_body`                                                                                | [models.UpdateWebhookByTokenRequestBody](../../models/updatewebhookbytokenrequestbody.md)     | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `security`                                                                                    | [Optional[models.UpdateWebhookByTokenSecurity]](../../models/updatewebhookbytokensecurity.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.UpdateWebhookByTokenResponseBody](../../models/updatewebhookbytokenresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.webhooks.get(webhook_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetWebhookResponseBody](../../models/getwebhookresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## delete

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

s.webhooks.delete(webhook_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `webhook_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.webhooks.update(webhook_id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `webhook_id`                                                                | *str*                                                                       | :heavy_check_mark:                                                          | N/A                                                                         |
| `request_body`                                                              | [models.UpdateWebhookRequestBody](../../models/updatewebhookrequestbody.md) | :heavy_check_mark:                                                          | N/A                                                                         |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.UpdateWebhookResponseBody](../../models/updatewebhookresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |