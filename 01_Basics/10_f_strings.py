# ============================================
# Topic: f-Strings
# Folder: 01_Basics
# Description: Formatting strings using f-strings.
# ============================================

# --------------------------------------------
# Basic f-String
# --------------------------------------------

name = "Yash"

print(f"Hello, {name}")

# --------------------------------------------
# Multiple Variables
# --------------------------------------------

age = 20
cgpa = 9.15

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa}")

# --------------------------------------------
# Expressions
# --------------------------------------------

a = 10
b = 20

print(f"Sum = {a + b}")

# --------------------------------------------
# Formatting Numbers
# --------------------------------------------

pi = 3.1415926535

print(f"{pi:.2f}")

# Output:
# 3.14

# --------------------------------------------
# Alignment
# --------------------------------------------

text = "Python"

print(f"|{text:<10}|")   # Left
print(f"|{text:^10}|")   # Center
print(f"|{text:>10}|")   # Right

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# Wrong
# print("Hello {name}")

# Correct
print(f"Hello {name}")

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Prefer f-strings over string concatenation.
# ✔ f-strings are easier to read and maintain.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# f"..."
# {variable}
# {expression}
# :.2f

# --------------------------------------------
# End of File
# --------------------------------------------