# ============================================
# Topic: Data Types
# Folder: 01_Basics
# Description: Built-in data types in Python.
# ============================================

# --------------------------------------------
# Numeric Types
# --------------------------------------------

integer = 100
floating = 95.75
complex_number = 2 + 5j

print(integer)
print(floating)
print(complex_number)

# --------------------------------------------
# String
# --------------------------------------------

name = "Python"

print(name)

# --------------------------------------------
# Boolean
# --------------------------------------------

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)

# --------------------------------------------
# List (Mutable)
# --------------------------------------------

fruits = ["Apple", "Banana", "Orange"]

print(fruits)

# Can be modified.

fruits.append("Mango")

print(fruits)

# --------------------------------------------
# Tuple (Immutable)
# --------------------------------------------

coordinates = (10, 20)

print(coordinates)

# coordinates[0] = 100
# TypeError

# --------------------------------------------
# Set
# --------------------------------------------

numbers = {1, 2, 3, 4, 5}

print(numbers)

# Duplicate values are removed.

duplicate = {1, 2, 2, 3, 3}

print(duplicate)

# --------------------------------------------
# Dictionary
# --------------------------------------------

student = {
    "name": "Yash",
    "age": 20,
    "cgpa": 9.2
}

print(student)

print(student["name"])

# --------------------------------------------
# None Type
# --------------------------------------------

data = None

print(data)

# Represents "no value".

# --------------------------------------------
# Finding Data Type
# --------------------------------------------

print(type(integer))
print(type(floating))
print(type(name))
print(type(is_logged_in))
print(type(fruits))
print(type(coordinates))
print(type(numbers))
print(type(student))
print(type(data))

# --------------------------------------------
# End of File
# --------------------------------------------