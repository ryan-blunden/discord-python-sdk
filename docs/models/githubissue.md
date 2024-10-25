# GithubIssue


## Fields

| Field                                        | Type                                         | Required                                     | Description                                  |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| `id`                                         | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `number`                                     | *int*                                        | :heavy_check_mark:                           | N/A                                          |
| `html_url`                                   | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `user`                                       | [models.GithubUser](../models/githubuser.md) | :heavy_check_mark:                           | N/A                                          |
| `title`                                      | *str*                                        | :heavy_check_mark:                           | N/A                                          |
| `body`                                       | *OptionalNullable[str]*                      | :heavy_minus_sign:                           | N/A                                          |
| `pull_request`                               | *Optional[Any]*                              | :heavy_minus_sign:                           | N/A                                          |