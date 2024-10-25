# AutoModeration
(*guilds.auto_moderation*)

## Overview

### Available Operations

* [get_rule](#get_rule)
* [update_rule](#update_rule)
* [list_rules](#list_rules)

## get_rule

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guilds.auto_moderation.get_rule(guild_id="<value>", rule_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guild_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `rule_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetAutoModerationRuleResponseBody](../../models/getautomoderationruleresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_rule

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guilds.auto_moderation.update_rule(guild_id="<value>", rule_id="<value>", request_body={
    "event_type": 1,
    "trigger_type": 1,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `guild_id`                                                                                        | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `rule_id`                                                                                         | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `request_body`                                                                                    | [models.UpdateAutoModerationRuleRequestBody](../../models/updateautomoderationrulerequestbody.md) | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.UpdateAutoModerationRuleResponseBody](../../models/updateautomoderationruleresponsebody.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## list_rules

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guilds.auto_moderation.list_rules(guild_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `guild_id`                                                          | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.ResponseBody]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |