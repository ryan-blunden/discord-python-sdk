# GetEntitlementsRequest


## Fields

| Field                                | Type                                 | Required                             | Description                          |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `application_id`                     | *str*                                | :heavy_check_mark:                   | N/A                                  |
| `sku_ids`                            | [models.SkuIds](../models/skuids.md) | :heavy_check_mark:                   | N/A                                  |
| `user_id`                            | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `guild_id`                           | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `before`                             | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `after`                              | *Optional[str]*                      | :heavy_minus_sign:                   | N/A                                  |
| `limit`                              | *Optional[int]*                      | :heavy_minus_sign:                   | N/A                                  |
| `exclude_ended`                      | *Optional[bool]*                     | :heavy_minus_sign:                   | N/A                                  |
| `only_active`                        | *Optional[bool]*                     | :heavy_minus_sign:                   | N/A                                  |