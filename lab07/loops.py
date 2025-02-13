# 1. for Loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() with for Loop
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Custom Ranges
for i in range(2, 10, 2):  # Start at 2, end before 10, step by 2
    print(i)  # Output: 2, 4, 6, 8

# 2. while Loop
count = 0
while count < 5:
    print(count)
    count += 1  # Output: 0, 1, 2, 3, 4

# 3. break Statement
for num in range(10):
    if num == 5:
        break
    print(num)  # Output: 0, 1, 2, 3, 4

# 4. continue Statement
for num in range(5):
    if num == 2:
        continue
    print(num)  # Output: 0, 1, 3, 4 (skips 2)

# 5. else Clause with Loops
for i in range(3):
    print(i)
else:
    print("Loop finished normally.")  # Executes when loop ends normally

# else does NOT execute if loop breaks
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not be printed.")

# 6. Nested Loops
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 7. Infinite Loops (use with caution)
while True:
     print("This will run forever. Stop manually!")

