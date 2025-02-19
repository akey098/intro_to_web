import re

# Example 1: Finding Phone Numbers
text = "Call me at 555-1234 or 555-5678. My office number is 555-9999."
phone_numbers = re.findall(r"\b\d{3}-\d{4}\b", text)
print("Phone Numbers Found:", phone_numbers)

# Example 2: Matching at the Start of a String
text1 = "Hello, welcome to Python!"
text2 = "Welcome, Hello there!"
if re.match(r"^Hello", text1):
    print("Match found in text1: Hello")
else:
    print("No match found in text1.")

if re.match(r"^Hello", text2):
    print("Match found in text2: Hello")
else:
    print("No match found in text2.")

if re.search(r"Hello", text2):
    print("Found in text2 using re.search(): Hello")

# Example 3: Replacing Numbers with a Word
text = "There are 5 apples, 12 oranges, and 9 bananas in the basket."
modified_text = re.sub(r"\d+", "NUMBER", text)
print("Modified Text:", modified_text)

# Example 4: Extracting Email Addresses
text = "Please contact support@example.com or sales@example.org for assistance."
emails = re.findall(r"\b\w+@\w+\.\w+\b", text)
print("Email Addresses Found:", emails)

# Example 5: Finding Words that Start with a Vowel
text = "An apple a day keeps the doctor away. Even elephants enjoy eating."
vowel_words = re.findall(r"\b[aeiouAEIOU]\w*\b", text, re.IGNORECASE)
print("Words starting with a vowel:", vowel_words)
