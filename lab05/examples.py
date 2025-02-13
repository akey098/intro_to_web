#1
print("Hello World")

#2
x = 5
y = "X is not a y"
price = 19.99
print(x, "and", y, "so", price)

price = "20.99"
print(x, "and", y, "so", price)

d = "5.0"
print(type(d))

#3
x, y = input("Enter your first and last name: ").split()
a = int(input("Enter your age: "))
print("Hello, I am ", x, y, "and", a, "years old, next year I'll be", a + 1)

c, d = input("Enter two numbers: ").split()
c, d = int(c), int(d)
print("Sum of",c, "and", d, "is", c + d)

#4
"""
    The below code demonstrates us how the value of variables can be changed.
    Variables once assigned are allowed to change when it is necessary.
"""
X = 5   # The variable X is assigned as 5 initially
print(X)

X = 15  # The variable X is changed to 15
print(X)