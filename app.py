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
