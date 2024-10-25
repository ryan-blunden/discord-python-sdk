# ApplicationCommandSubcommandOptionResponse


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `name`                                       | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `description`                                | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `type`                                       | *Literal[1]*                                 | :heavy_check_mark:                           | N/A                                          |
| `name_localized`                             | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | N/A                                          |
| `name_localizations`                         | Dict[str, *str*]                             | :heavy_minus_sign:                           | N/A                                          |
| `description_localized`                      | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | N/A                                          |
| `description_localizations`                  | Dict[str, *str*]                             | :heavy_minus_sign:                           | N/A                                          |
| `required`                                   | *OptionalNullable[bool]*                     | :heavy_minus_sign:                           | N/A                                          |
| `options`                                    | List[[models.Options](../models/options.md)] | :heavy_minus_sign:                           | N/A                                          |