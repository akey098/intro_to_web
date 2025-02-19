# Appending additional text to the existing file
with open("sample_text.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("Additional text has been appended to sample_text.txt")

# Reading the updated content
with open("sample_text.txt", "r") as file:
    updated_content = file.read()

print("Updated content of the file:")
print(updated_content)
