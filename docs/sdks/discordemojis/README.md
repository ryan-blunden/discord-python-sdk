# DiscordEmojis
(*applications.emojis*)

## Overview

### Available Operations

* [update](#update)

## update

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.emojis.update(application_id="<value>", emoji_id="<value>", request_body={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                     | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `application_id`                                                                              | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `emoji_id`                                                                                    | *str*                                                                                         | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `request_body`                                                                                | [models.UpdateApplicationEmojiRequestBody](../../models/updateapplicationemojirequestbody.md) | :heavy_check_mark:                                                                            | N/A                                                                                           |
| `retries`                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                              | :heavy_minus_sign:                                                                            | Configuration to override the default retry behavior of the client.                           |

### Response

**[models.EmojiResponse](../../models/emojiresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |