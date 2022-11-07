from pytube import YouTube
from yt_concate.yt_concate.utils import Utils
from yt_concate.yt_concate.pipeline.steps.step import Step



class DownloadCaptions(Step):
    def process(self, data, inputs):
        start = time.time()
        for url in data:
            print("downloading caption for", url)
            if utils.caption_file_exists(url):
                print("found existing caption file")
                continue
            print(url)
            try:
            source = YouTube(url)

            en_caption = source.captions.get_by_language_code('en')
            en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except (KeyError, AttributeError):
                print("error when downloaind caption for", url)
            #print(en_caption_convert_to_srt)
            # save the caption to a file named Output.txt

            text_file = open(utils.get_video_id_from_url(url) + ".txt", "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
        end = time.time()
        print("took", end - start, "s")

