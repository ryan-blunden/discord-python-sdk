# DiscordEntitlements
(*applications.entitlements*)

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

res = s.applications.entitlements.get(security=discord_sdk.GetEntitlementsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), request={
    "application_id": "<value>",
    "sku_ids": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [models.GetEntitlementsRequest](../../models/getentitlementsrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |
| `security`                                                              | [models.GetEntitlementsSecurity](../../getentitlementssecurity.md)      | :heavy_check_mark:                                                      | The security requirements to use for the request.                       |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[List[models.EntitlementResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |