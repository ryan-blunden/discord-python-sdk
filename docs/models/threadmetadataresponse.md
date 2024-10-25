# ThreadMetadataResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `archived`                                                           | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `locked`                                                             | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `archive_timestamp`                                                  | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `auto_archive_duration`                                              | *Literal[60]*                                                        | :heavy_check_mark:                                                   | N/A                                                                  |
| `create_timestamp`                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | N/A                                                                  |
| `invitable`                                                          | *OptionalNullable[bool]*                                             | :heavy_minus_sign:                                                   | N/A                                                                  |