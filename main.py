from linear_regression import LinearRegression
from train_test_split import TrainTestSplit
import matplotlib.pyplot as plt
from csv_reader import CSVReader

f = CSVReader()
f.read(csv="autos_prepared.csv")

x_train, x_test, y_train, y_test = TrainTestSplit().split(x=f.data["powerPS"], y=f.data["price"])

model = LinearRegression()
model.train(x=x_train, y=y_train)

print("Fehler              |", model.error)
print("Durchschnittsfehler |", model.avg_error)
print("a                   |", model.a)
print("b                   |", model.b)
print("Bestimmtheitsmaß    |", model.score(xs=x_test, ys=y_test))

predicted = model.predict(x_test)

plt.scatter(x_train, y_train)
plt.scatter(x_test, y_test, color="green")
plt.plot(x_test, predicted, color="red")
plt.show()

