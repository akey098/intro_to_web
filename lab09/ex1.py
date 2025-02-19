# Custom Exception for Negative Index
class NegativeIndexError(Exception):
    def __init__(self, msg="Index cannot be negative!"):
        super().__init__(msg)


# Handling List Indexing with Custom Error
try:
    numbers = [4,8,10]
    index = int(input("Enter an index to retrieve a number: "))

    if index < 0:
        raise NegativeIndexError()
    print(numbers[index])

except NegativeIndexError as err:
    print(f"Error: {err}")
except ValueError:
    print("Invalid input! Please enter an integer.")
except IndexError:
    print(f"Index {index} is out of range.")

print()

# Type Error Handling
try:
    result = "60" + 11
    print(result)
except TypeError:
    print("You can't add a string and an integer.")

print()

# Key Error Handling
try:
    sample_dict = {"a": 3, "b": 2, "c": 13}
    print(sample_dict["x"])
except KeyError:
    print("Key not found in dictionary!")
