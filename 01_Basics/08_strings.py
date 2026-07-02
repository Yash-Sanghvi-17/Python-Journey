# ============================================
# Topic: Strings
# Folder: 01_Basics
# Description: Working with strings in Python.
# ============================================

# --------------------------------------------
# Creating Strings
# --------------------------------------------

name = "Python"
language = 'Programming'

paragraph = """Python is
easy to
learn."""

print(name)
print(language)
print(paragraph)

# --------------------------------------------
# String Indexing
# --------------------------------------------

text = "Python"

print(text[0])
print(text[1])
print(text[-1])

# --------------------------------------------
# String Slicing
# --------------------------------------------

print(text[0:2])
print(text[2:6])
print(text[:4])
print(text[3:])
print(text[::-1])

# --------------------------------------------
# String Length
# --------------------------------------------

print(len(text))

# --------------------------------------------
# String Concatenation
# --------------------------------------------

first = "Hello"
second = "World"

print(first + " " + second)

# --------------------------------------------
# String Repetition
# --------------------------------------------

print("Hi! " * 3)

# --------------------------------------------
# Checking Characters
# --------------------------------------------

print("P" in text)
print("Z" not in text)

# --------------------------------------------
# Strings are Immutable
# --------------------------------------------

# text[0] = "J"
# TypeError

# Correct

new_text = "J" + text[1:]

print(new_text)

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Prefer double quotes for consistency.
# ✔ Use triple quotes for multi-line strings.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# • Ordered
# • Immutable
# • Supports indexing
# • Supports slicing

# --------------------------------------------
# End of File
# --------------------------------------------