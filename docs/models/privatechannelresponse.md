# PrivateChannelResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `type`                                                               | [models.Type](../models/type.md)                                     | :heavy_check_mark:                                                   | N/A                                                                  |
| `flags`                                                              | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `recipients`                                                         | List[[models.UserResponse](../models/userresponse.md)]               | :heavy_check_mark:                                                   | N/A                                                                  |
| `last_message_id`                                                    | *OptionalNullable[str]*                                              | :heavy_minus_sign:                                                   | N/A                                                                  |
| `last_pin_timestamp`                                                 | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |