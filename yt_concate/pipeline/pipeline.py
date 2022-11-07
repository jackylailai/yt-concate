from .steps.step import StepException


class Pipeline:
    def __init__(self,steps):
        self.steps = steps

    def run(self, data, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print("Exception happend:",e)
                break