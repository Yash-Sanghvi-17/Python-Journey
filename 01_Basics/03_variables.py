# ============================================
# Topic: Variables
# Folder: 01_Basics
# Description: Variables store data in memory.
# ============================================

# --------------------------------------------
# Creating Variables
# --------------------------------------------

name = "Yash"
age = 20
cgpa = 9.15
is_student = True

print(name)
print(age)
print(cgpa)
print(is_student)

# --------------------------------------------
# Dynamic Typing
# --------------------------------------------

# Python automatically determines the data type.

x = 100
print(x)

x = "Python"
print(x)

# --------------------------------------------
# Multiple Assignment
# --------------------------------------------

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Same value to multiple variables.

x = y = z = 50

print(x)
print(y)
print(z)

# --------------------------------------------
# Variable Naming Rules
# --------------------------------------------

student_name = "John"
marks = 95
_price = 100

# Valid
userAge = 21
user_age = 21

# Invalid Examples

# 2name = "Yash"      # Starts with a number
# my-name = "Yash"    # Hyphen not allowed
# class = "Python"    # Keyword cannot be used

# --------------------------------------------
# Case Sensitive
# --------------------------------------------

name = "Yash"
Name = "Python"

print(name)
print(Name)

# These are two different variables.

# --------------------------------------------
# Swapping Variables
# --------------------------------------------

a = 10
b = 20

print(a, b)

a, b = b, a

print(a, b)

# No temporary variable required.

# --------------------------------------------
# Deleting Variables
# --------------------------------------------

temp = 100

print(temp)

del temp

# print(temp)      # NameError

# --------------------------------------------
# Best Practices
# --------------------------------------------

# Use meaningful variable names.

student_name = "Rahul"
total_marks = 480

# Avoid

# a = "Rahul"
# x = 480

# --------------------------------------------
# End of File
# --------------------------------------------