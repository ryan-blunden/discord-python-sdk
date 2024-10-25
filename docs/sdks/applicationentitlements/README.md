# ApplicationEntitlements
(*application_entitlements*)

## Overview

### Available Operations

* [consume](#consume)

## consume

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

s.application_entitlements.consume(security=discord_sdk.ConsumeEntitlementSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", entitlement_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `security`                                                                      | [models.ConsumeEntitlementSecurity](../../models/consumeentitlementsecurity.md) | :heavy_check_mark:                                                              | N/A                                                                             |
| `application_id`                                                                | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `entitlement_id`                                                                | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |