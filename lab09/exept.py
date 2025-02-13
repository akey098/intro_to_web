# 1. Example Without Exception Handling

# num = int(input("Enter a number: "))  # May raise ValueError
# result = 10 / num  # May raise ZeroDivisionError
# print(result)

# 2. Common Built-in Exceptions
try:
    x = 10 / 0  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    num = int("abc")  # Raises ValueError
except ValueError:
    print("Error: Invalid input, please enter a number.")

my_list = [1, 2, 3]
try:
    print(my_list[5])  # Raises IndexError
except IndexError:
    print("Error: Index out of range.")

my_dict = {"name": "Alice"}
try:
    print(my_dict["age"])  # Raises KeyError
except KeyError:
    print("Error: Key not found in dictionary.")

# 3. Exception Handling Using try and except
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# 4. Handling Multiple Exceptions
try:
    a, b = 5, 0
    print(a / b)  # ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero.")
except TypeError:
    print("Invalid type for division.")

# Catching multiple exceptions in one block
try:
    val = int("abc")
except (ValueError, TypeError):
    print("Invalid operation!")

# 5. Using else in Exception Handling
try:
    num = int(input("Enter a valid number: "))
except ValueError:
    print("That was not a valid number!")
else:
    print(f"Success! You entered {num}")

# 6. Using finally
try:
    file = open("example.txt", "r")  # FileNotFoundError
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This always runs, closing resources if needed.")

# 7. Raising Exceptions
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance!")
    return balance - amount

try:
    print(withdraw(100, 200))
except ValueError as e:
    print(f"Error: {e}")

# 8. Custom Exceptions
class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError("Cannot compute square root of a negative number.")
    return n ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")

# 9. Debugging in Python
# Using print statements for debugging
def debug_example():
    x = 5
    y = 0
    print("Before division")  # Debugging print
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("After division")

debug_example()

# Using Assertions
def check_positive(n):
    assert n > 0, "Number must be positive"
    return n

try:
    print(check_positive(-3))
except AssertionError as e:
    print(f"Assertion Error: {e}")
