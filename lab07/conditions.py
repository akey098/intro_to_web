# 1. if Statement
age = 20
if age >= 18:
    print("You are an adult.")

# 2. else Statement
age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# 3. elif Statement
age = 20
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# 4. Nested if Statements
age = 22
has_ticket = True
if age >= 18:
    if has_ticket:
        print("You can enter the concert.")
    else:
        print("You need a ticket to enter.")
else:
    print("You are too young to enter.")

# 5. Conditional Expressions (Ternary Operator)
age = 16
can_drive = "You can drive." if age >= 18 else "You cannot drive."
print(can_drive)

# 6. Combining Conditions
age = 21
has_id = True
if age >= 18 and has_id:
    print("You can enter the concert.")
else:
    print("You cannot enter.")

# 7. Logical Operators
temperature = 30
is_raining = False

if temperature > 25 and not is_raining:
    print("It's a nice day for a walk.")
elif temperature <= 25 or is_raining:
    print("Better stay inside.")

