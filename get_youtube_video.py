import requests
import os
from dotenv import load_dotenv
import json
import random
import sys

class VideoGetter():

    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.favorite_channels = self.get_favorite_channels()["channels"]
        self.favorite_channel = self.favorite_channels[random.randint(0,len(self.favorite_channels)-1)]
        self.api_key = self.get_api_key()
        self.base_url = "https://www.googleapis.com/youtube"
        self.api_version = "v3"

    def get_favorite_channels(self):
        favorite_channels_file = os.path.join(self.current_dir, "channels.json")
        with open(favorite_channels_file, "r") as f:
            return json.load(f)

    def get_last_videos(self):
        pass

    def get_api_key(self):
        env_file = os.path.join(self.current_dir, ".env")
        load_dotenv(env_file)
        return os.environ.get("GOOGLE_API_KEY")
    
    def get_channels(self, q):
        query = f"key={self.api_key}&type=channel&part=snippet&q={q}"
        res = requests.get(f"{self.base_url}/{self.api_version}/search?{query}")
        channels = res.json()["items"]
        for channel in channels:
            print("Channel Id::", channel["snippet"]["channelId"])
            print("Description::", channel["snippet"]["description"])
            print("Image::", channel["snippet"]["thumbnails"]["default"]["url"])
            print("------------------------------------------------------")

    

        

    def main(self):
        query = f"key={self.api_key}&type=video&part=id&maxResults=50&channelId={self.favorite_channel['channelId']}"
        res = requests.get(f"{self.base_url}/{self.api_version}/search?{query}")
        videos = res.json()["items"]
        random_index = random.randint(0,len(videos)-1)
        video = videos[random_index]
        video_id = video["id"]["videoId"]
        return video_id


if __name__ == "__main__":
    video_getter = VideoGetter()
    print(video_getter)
    #video_getter.get_channels("mayuko inoue")