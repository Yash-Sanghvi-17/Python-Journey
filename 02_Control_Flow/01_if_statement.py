"""
=========================================================
File: 01_if_statement.py
Topic: if Statement
Folder: 02_Control_Flow
=========================================================

Description:
------------
The 'if' statement is used to make decisions in a program.
It executes a block of code only when a given condition is True.

Syntax:
-------
if condition:
    # Code to execute if condition is True
"""

# =========================================================
# Example 1: Basic if Statement
# =========================================================

age = 20

if age >= 18:
    print("You are eligible to vote.")

# Output:
# You are eligible to vote.


# =========================================================
# Example 2: Condition is False
# =========================================================

temperature = 25

if temperature < 20:
    print("It's cold outside.")

# No output because the condition is False.


# =========================================================
# Example 3: User Input
# =========================================================

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Congratulations! You passed.")

# Try:
# Input: 50
# Output: Congratulations! You passed.


# =========================================================
# Example 4: Checking Equality
# =========================================================

password = "python123"

if password == "python123":
    print("Access Granted")

# Output:
# Access Granted


# =========================================================
# Example 5: Using Multiple Conditions
# =========================================================

number = 12

if number > 0:
    print("Positive Number")

if number % 2 == 0:
    print("Even Number")

# Output:
# Positive Number
# Even Number


# =========================================================
# Example 6: Boolean Variable
# =========================================================

is_logged_in = True

if is_logged_in:
    print("Welcome!")

# Output:
# Welcome!


# =========================================================
# Example 7: String Comparison
# =========================================================

name = "Byte"

if name == "Byte":
    print("Hello, Byte!")

# Output:
# Hello, Byte!


# =========================================================
# Example 8: Nested Operations Inside if
# =========================================================

num = 16

if num > 10:
    square = num ** 2
    print("Square:", square)

# Output:
# Square: 256


# =========================================================
# Example 9: Multiple Statements
# =========================================================

salary = 50000

if salary >= 30000:
    print("Salary Approved")
    print("You can apply for the loan.")
    print("Verification Complete.")

# Output:
# Salary Approved
# You can apply for the loan.
# Verification Complete.


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Missing Colon
#
# if age >= 18
#     print("Adult")


# ❌ Wrong Indentation
#
# if age >= 18:
# print("Adult")


# ❌ Using = Instead of ==
#
# if age = 18:
#     print("Adult")


# =========================================================
# Best Practices
# =========================================================

# ✔ Keep conditions simple and readable.

# ✔ Use meaningful variable names.

# ✔ Maintain proper indentation (4 spaces).

# ✔ Write only the required code inside an if block.

# ✔ Use comments where necessary to improve readability.


# =========================================================
# Quick Revision
# =========================================================

# -> if is used for decision making.
#
# -> Code runs ONLY when the condition is True.
#
# -> A colon (:) is mandatory after the condition.
#
# -> Indentation defines the block of code.
#
# -> Multiple independent if statements can exist together.
#
# -> Comparison operators commonly used:
#    ==   Equal to
#    !=   Not equal to
#    >    Greater than
#    <    Less than
#    >=   Greater than or equal to
#    <=   Less than or equal to
#
# -> Conditions evaluate to either True or False.