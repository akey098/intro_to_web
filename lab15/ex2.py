import csv

# Writing data to a CSV file
data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

with open("people.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data has been written to people.csv")

# Reading data from a CSV file
with open("people.csv", "r") as file:
    reader = csv.reader(file)
    print("Reading data from the CSV file:")
    for row in reader:
        print(row)