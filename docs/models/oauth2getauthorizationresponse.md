# OAuth2GetAuthorizationResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `application`                                                        | [models.ApplicationResponse](../models/applicationresponse.md)       | :heavy_check_mark:                                                   | N/A                                                                  |
| `expires`                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `scopes`                                                             | List[*str*]                                                          | :heavy_check_mark:                                                   | N/A                                                                  |
| `user`                                                               | [OptionalNullable[models.UserResponse]](../models/userresponse.md)   | :heavy_minus_sign:                                                   | N/A                                                                  |