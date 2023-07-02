import requests
import os
from dotenv import load_dotenv
import json
import random
import sys
import math


class VideoGetter():

    def __init__(self):
        self.current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.favorite_channels = self.get_favorite_channels()["channels"]
        self.api_key = self.get_api_key()
        self.base_url = "https://www.googleapis.com/youtube"
        self.api_version = "v3"

    def get_favorite_channels(self):
        favorite_channels_file = os.path.join(self.current_dir, "channels.json")
        with open(favorite_channels_file, "r") as f:
            return json.load(f)


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

    def get_random_favorite_channel(self):
            return self.favorite_channels[random.randint(0,len(self.favorite_channels)-1)]

    def get_page_count(self, query):
        res = requests.get(f"{self.base_url}/{self.api_version}/search?{query}")
        total_results = res.json()["pageInfo"]["totalResults"]
        results_per_page = res.json()["pageInfo"]["resultsPerPage"]
        return math.ceil(total_results / results_per_page)
    
    def get_random_page(self, query):
        page_count = self.get_page_count(query)
        return random.randint(1, page_count)
    
    def get_videos(self, page, query, page_token=None):
        endpoint = f"{self.base_url}/{self.api_version}/search?{query}"
        endpoint = f"{endpoint}&pageToken={page_token}" if page_token is not None else endpoint
        res = requests.get(endpoint)
        if page == 1:
            return res.json()["items"]
        else:
            next_page_token = res.json()["nextPageToken"]
            return self.get_videos(page - 1, query, next_page_token)
            
        

    

        

    def main(self):
        channel = self.get_random_favorite_channel()
        query = f"key={self.api_key}&type=video&part=id&maxResults=50&channelId={channel['channelId']}"
        page = self.get_random_page(query)
        videos = self.get_videos(page, query)
        random_index = random.randint(0,len(videos)-1)
        video = videos[random_index]
        video_id = video["id"]["videoId"]
        print(video_id)
        return video_id


if __name__ == "__main__":
    video_getter = VideoGetter()
    video_getter.main()
    #video_getter.get_channels("Learn English With TV Series")