from get_youtube_video import VideoGetter
from embed_to_notion import NotionEmbeder
import traceback

class Main():

    def main():
        try:
            video_getter = VideoGetter()
            video_id = video_getter.main()
            embeder = NotionEmbeder(video_id)
            embeder.main()
        except Exception as e:
            print(traceback.format_exc())    # いつものTracebackが表示される
            traceback.print_exc()   
        finally:
            input("実行が終了しました。")


if __name__ == "__main__":
    Main.main()