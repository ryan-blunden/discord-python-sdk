# ErrorResponse

Errors object returned by the Discord API


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `code`                                                     | *int*                                                      | :heavy_check_mark:                                         | Discord internal error code. See error code reference      |
| `message`                                                  | *str*                                                      | :heavy_check_mark:                                         | Human-readable error message                               |
| `errors`                                                   | [Optional[models.ErrorDetails]](../models/errordetails.md) | :heavy_minus_sign:                                         | N/A                                                        |