from errors import InvalidDataError

import random


class TrainTestSplit:
    def __init__(self):
        self.x = []
        self.y = []

    @staticmethod
    def throw_exceptions(x, y):
        if len(x) == 0 or len(y) == 0:
            raise InvalidDataError("x or y parameter is missing!")
        if len(x) != len(y):
            raise InvalidDataError("length of x and y has to be the same!")

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def split(self, x=[], y=[], test_size=0.25):
        self.throw_exceptions(x, y)
        self.set_values(x, y)
        x_train = self.x
        x_test = []
        y_train = self.y
        y_test = []
        nums = [x for x in range(0, len(x_train))]
        for i in range(0, int(len(self.x) * test_size)):
            num = random.choice(nums)
            x_test.append(x_train[num])
            del x_train[num]
            y_test.append(y_train[num])
            del y_train[num]
            nums.pop()

        return x_train, x_test, y_train, y_test
