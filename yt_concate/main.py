from yt_concate.yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.yt_concate.pipeline.steps.step import StepException
from yt_concate.yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.yt_concate.pipeline.pipeline import Pipeline
from yt_concate.yt_concate.utils import Utils
from yt_concate.yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.yt_concate.pipeline.steps.postflight import Postflight
# import urllib.request
# import json
from yt_concate.yt_concate.settings import API_KEY

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"
print(API_KEY)


def main():
    inputs = {
        "channel_id": CHANNEL_ID
    }
    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),

    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(data,inputs, utils)


if __name__ == "__main__":
    main()

# def get_all_video_in_channel(CHANNEL_ID):
#
#
#     base_video_url = 'https://www.youtube.com/watch?v='
#     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
#
#     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY, CHANNEL_ID)
#
#     video_links = []
#     url = first_url
#     while True:
#         inp = urllib.request.urlopen(url)
#         resp = json.load(inp)
#
#         for i in resp['items']:
#             if i['id']['kind'] == "youtube#video":
#                 video_links.append(base_video_url + i['id']['videoId'])
#
#         try:
#             next_page_token = resp['nextPageToken']
#             url = first_url + '&pageToken={}'.format(next_page_token)
#         except KeyError:
#             break
#     return video_links
#
#
# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_list))




#先找到data 有哪些class需要data哪些不需要
#大家繼承abc class 需要帶這麼多參數嗎？
#為什麼這幾個
#一個一個debug
#
