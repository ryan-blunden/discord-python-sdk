# GuildTemplateResponse


## Fields

| Field                                                                              | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `code`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `name`                                                                             | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `usage_count`                                                                      | *int*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `creator_id`                                                                       | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `created_at`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_check_mark:                                                                 | N/A                                                                                |
| `updated_at`                                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects)               | :heavy_check_mark:                                                                 | N/A                                                                                |
| `source_guild_id`                                                                  | *str*                                                                              | :heavy_check_mark:                                                                 | N/A                                                                                |
| `serialized_source_guild`                                                          | [models.GuildTemplateSnapshotResponse](../models/guildtemplatesnapshotresponse.md) | :heavy_check_mark:                                                                 | N/A                                                                                |
| `description`                                                                      | *OptionalNullable[str]*                                                            | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `creator`                                                                          | [OptionalNullable[models.UserResponse]](../models/userresponse.md)                 | :heavy_minus_sign:                                                                 | N/A                                                                                |
| `is_dirty`                                                                         | *OptionalNullable[bool]*                                                           | :heavy_minus_sign:                                                                 | N/A                                                                                |