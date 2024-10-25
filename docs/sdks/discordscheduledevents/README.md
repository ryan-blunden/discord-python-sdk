# DiscordScheduledEvents
(*guilds.scheduled_events*)

## Overview

### Available Operations

* [update](#update)
* [list](#list)

## update

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guilds.scheduled_events.update(guild_id="<value>", guild_scheduled_event_id="<value>", request_body={
    "status": 1,
    "entity_type": 0,
    "privacy_level": 2,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `guild_id`                                                                                          | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `guild_scheduled_event_id`                                                                          | *str*                                                                                               | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `request_body`                                                                                      | [models.UpdateGuildScheduledEventRequestBody](../../models/updateguildscheduledeventrequestbody.md) | :heavy_check_mark:                                                                                  | N/A                                                                                                 |
| `retries`                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                    | :heavy_minus_sign:                                                                                  | Configuration to override the default retry behavior of the client.                                 |

### Response

**[models.UpdateGuildScheduledEventResponseBody](../../models/updateguildscheduledeventresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## list

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guilds.scheduled_events.list(guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guild_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `with_user_count`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ListGuildScheduledEventsResponseBody]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |