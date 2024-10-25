# GuildSoundboardSounds
(*guild_soundboard_sounds*)

## Overview

### Available Operations

* [update](#update)
* [create](#create)

## update

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guild_soundboard_sounds.update(guild_id="<value>", sound_id="<value>", soundboard_patch_request_partial={})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                             | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `guild_id`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `sound_id`                                                                            | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `soundboard_patch_request_partial`                                                    | [models.SoundboardPatchRequestPartial](../../models/soundboardpatchrequestpartial.md) | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `retries`                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                      | :heavy_minus_sign:                                                                    | Configuration to override the default retry behavior of the client.                   |

### Response

**[models.SoundboardSoundResponse](../../models/soundboardsoundresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## create

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.guild_soundboard_sounds.create(guild_id="<value>", soundboard_create_request={
    "name": "<value>",
    "sound": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                 | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `guild_id`                                                                | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `soundboard_create_request`                                               | [models.SoundboardCreateRequest](../../models/soundboardcreaterequest.md) | :heavy_check_mark:                                                        | N/A                                                                       |
| `retries`                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)          | :heavy_minus_sign:                                                        | Configuration to override the default retry behavior of the client.       |

### Response

**[models.SoundboardSoundResponse](../../models/soundboardsoundresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |