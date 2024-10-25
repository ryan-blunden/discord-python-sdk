# PollResponse


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `question`                                                           | [models.PollMediaResponse](../models/pollmediaresponse.md)           | :heavy_check_mark:                                                   | N/A                                                                  |
| `answers`                                                            | List[[models.PollAnswerResponse](../models/pollanswerresponse.md)]   | :heavy_check_mark:                                                   | N/A                                                                  |
| `expiry`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |
| `allow_multiselect`                                                  | *bool*                                                               | :heavy_check_mark:                                                   | N/A                                                                  |
| `layout_type`                                                        | *int*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `results`                                                            | [models.PollResultsResponse](../models/pollresultsresponse.md)       | :heavy_check_mark:                                                   | N/A                                                                  |