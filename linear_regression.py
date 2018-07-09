from errors import InvalidDataError, PredictionError


class LinearRegression:
    def __init__(self):
        self.x = []
        self.y = []
        self.a = 0
        self.b = 0
        self.error = 500000000000000
        self.avg_error = 5000000000000

    @staticmethod
    def throw_exceptions(x, y):
        if len(x) == 0 or len(y) == 0:
            raise InvalidDataError("x or y parameter is missing!")
        if len(x) != len(y):
            raise InvalidDataError("length of x and y has to be the same!")

    def set_values(self, x, y):
        self.x = x
        self.y = y

    def average(self, l):
        sum = 0
        for value in l:
            sum += value
        return sum / len(l)

    def train(self, x=[], y=[]):
        self.throw_exceptions(x, y)
        self.set_values(x, y)
        x_avg = self.average(self.x)
        y_avg = self.average(self.y)
        numerator = 0
        for i in range(0, len(self.x)):
            numerator += (self.x[i] - x_avg) * (self.y[i] - y_avg)
        denominator = 0
        for x in self.x:
            denominator += (x - x_avg) ** 2
        self.a = numerator / denominator
        self.b = y_avg - self.a * x_avg

    def predict(self, xl):
        if self.error == 5000000:
            raise PredictionError("Please call LinearRegression.train() method before predicting!")
        predicted = []
        for x in xl:
            predicted.append(self.a * x + self.b)
        return predicted

    def score(self, xs, ys):
        y_avg = self.average(ys)
        sum_pred = 0
        sum_avg = 0
        for i in range(0, len(xs)):
            sum_pred += (ys[i] - self.predict([xs[i]])[0]) ** 2
            sum_avg += (ys[i] - y_avg) ** 2
        r2 = 1 - sum_pred / sum_avg
        return r2


