# Overview

this code gets recomended Youtube video based on your favorite channels, and
automatically embed the video on Nontion.<br>
It is really useful if you learn a language but don't want to be bother to look up
a video for study everyday.

# Requirements

- use habit tracker in Notion to work with this.


## 1. Set up environment
```
> python -m venv venv
> .\venv\Scripts\activate
> pip install -r requirements.txt
```

## 2. Get your credentials
you need Google API Key and Notion Token to use this.<br>
Please follow the official documents respectively.


## 3. Create env file for your credentials.
please create env file and locate it in the same directory as main.py.<br>
the content of the file should be like this.
```
GOOGLE_API_KEY=AIzaSyAEC5kg_g5real54Am4rrea4uAMAZxpOdNVlriY
NOTION_TOKEN=secret_fHrSqPiJForeaSzUgYreJk25sCRjx1sjpKiQscJV1eyR
```

## 4. get channel Id of you favorite youtube channel
you can use get_channels method in get_youtube_video.py.<br>
the argument "q" should be something relevant to your favorite youtuber.<br>
Please edit channels.js accordingly.

## 5. run main.py
You are finally good to go!!
run the following command periodically and you hacked your life.
```
python main.py
```
