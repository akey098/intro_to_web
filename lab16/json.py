import json

# 1. Convert a Python Dictionary to a JSON String (Serialization)
student = {
    "name": "Alice",
    "age": 21,
    "courses": ["Math", "Science", "History"]
}

json_string = json.dumps(student, indent=4)
print("Serialized JSON string:")
print(json_string)

# 2. Convert a JSON String Back to a Python Object (Deserialization)
json_data = '{"name": "Alice", "age": 21, "courses": ["Math", "Science", "History"]}'
student_dict = json.loads(json_data)
print("\nDeserialized Python object:")
print(student_dict)

# 3. Writing JSON to a File
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
print("\nData has been written to student.json")

# 4. Reading JSON from a File
with open("student.json", "r") as file:
    loaded_data = json.load(file)
print("\nData loaded from the JSON file:")
print(loaded_data)

# 5. Handling Lists in JSON
students_list = [
    {"name": "Alice", "age": 21},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 23}
]

json_list_string = json.dumps(students_list, indent=4)
print("\nJSON string for a list of students:")
print(json_list_string)

# 6. Writing a List of Dictionaries to a JSON File
with open("students.json", "w") as file:
    json.dump(students_list, file, indent=4)
print("\nList of students has been written to students.json")

# 7. Reading a List of Dictionaries from a JSON File
with open("students.json", "r") as file:
    loaded_students = json.load(file)
print("\nData loaded from students.json:")
print(loaded_students)

# 8. Handling Invalid JSON with Error Handling
invalid_json = '{"name": "Alice", "age": 21, "courses": ["Math", "Science", "History" }'  # Missing closing bracket

try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("\nError decoding JSON:", e)
