# GithubWebhook


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `sender`                                                                   | [models.GithubUser](../models/githubuser.md)                               | :heavy_check_mark:                                                         | N/A                                                                        |
| `action`                                                                   | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | N/A                                                                        |
| `ref`                                                                      | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | N/A                                                                        |
| `ref_type`                                                                 | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | N/A                                                                        |
| `comment`                                                                  | [OptionalNullable[models.GithubComment]](../models/githubcomment.md)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `issue`                                                                    | [OptionalNullable[models.GithubIssue]](../models/githubissue.md)           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `pull_request`                                                             | [OptionalNullable[models.GithubIssue]](../models/githubissue.md)           | :heavy_minus_sign:                                                         | N/A                                                                        |
| `repository`                                                               | [OptionalNullable[models.GithubRepository]](../models/githubrepository.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `forkee`                                                                   | [OptionalNullable[models.GithubRepository]](../models/githubrepository.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `member`                                                                   | [OptionalNullable[models.GithubUser]](../models/githubuser.md)             | :heavy_minus_sign:                                                         | N/A                                                                        |
| `release`                                                                  | [OptionalNullable[models.GithubRelease]](../models/githubrelease.md)       | :heavy_minus_sign:                                                         | N/A                                                                        |
| `head_commit`                                                              | [OptionalNullable[models.GithubCommit]](../models/githubcommit.md)         | :heavy_minus_sign:                                                         | N/A                                                                        |
| `commits`                                                                  | List[[models.GithubCommit](../models/githubcommit.md)]                     | :heavy_minus_sign:                                                         | N/A                                                                        |
| `forced`                                                                   | *OptionalNullable[bool]*                                                   | :heavy_minus_sign:                                                         | N/A                                                                        |
| `compare`                                                                  | *OptionalNullable[str]*                                                    | :heavy_minus_sign:                                                         | N/A                                                                        |
| `review`                                                                   | [OptionalNullable[models.GithubReview]](../models/githubreview.md)         | :heavy_minus_sign:                                                         | N/A                                                                        |
| `check_run`                                                                | [OptionalNullable[models.GithubCheckRun]](../models/githubcheckrun.md)     | :heavy_minus_sign:                                                         | N/A                                                                        |
| `check_suite`                                                              | [OptionalNullable[models.GithubCheckSuite]](../models/githubchecksuite.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `discussion`                                                               | [OptionalNullable[models.GithubDiscussion]](../models/githubdiscussion.md) | :heavy_minus_sign:                                                         | N/A                                                                        |
| `answer`                                                                   | [OptionalNullable[models.GithubComment]](../models/githubcomment.md)       | :heavy_minus_sign:                                                         | N/A                                                                        |