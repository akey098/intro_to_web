#list
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.insert(1, 15)
numbers.remove(30)
numbers.reverse()
numbers.sort()
print(numbers[:3])
print(numbers[-2:])
print(numbers[::-1])

#dictionary
student = {"name": "Alice", "age": 22, "grade": "A"}
student["subject"] = "Math"
student["grade"] = "A+"
del student["age"]
print(student.keys())
print(student.values())

#set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#tuple
colors = ("red", "blue", "green", "red", "yellow")
print(colors.index("green"))
print(colors.count("red"))

#nested list and dict
company = {
    "employees": [
        {"name": "Alice", "position": "Developer", "salary": 60000},
        {"name": "Bob", "position": "Designer", "salary": 55000}
    ]
}
company["employees"].append({"name": "Charlie", "position": "Manager", "salary": 70000})
for employee in company["employees"]:
    print(employee["name"])
