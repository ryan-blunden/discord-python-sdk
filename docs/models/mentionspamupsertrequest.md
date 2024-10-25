# MentionSpamUpsertRequest


## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `name`                                                                                         | *str*                                                                                          | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `event_type`                                                                                   | *Literal[1]*                                                                                   | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `actions`                                                                                      | List[[models.MentionSpamUpsertRequestActions](../models/mentionspamupsertrequestactions.md)]   | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `enabled`                                                                                      | *OptionalNullable[bool]*                                                                       | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `exempt_roles`                                                                                 | List[*str*]                                                                                    | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `exempt_channels`                                                                              | List[*str*]                                                                                    | :heavy_minus_sign:                                                                             | N/A                                                                                            |
| `trigger_type`                                                                                 | *Literal[1]*                                                                                   | :heavy_check_mark:                                                                             | N/A                                                                                            |
| `trigger_metadata`                                                                             | [OptionalNullable[models.MentionSpamTriggerMetadata]](../models/mentionspamtriggermetadata.md) | :heavy_minus_sign:                                                                             | N/A                                                                                            |