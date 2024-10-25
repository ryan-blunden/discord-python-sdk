# Widget
(*guilds.widget*)

## Overview

### Available Operations

* [get_png](#get_png)

## get_png

### Example Usage

```python
from discord_sdk import Discord

s = Discord()

res = s.guilds.widget.get_png(guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `guild_id`                                                                              | *str*                                                                                   | :heavy_check_mark:                                                                      | N/A                                                                                     |
| `security`                                                                              | [Optional[models.GetGuildWidgetPngSecurity]](../../models/getguildwidgetpngsecurity.md) | :heavy_minus_sign:                                                                      | N/A                                                                                     |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |