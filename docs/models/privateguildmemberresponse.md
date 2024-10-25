# PrivateGuildMemberResponse


## Fields

| Field                                                                                              | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `flags`                                                                                            | *int*                                                                                              | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `joined_at`                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                               | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `pending`                                                                                          | *bool*                                                                                             | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `roles`                                                                                            | List[*str*]                                                                                        | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `user`                                                                                             | [models.UserResponse](../models/userresponse.md)                                                   | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `mute`                                                                                             | *bool*                                                                                             | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `deaf`                                                                                             | *bool*                                                                                             | :heavy_check_mark:                                                                                 | N/A                                                                                                |
| `avatar`                                                                                           | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `avatar_decoration_data`                                                                           | [OptionalNullable[models.UserAvatarDecorationResponse]](../models/useravatardecorationresponse.md) | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `banner`                                                                                           | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `communication_disabled_until`                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                               | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `nick`                                                                                             | *OptionalNullable[str]*                                                                            | :heavy_minus_sign:                                                                                 | N/A                                                                                                |
| `premium_since`                                                                                    | [date](https://docs.python.org/3/library/datetime.html#date-objects)                               | :heavy_minus_sign:                                                                                 | N/A                                                                                                |