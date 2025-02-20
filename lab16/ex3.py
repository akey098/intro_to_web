import json

# Define a Python dictionary
student = {
    "name": "Liza",
    "age": 19,
    "courses": ["Math", "Science", "History"]
}

# Write the dictionary to a JSON file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data has been written to student.json")

# Read the JSON data back from the file
with open("student.json", "r") as file:
    loaded_data = json.load(file)

# Print the loaded data
print("Data loaded from the JSON file:")
print(loaded_data)
