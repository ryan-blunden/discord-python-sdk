# PartialGuildSubscriptionIntegrationResponse


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `id`                                                                     | *str*                                                                    | :heavy_check_mark:                                                       | N/A                                                                      |
| `type`                                                                   | *Literal["discord"]*                                                     | :heavy_check_mark:                                                       | N/A                                                                      |
| `name`                                                                   | *OptionalNullable[str]*                                                  | :heavy_minus_sign:                                                       | N/A                                                                      |
| `account`                                                                | [OptionalNullable[models.AccountResponse]](../models/accountresponse.md) | :heavy_minus_sign:                                                       | N/A                                                                      |