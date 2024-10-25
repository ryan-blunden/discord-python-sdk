# Templates
(*templates*)

## Overview

### Available Operations

* [get](#get)

## get

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.templates.get(code="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `code`                                                                                | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `security`                                                                            | [Optional[models.GetGuildTemplateSecurity]](../../models/getguildtemplatesecurity.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.GuildTemplateResponse](../../models/guildtemplateresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |