# ============================================
# Topic: String Methods
# Folder: 01_Basics
# Description: Frequently used string methods.
# ============================================

text = "python programming"

# --------------------------------------------
# Case Conversion
# --------------------------------------------

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# --------------------------------------------
# Removing Spaces
# --------------------------------------------

name = "   Python   "

print(name.strip())
print(name.lstrip())
print(name.rstrip())

# --------------------------------------------
# Searching
# --------------------------------------------

print(text.find("program"))
print(text.index("python"))

print(text.startswith("python"))
print(text.endswith("ming"))

# --------------------------------------------
# Counting
# --------------------------------------------

print(text.count("m"))

# --------------------------------------------
# Replacing
# --------------------------------------------

print(text.replace("python", "Java"))

# --------------------------------------------
# Splitting
# --------------------------------------------

sentence = "Python Java C++"

words = sentence.split()

print(words)

# --------------------------------------------
# Joining
# --------------------------------------------

languages = ["Python", "Java", "C++"]

print(", ".join(languages))

# --------------------------------------------
# Checking Methods
# --------------------------------------------

print("python".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("HELLO".isupper())
print("hello".islower())
print("Python".istitle())
print("   ".isspace())

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# Strings are immutable.

text = "python"

# Wrong
# text.upper()
# print(text)

# Correct
text = text.upper()

print(text)

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Store the returned value if you want changes.
# ✔ Read the documentation for available methods.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# upper()
# lower()
# title()
# strip()
# split()
# join()
# replace()
# find()
# count()

# --------------------------------------------
# End of File
# --------------------------------------------