# ============================================
# Topic: User Input
# Folder: 01_Basics
# Description: Taking input from the user.
# ============================================

# --------------------------------------------
# Basic Input
# --------------------------------------------

# input() always returns data as a string.

name = input("Enter your name: ")

print("Hello,", name)

# --------------------------------------------
# Input with Type Conversion
# --------------------------------------------

# Convert input into an integer.

age = int(input("Enter your age: "))

print("Age:", age)

# Convert input into a float.

cgpa = float(input("Enter your CGPA: "))

print("CGPA:", cgpa)

# --------------------------------------------
# Multiple Inputs
# --------------------------------------------

first_name = input("First Name: ")
last_name = input("Last Name: ")

print(first_name, last_name)

# --------------------------------------------
# Taking Multiple Values in One Line
# --------------------------------------------

# User Input:
# 10 20

a, b = map(int, input("Enter two numbers: ").split())

print(a)
print(b)

# --------------------------------------------
# String Concatenation
# --------------------------------------------

city = input("Enter your city: ")

print("You live in " + city)

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# Wrong
# age = input("Age: ")
# print(age + 5)
# TypeError

# Correct
age = int(input("Enter age: "))
print(age + 5)

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Always convert numeric input using int() or float().
# ✔ Use meaningful prompts.
# ✔ Validate user input when required.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# • input() returns a string.
# • Use int() for integers.
# • Use float() for decimal numbers.
# • split() separates values.
# • map() converts multiple values.

# --------------------------------------------
# End of File
# --------------------------------------------