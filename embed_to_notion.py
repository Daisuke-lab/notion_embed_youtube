import os
from dotenv import load_dotenv
import datetime
import requests
import sys
from datetime import datetime, timedelta, timezone


class NotionEmbeder():
    def __init__(self, video_id):
        self.current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.video_id = video_id
        self.base_url = "https://api.notion.com"
        self.api_version = "v1"
        JST = timezone(timedelta(hours=+9), 'JST')
        self.today = datetime.datetime.now(JST).strftime("%Y-%m-%d")
        self.headers = self.get_headers()

        

    def get_headers(self):
        env_file = os.path.join(self.current_dir, ".env")
        load_dotenv(env_file)
        token = os.environ.get("NOTION_TOKEN")
        headers = {
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "Authorization": f"Bearer {token}"
        }
        return headers
    
    def get_today_page_id(self):
        payload = {
            "filter": {
            "value": 'page',
            "property": 'object'
            },
            "sort": {
            "direction": 'descending',
            "timestamp": 'last_edited_time'
            },
            "page_size": 5,
        }
        endpoint = f"{self.base_url}/{self.api_version}/search"
        res = requests.post(endpoint, json=payload, headers=self.headers)
        pages = res.json()["results"]
        for page in pages:
            print(page)
            date = page.get("properties", {}).get("Day", {}).get("title", [{}])[0].get("plain_text")
            if date == self.today:
                return page["id"]
            
    def add_today_video(self, page_id):
        video_block = {
            "type": "video",
            'archived': False,
            'video': {
                'caption': [],
                'type': 'external',
                'external': {
                    'url': f'https://www.youtube.com/embed/{self.video_id}'
                    }
                    }
        }
        payload = {"children":[
            video_block
        ]}
        endpoint = f"{self.base_url}/{self.api_version}/blocks/{page_id}/children"
        res = requests.patch(endpoint, headers=self.headers, json=payload)

    def main(self):
        page_id = self.get_today_page_id()
        self.add_today_video(page_id)


if __name__ == "__main__":
    video_id = "Zp5sy59veFo"
    embeder = NotionEmbeder(video_id)
    embeder.main()