# Applications
(*applications*)

## Overview

### Available Operations

* [get_my](#get_my)
* [update_role_connections_metadata](#update_role_connections_metadata)
* [get_guild_command](#get_guild_command)
* [create_command](#create_command)
* [get_activity_instance](#get_activity_instance)
* [delete_entitlement](#delete_entitlement)
* [create_entitlement](#create_entitlement)
* [upload_attachment](#upload_attachment)
* [delete_command](#delete_command)
* [list_commands](#list_commands)
* [bulk_set_commands](#bulk_set_commands)
* [get](#get)
* [update](#update)

## get_my

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.get_my()

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PrivateApplicationResponse](../../models/privateapplicationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update_role_connections_metadata

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.update_role_connections_metadata(application_id="<value>", request_body=[
    {
        "key": "<key>",
        "name": "<value>",
        "description": "into powerfully likely near geez",
        "type": 1,
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                   | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `application_id`                                                                                                            | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `request_body`                                                                                                              | List[[models.ApplicationRoleConnectionsMetadataItemRequest](../../models/applicationroleconnectionsmetadataitemrequest.md)] | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `retries`                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                            | :heavy_minus_sign:                                                                                                          | Configuration to override the default retry behavior of the client.                                                         |

### Response

**[List[models.ApplicationRoleConnectionsMetadataItemResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get_guild_command

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.get_guild_command(security=discord_sdk.GetGuildApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", command_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.GetGuildApplicationCommandSecurity](../../models/getguildapplicationcommandsecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `application_id`                                                                                | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `guild_id`                                                                                      | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `command_id`                                                                                    | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.ApplicationCommandResponse](../../models/applicationcommandresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## create_command

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.create_command(security=discord_sdk.CreateGuildApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", guild_id="<value>", application_command_create_request={
    "name": "<value>",
    "type": 1,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                             | Type                                                                                                  | Required                                                                                              | Description                                                                                           |
| ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `security`                                                                                            | [models.CreateGuildApplicationCommandSecurity](../../models/createguildapplicationcommandsecurity.md) | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_id`                                                                                      | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `guild_id`                                                                                            | *str*                                                                                                 | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `application_command_create_request`                                                                  | [models.ApplicationCommandCreateRequest](../../models/applicationcommandcreaterequest.md)             | :heavy_check_mark:                                                                                    | N/A                                                                                                   |
| `retries`                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                      | :heavy_minus_sign:                                                                                    | Configuration to override the default retry behavior of the client.                                   |

### Response

**[models.ApplicationCommandResponse](../../models/applicationcommandresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get_activity_instance

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.get_activity_instance(application_id="<value>", instance_id="<id>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `instance_id`                                                       | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.EmbeddedActivityInstance](../../models/embeddedactivityinstance.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## delete_entitlement

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

s.applications.delete_entitlement(security=discord_sdk.DeleteEntitlementSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", entitlement_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `security`                                                                    | [models.DeleteEntitlementSecurity](../../models/deleteentitlementsecurity.md) | :heavy_check_mark:                                                            | N/A                                                                           |
| `application_id`                                                              | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `entitlement_id`                                                              | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## create_entitlement

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.create_entitlement(application_id="<value>", create_entitlement_request_data={
    "sku_id": "<value>",
    "owner_id": "<value>",
    "owner_type": 617153,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `application_id`                                                                    | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `create_entitlement_request_data`                                                   | [models.CreateEntitlementRequestData](../../models/createentitlementrequestdata.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.EntitlementResponse](../../models/entitlementresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## upload_attachment

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.upload_attachment(security=discord_sdk.UploadApplicationAttachmentSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", request_body={
    "file": "<value>",
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `security`                                                                                              | [models.UploadApplicationAttachmentSecurity](../../models/uploadapplicationattachmentsecurity.md)       | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `application_id`                                                                                        | *str*                                                                                                   | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `request_body`                                                                                          | [models.UploadApplicationAttachmentRequestBody](../../models/uploadapplicationattachmentrequestbody.md) | :heavy_check_mark:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.ActivitiesAttachmentResponse](../../models/activitiesattachmentresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## delete_command

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

s.applications.delete_command(security=discord_sdk.DeleteApplicationCommandSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", command_id="<value>")

# Use the SDK ...

```

### Parameters

| Parameter                                                                                   | Type                                                                                        | Required                                                                                    | Description                                                                                 |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `security`                                                                                  | [models.DeleteApplicationCommandSecurity](../../models/deleteapplicationcommandsecurity.md) | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `application_id`                                                                            | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `command_id`                                                                                | *str*                                                                                       | :heavy_check_mark:                                                                          | N/A                                                                                         |
| `retries`                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                            | :heavy_minus_sign:                                                                          | Configuration to override the default retry behavior of the client.                         |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## list_commands

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.list_commands(security=discord_sdk.ListApplicationCommandsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `security`                                                                                | [models.ListApplicationCommandsSecurity](../../models/listapplicationcommandssecurity.md) | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `application_id`                                                                          | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `with_localizations`                                                                      | *Optional[bool]*                                                                          | :heavy_minus_sign:                                                                        | N/A                                                                                       |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |

### Response

**[List[models.ApplicationCommandResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## bulk_set_commands

### Example Usage

```python
import discord_sdk
from discord_sdk import Discord
import os

s = Discord()

res = s.applications.bulk_set_commands(security=discord_sdk.BulkSetApplicationCommandsSecurity(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
), application_id="<value>", request_body=[
    {
        "name": "<value>",
        "type": 1,
    },
    {
        "name": "<value>",
        "type": 1,
    },
])

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `security`                                                                                      | [models.BulkSetApplicationCommandsSecurity](../../models/bulksetapplicationcommandssecurity.md) | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `application_id`                                                                                | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `request_body`                                                                                  | List[[models.ApplicationCommandUpdateRequest](../../models/applicationcommandupdaterequest.md)] | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[List[models.ApplicationCommandResponse]](../../models/.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## get

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.get(application_id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `application_id`                                                    | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PrivateApplicationResponse](../../models/privateapplicationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |

## update

### Example Usage

```python
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.applications.update(application_id="<value>", application_form_partial={
    "explicit_content_filter": 0,
    "type": 4,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `application_id`                                                        | *str*                                                                   | :heavy_check_mark:                                                      | N/A                                                                     |
| `application_form_partial`                                              | [models.ApplicationFormPartial](../../models/applicationformpartial.md) | :heavy_check_mark:                                                      | N/A                                                                     |
| `retries`                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)        | :heavy_minus_sign:                                                      | Configuration to override the default retry behavior of the client.     |

### Response

**[models.PrivateApplicationResponse](../../models/privateapplicationresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 4XX                  | application/json     |
| models.SDKError      | 5XX                  | \*/\*                |