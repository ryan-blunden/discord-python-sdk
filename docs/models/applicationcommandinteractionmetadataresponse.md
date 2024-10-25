# ApplicationCommandInteractionMetadataResponse


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `id`                                                               | *str*                                                              | :heavy_check_mark:                                                 | N/A                                                                |
| `authorizing_integration_owners`                                   | Dict[str, *str*]                                                   | :heavy_check_mark:                                                 | N/A                                                                |
| `type`                                                             | *Literal[1]*                                                       | :heavy_check_mark:                                                 | N/A                                                                |
| `user`                                                             | [OptionalNullable[models.UserResponse]](../models/userresponse.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `original_response_message_id`                                     | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | N/A                                                                |
| `target_user`                                                      | [OptionalNullable[models.UserResponse]](../models/userresponse.md) | :heavy_minus_sign:                                                 | N/A                                                                |
| `target_message_id`                                                | *OptionalNullable[str]*                                            | :heavy_minus_sign:                                                 | N/A                                                                |