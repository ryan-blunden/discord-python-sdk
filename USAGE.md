<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from discord_sdk import Discord
import os

s = Discord(
    bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
)

res = s.oauth2_applications.get_my()

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from discord_sdk import Discord
import os

async def main():
    s = Discord(
        bot_token=os.getenv("DISCORD_BOT_TOKEN", ""),
    )
    res = await s.oauth2_applications.get_my_async()
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->