import random


class KFold:
    def __init__(self):
        self.blocks = []
        self.scores = []

    #def get_score(self):

    def get_blocks(self, x, y):
        nums = [i for i in range(0, len(x))]
        for i in range(0, 8):
            block = []
            for j in range(0, int(len(x) / 8)):
                num = random.choice(nums)
                block.append(x[num])
                del x[num]
                block.append(y[num])
                del x[num]
                nums.pop()
            self.blocks.append(block)

    def get_ordered_blocks(self):
        ordered_blocks = []
        nums = [i for i in range(0, len(self.blocks))]
        for i in range(0, 4):
            block = []
            for j in range(0, 2):
                num = random.choice(nums)
                block.append(self.blocks[num])
            ordered_blocks.append(block)
        print(ordered_blocks)

    def cross_val(self, model, x, y):
        self.get_blocks(x, y)
        self.get_ordered_blocks()

