class Pipeline:
    def __init__(self):
        self.stages = []

    def add(self, stage):
        self.stages.append(stage)
    
    def execute(self, input):
        for stage in self.stages:
            input = stage.process(input)
        return input
