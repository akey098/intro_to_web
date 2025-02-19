# Part 2:
print("Hello, world!")

# Part 3:

# 1. Variable Assignment
name = "John Doe"
age = 25
pi = 3.14159

# 2. Dynamic Typing
x = 10
x = "Now I'm a string"

# 3. Printing Variables
print("My name is", name, "and I am", age, "years old.")

# 4. Multiple Assignments
a, b, c = 10, 20, 30
print(a, b, c)

# 5. Swapping Variables Without a Temporary Variable
a, b = b, a
print("Swapped values: a =", a, ", b =", b)

# 6. Constants (by convention, uppercase names)
PI = 3.14159
radius = 5
area = PI * radius**2
print("Area of the circle:", area)


# Part 4:

# 1. Basic Input
user_name = input("Enter your name: ")
print("Hello,", user_name)

# 2. Type Conversion with Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

# 3. Multiple Inputs
num1, num2, num3 = map(int, input("Enter three numbers separated by space: ").split())
print(f"Sum: {num1 + num2 + num3}, Average: {(num1 + num2 + num3) / 3}, Product: {num1 * num2 * num3}")

# 4. Output Formatting
print(f"Hello {user_name}, you entered numbers {num1}, {num2}, and {num3}.")

# 5. Specifying sep and end in print()
print("Hello", "world", sep="-", end="!\n")


# Part 5: Comments in Python

# Single-line comment
# This prints a message to the console
print("This is a Python script.")  # Inline comment

"""
Multi-line comment
This script demonstrates basic Python syntax, including:
- Variables
- Input/Output
- Comments
"""

def greet(name):
    """This function prints a greeting message."""
    print(f"Hello, {name}!")

greet("Alice")

