#1 Variable types
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")
print(type(a))
print(type(b))
print(type(c))

#2 Data conversion
a = "1000"
b = int(a)
c = float(b)
print("Text data: ", a)
print("Integer data: ", b)
print("Float data: ", c)

dict = {"name": "Theo", "age": 35, "job": "Doctor"}
print(dict["name"])
print(dict["age"])
print(dict["job"])

#3 Operations on sets
s = {0, 6, 11}
s.add(11)
s.remove(0)
print(11 in s)