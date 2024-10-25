# Error

A single error, either for an API response or a specific field.


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `code`                                                | *int*                                                 | :heavy_check_mark:                                    | Discord internal error code. See error code reference |
| `message`                                             | *str*                                                 | :heavy_check_mark:                                    | Human-readable error message                          |