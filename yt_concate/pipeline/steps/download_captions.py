from pytube import YouTube
from utils import Utils
from .step import Step
import time


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data[:20]:#影片連結前20
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file")
                continue
            print(url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())

                text_file = open(utils.get_video_id_from_url(url) + ".txt", "w", encoding="utf-8")
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
            except (KeyError, AttributeError):
                print("error when downloaind caption for", url)
                en_caption_convert_to_srt = ""
                text_file = open(utils.get_video_id_from_url(url) + ".txt", "w", encoding="utf-8")
                text_file.write(en_caption_convert_to_srt)
                text_file.close()
        end = time.time()
        print("took", end - start, "s")


