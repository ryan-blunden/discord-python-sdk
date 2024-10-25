# ChannelRecipients
(*channel_recipients*)

## Overview

### Available Operations

* [add](#add)

## add

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.channel_recipients.add(channel_id="<value>", user_id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `channel_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `user_id`                                                                     | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `request_body`                                                                | [models.AddGroupDmUserRequestBody](../../models/addgroupdmuserrequestbody.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.AddGroupDmUserResponseBody](../../models/addgroupdmuserresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |