# ============================================
# Topic: Operators
# Folder: 01_Basics
# Description: Different operators used in Python.
# ============================================

a = 10
b = 3

# --------------------------------------------
# Arithmetic Operators
# --------------------------------------------

print(a + b)     # Addition
print(a - b)     # Subtraction
print(a * b)     # Multiplication
print(a / b)     # Float Division
print(a // b)    # Floor Division
print(a % b)     # Modulus (Remainder)
print(a ** b)    # Exponentiation

# --------------------------------------------
# Comparison Operators
# --------------------------------------------

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# --------------------------------------------
# Logical Operators
# --------------------------------------------

print(a > 5 and b > 1)
print(a > 5 or b > 10)
print(not(a > b))

# --------------------------------------------
# Assignment Operators
# --------------------------------------------

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 2
print(x)

x //= 2
print(x)

x %= 3
print(x)

x **= 2
print(x)

# --------------------------------------------
# Identity Operators
# --------------------------------------------

list1 = [1, 2]
list2 = list1
list3 = [1, 2]

print(list1 is list2)
print(list1 is list3)

print(list1 is not list3)

# --------------------------------------------
# Membership Operators
# --------------------------------------------

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

print("Orange" not in fruits)

# --------------------------------------------
# Bitwise Operators
# --------------------------------------------

print(5 & 3)     # AND
print(5 | 3)     # OR
print(5 ^ 3)     # XOR
print(~5)        # NOT
print(5 << 1)    # Left Shift
print(5 >> 1)    # Right Shift

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# =  Assignment
# == Comparison

# Wrong
# if a = b:

# Correct
# if a == b:

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Use parentheses for complex expressions.
# ✔ Use 'is' only for object identity.
# ✔ Use '==' for value comparison.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# Arithmetic
# Comparison
# Logical
# Assignment
# Identity
# Membership
# Bitwise

# --------------------------------------------
# End of File
# --------------------------------------------