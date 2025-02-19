import math
import random
import datetime
import requests
import matplotlib.pyplot as plt
from flask import Flask

# Math Module
x = 16
y = 2
print(math.sqrt(x))
print(math.pow(x, y))
print(math.pi)

# Random Module
names = ["Alice", "Bob", "Charlie"]
print(random.randint(1, 10))
print(random.choice(names))
random.shuffle(names)
print(names)

# Datetime Module
now = datetime.datetime.now()
print(now)
specific_date = datetime.date(2024, 2, 19)
print(specific_date)
time_diff = datetime.timedelta(days=5)
print(now + time_diff)

# Requests Module
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

# Matplotlib Example
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Sample Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Flask App
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
