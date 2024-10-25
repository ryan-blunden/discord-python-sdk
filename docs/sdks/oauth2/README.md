# Oauth2
(*oauth2*)

## Overview

### Available Operations

* [get_my_authorization](#get_my_authorization)

## get_my_authorization

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.oauth2.get_my_authorization(security=discord_sdk.GetMyOauth2AuthorizationSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
))

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `security`                                                                           | [models.GetMyOauth2AuthorizationSecurity](../../getmyoauth2authorizationsecurity.md) | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |
| `retries`                                                                            | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                     | :heavy_minus_sign:                                                                   | Configuration to override the default retry behavior of the client.                  |

### Response

**[models.OAuth2GetAuthorizationResponse](../../models/oauth2getauthorizationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |