# GuildMfa
(*guild_mfa*)

## Overview

### Available Operations

* [set_level](#set_level)

## set_level

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guild_mfa.set_level(guild_id="<value>", request_body={
    "level": 0,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `guild_id`                                                                        | *str*                                                                             | :heavy_check_mark:                                                                | N/A                                                                               |
| `request_body`                                                                    | [models.SetGuildMfaLevelRequestBody](../../models/setguildmfalevelrequestbody.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.GuildMFALevelResponse](../../models/guildmfalevelresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |