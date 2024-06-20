## IN THE CASE THAT IT BITES YOU TO INSTALL LIBRARIES LIKE PANDAS OR SOME OTHER LIBRARY, JUST INSTALL

### I had to install this (latest)
```
pip install browser_cookie3
pip install pandas
```
``I found the solution to the problem, I had the same errors but making some modifications and changing the type and the way in which I obtained the videos, I modified:

add two variables

``` Python
        user = api.user(username)
        videos = user.videos()
```
change the for to iterate over the videos found in the account and then another variable

``` Python

        async for video in videos:
            print(f"Username: {video.author.username}")
            print(f"Video ID: {video.id}")
            print(f"Stats: {video.stats}")

            video_url = f"https://www.tiktok.com/@{username}/video/{video.id}"
```

sincerely I do not know what differences there are with the other method (speaking of the variable video_url) but well it works and then I leave as this the part that downloads the video from YoutubeDL

and at the end of the code add the variable username in which will start the code that is the user that we want to download the videos, I clarify that this will download all the videos of the user from top to bottom.

```Python
if __name__ == "__main__":
    username = 'username'
    asyncio.run(download_user_videos(username))
```

and regarding the token, honestly I did not use the ms_token and I do not know what it is for hahahahahah xd but the token that worked for me was the "multi_sids" that is the domain tiktok.com SPECIFICALLY THAT one

code complete:

```Python
from TikTokApi import TikTokApi
from yt_dlp import YoutubeDL
import asyncio
import os

ms_token = os.environ.get("multi_sids", None) 
ydl_opts = {
    'outtmpl': '%(uploader)s_%(id)s_%(timestamp)s.%(ext)s',
}

async def download_user_videos(username):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, 
                                  headless=False, suppress_resource_load_types=["image", "media", "font", "stylesheet"])

        user = api.user(username)
        videos = user.videos()

        async for video in videos:
            print(f"Username: {video.author.username}")
            print(f"Video ID: {video.id}")
            print(f"Stats: {video.stats}")

            video_url = f"https://www.tiktok.com/@{username}/video/{video.id}"
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

if __name__ == "__main__":
    username = 'username'
    asyncio.run(download_user_videos(username))

```

I clarify that the verisions of the libraries I am using are:
```
Name: TikTokApi
Version: 6.3.0
```
```
Name: yt-dlp
Version: 2024.5.27
```