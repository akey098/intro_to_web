import json

# Data to store
student = {
    "name": "Liza",
    "age": 19 ,
    "courses": ["Math", "Science", "History"]
}

# Write JSON data to a file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data has been written to student.json")
