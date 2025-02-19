with open("sample_text.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines of text for testing file operations.\n")

print("Content has been written to sample_text.txt")

# Reading from the text file
with open("sample_text.txt", "r") as file:
    content = file.read()

print("Content read from the file:")
print(content)


