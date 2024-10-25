# WebhookMessages
(*webhook_messages*)

## Overview

### Available Operations

* [get_original](#get_original)
* [update_original_json](#update_original_json)
* [update_original_form](#update_original_form)
* [update_original_multipart](#update_original_multipart)
* [update_json](#update_json)
* [update_form](#update_form)
* [update_multipart](#update_multipart)

## get_original

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.get_original(webhook_id="<value>", webhook_token="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                            | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `webhook_token`                                                                                         | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `thread_id`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `security`                                                                                              | [Optional[models.GetOriginalWebhookMessageSecurity]](../../models/getoriginalwebhookmessagesecurity.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_original_json

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_original_json(webhook_id="<value>", webhook_token="<value>", incoming_webhook_update_request_partial={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `webhook_token`                                                                                                       | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `incoming_webhook_update_request_partial`                                                                             | [models.IncomingWebhookUpdateRequestPartial](../../models/incomingwebhookupdaterequestpartial.md)                     | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `thread_id`                                                                                                           | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `security`                                                                                                            | [Optional[models.UpdateOriginalWebhookMessageJSONSecurity]](../../models/updateoriginalwebhookmessagejsonsecurity.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_original_form

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_original_form(webhook_id="<value>", webhook_token="<value>", incoming_webhook_update_request_partial={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                                          | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `webhook_token`                                                                                                       | *str*                                                                                                                 | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `incoming_webhook_update_request_partial`                                                                             | [models.IncomingWebhookUpdateRequestPartial](../../models/incomingwebhookupdaterequestpartial.md)                     | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `thread_id`                                                                                                           | *Optional[str]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `security`                                                                                                            | [Optional[models.UpdateOriginalWebhookMessageFormSecurity]](../../models/updateoriginalwebhookmessageformsecurity.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_original_multipart

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_original_multipart(webhook_id="<value>", webhook_token="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                       | Type                                                                                                                            | Required                                                                                                                        | Description                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `webhook_id`                                                                                                                    | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `webhook_token`                                                                                                                 | *str*                                                                                                                           | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `request_body`                                                                                                                  | [models.UpdateOriginalWebhookMessageMultipartRequestBody](../../models/updateoriginalwebhookmessagemultipartrequestbody.md)     | :heavy_check_mark:                                                                                                              | N/A                                                                                                                             |
| `thread_id`                                                                                                                     | *Optional[str]*                                                                                                                 | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `security`                                                                                                                      | [Optional[models.UpdateOriginalWebhookMessageMultipartSecurity]](../../models/updateoriginalwebhookmessagemultipartsecurity.md) | :heavy_minus_sign:                                                                                                              | N/A                                                                                                                             |
| `retries`                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                | :heavy_minus_sign:                                                                                                              | Configuration to override the default retry behavior of the client.                                                             |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_json

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_json(request={
    "webhook_id": "<value>",
    "webhook_token": "<value>",
    "message_id": "<value>",
    "incoming_webhook_update_request_partial": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.UpdateWebhookMessageJSONRequest](../../models/updatewebhookmessagejsonrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `security`                                                                                | [models.UpdateWebhookMessageJSONSecurity](../../updatewebhookmessagejsonsecurity.md)      | :heavy_check_mark:                                                                        | The security requirements to use for the request.                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_form

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_form(request={
    "webhook_id": "<value>",
    "webhook_token": "<value>",
    "message_id": "<value>",
    "incoming_webhook_update_request_partial": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `request`                                                                                 | [models.UpdateWebhookMessageFormRequest](../../models/updatewebhookmessageformrequest.md) | :heavy_check_mark:                                                                        | The request object to use for the request.                                                |
| `security`                                                                                | [models.UpdateWebhookMessageFormSecurity](../../updatewebhookmessageformsecurity.md)      | :heavy_check_mark:                                                                        | The security requirements to use for the request.                                         |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_multipart

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.webhook_messages.update_multipart(request={
    "webhook_id": "<value>",
    "webhook_token": "<value>",
    "message_id": "<value>",
    "request_body": {},
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `request`                                                                                           | [models.UpdateWebhookMessageMultipartRequest](../../models/updatewebhookmessagemultipartrequest.md) | :heavy_check_mark:                                                                                  | The request object to use for the request.                                                          |
| `security`                                                                                          | [models.UpdateWebhookMessageMultipartSecurity](../../updatewebhookmessagemultipartsecurity.md)      | :heavy_check_mark:                                                                                  | The security requirements to use for the request.                                                   |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.MessageResponse](../../models/messageresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |