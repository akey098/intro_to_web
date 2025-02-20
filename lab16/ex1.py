import json

# Python dictionary
student = {
    "name": "Liza",
    "age": 19,
    "courses": ["Math", "Science", "History"]
}

# Convert dictionary to JSON string
json_string = json.dumps(student, indent=4)
print(json_string)
