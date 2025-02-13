#1
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)
print(5 % 3)
print(5 ** 3)

#2
print(5 == 5)
print(5 == 3)
print(5 != 5)
print(5 != 3)
print(5 > 3)
print(5 > 6)
print(5 < 3)
print(5 < 6)
print(5 >= 3)
print(5 >= 6)
print(5 <= 3)
print(5 <= 6)


#3
# AND operator
print(5 > 3 and 5 < 3)

# OR operator
print(5 > 3 or 5 < 3)

# NOT operator
print(not 5 < 3)

#4
print(5 & 3)
print(5 | 3)
print(5 ^ 3)
print(~5)

#5
x = 5
print(x)
x += 1
print(x)
x -= 1
print(x)
x *= 2
print(x)
x /= 2
print(x)

#6
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)       # True, because x and y are pointing to same memory location
print(x is z)       # False, even numbers are same, x and z are have two different memory location

a = [1, 2, 3]
b = [1, 2, 3]
print(x is not y)

fruits = ["apple", "orange", "strawberry", "banana"]
print("banana" in fruits)
print("banana" not in fruits)

vegetables = ["potatoes", "tomatoes", "cabbage"]
print("potatoes" in vegetables)
print("tomatoes" in fruits)