# Numeric Types
num_items = 10
temperature = -5
price = 99.99
distance = 1.5e3
complex_num = 3 + 4j

# Sequence Types
greeting = "Hello, World!"
name = 'Alice'
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
coordinates = (10, 20, 30)

# Mapping Type
person = {"name": "John", "age": 25, "city": "New York"}
person["age"] = 26

# Set Types
numbers = {1, 2, 3, 4, 4, 5}
numbers.add(6)
numbers.remove(2)
frozen_numbers = frozenset([1, 2, 3, 4])

# Boolean Type
is_sunny = True
is_raining = False

# Binary Types
byte_data = bytes([65, 66, 67])
byte_array = bytearray([72, 101, 108, 108, 111])
byte_array[0] = 77

# Type Conversion
num_str = "42"
num_int = int(num_str)
num_float = float(num_int)
num_str = str(num_int)
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
list_data = [4, 5, 6]
tuple_data = tuple(list_data)
list_data = [1, 2, 2, 3, 4, 4]
set_data = set(list_data)
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_data = dict(pairs)

# Output
print(type(num_items), type(price), type(complex_num))
print(type(greeting), type(fruits), type(coordinates))
print(person)
print(numbers, frozen_numbers)
print(is_sunny, is_raining)
print(byte_data, byte_array)
print(num_int, num_float, num_str)
print(list_data, tuple_data, set_data)
print(dict_data)

