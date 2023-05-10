from .step import Step
class Preflight(Step):
    def process(self, data, inputs, utils):
        print("in Preflight")
        utils.create_dirs()#先在抓影片加入txt時，新增資料夾。