# Define a function

def greet():
    print("Welcome to Python Programming!")

greet()

# Function parameters

def greet_user1(name):
    print(f"Hello, {name}! How are you?")

greet_user1("John")

# Default Parameters

def greet_user2(name="Guest"):
    print(f"Hello, {name}!")

greet_user2()
greet_user2("Alice")

# Returning values

def add(a, b):
    return a + b

result = add(5, 10)
print(f"The sum is {result}")

# Multiple return values

def rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = rectangle_properties(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")

# Variable-Length Arguments

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))

# Lambda functions

square = lambda x: x * x
print(square(4))

# Scope of Variables

def local_scope():
    x = 10
    print(x)

local_scope()

x = 5
def modify_global():
    global x
    x += 10

modify_global()
print(x)

# Recursion

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Docstrings

def multiply(a, b):
    """This function multiplies two numbers"""
    return a * b

print(multiply.__doc__)