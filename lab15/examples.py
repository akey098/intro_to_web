# File Handling Examples in Python

# 1. Writing to a File
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.\nPython makes file handling easy.")
print("File written successfully.")

# 2. Reading from a File
with open("example.txt", "r") as file:
    content = file.read()
print("File Content:\n", content)

# 3. Reading a File Line by Line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# 4. Appending Data to a File
with open("example.txt", "a") as file:
    file.write("\nAppending new data to the file.")
print("Data appended successfully.")

# 5. Checking if a File Exists Before Writing
import os

filename = "new_file.txt"
if not os.path.exists(filename):
    with open(filename, "x") as file:
        file.write("This is a newly created file.")
    print("File created successfully.")
else:
    print("File already exists.")

# CSV Handling Examples
import csv

# 6. Writing to a CSV File
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 22, "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file written successfully.")

# 7. Reading a CSV File
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 8. Reading a CSV File as Dictionaries
with open("people.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}.")

# 9. Appending Data to a CSV File
new_data = [
    ["David", 28, "Houston"],
    ["Eve", 35, "Miami"]
]

with open("people.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)

print("Data appended to CSV file successfully.")
