# WidgetResponse


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `id`                                                     | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `name`                                                   | *str*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `channels`                                               | List[[models.WidgetChannel](../models/widgetchannel.md)] | :heavy_check_mark:                                       | N/A                                                      |
| `members`                                                | List[[models.WidgetMember](../models/widgetmember.md)]   | :heavy_check_mark:                                       | N/A                                                      |
| `presence_count`                                         | *int*                                                    | :heavy_check_mark:                                       | N/A                                                      |
| `instant_invite`                                         | *OptionalNullable[str]*                                  | :heavy_minus_sign:                                       | N/A                                                      |