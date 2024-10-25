# GuildChannels
(*guild_channels*)

## Overview

### Available Operations

* [list](#list)

## list

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.guild_channels.list(security=discord_sdk.ListGuildChannelsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.ListGuildChannelsSecurity](../../models/listguildchannelssecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `guild_id`                                                                    | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[List[models.ListGuildChannelsResponseBody]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |