from pipeline.steps.get_video_list import GetVideoList
from pipeline.steps.step import StepException
from pipeline.steps.download_captions import DownloadCaptions
from pipeline.pipeline import Pipeline
from utils import Utils
from pipeline.steps.preflight import Preflight
from pipeline.steps.postflight import Postflight
from settings import API_KEY
import sys
sys.path.append('/Users/laijacky/Desktop/sideproject')
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
    p.run(inputs, utils)


if __name__ == "__main__":
    main()





#先找到data 有哪些class需要data哪些不需要
#大家繼承abc class 需要帶這麼多參數嗎？
#為什麼這幾個
#一個一個debug
#
