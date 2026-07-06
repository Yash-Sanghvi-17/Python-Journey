"""
=========================================================
File: 02_if_else.py
Topic: if-else Statement
Folder: 02_Control_Flow
=========================================================

Description:
------------
The 'if-else' statement is used when there are two possible
outcomes. If the condition is True, the 'if' block executes.
Otherwise, the 'else' block executes.

Syntax:
-------
if condition:
    # Code if condition is True
else:
    # Code if condition is False
"""

# =========================================================
# Example 1: Basic if-else Statement
# =========================================================

age = 16

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Output:
# You are not eligible to vote.


# =========================================================
# Example 2: User Input
# =========================================================

marks = int(input("Enter your marks: "))

if marks >= 35:
    print("Congratulations! You passed.")
else:
    print("Sorry! You failed.")

# Try:
# Input: 50
# Output: Congratulations! You passed.
#
# Input: 20
# Output: Sorry! You failed.


# =========================================================
# Example 3: Even or Odd Number
# =========================================================

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Output:
# Odd Number


# =========================================================
# Example 4: Positive or Negative
# =========================================================

num = -10

if num >= 0:
    print("Positive Number")
else:
    print("Negative Number")

# Output:
# Negative Number


# =========================================================
# Example 5: Password Check
# =========================================================

password = input("Enter password: ")

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# Try:
# Input: python123
# Output: Access Granted


# =========================================================
# Example 6: Boolean Variable
# =========================================================

is_logged_in = False

if is_logged_in:
    print("Welcome Back!")
else:
    print("Please log in.")

# Output:
# Please log in.


# =========================================================
# Example 7: Number Comparison
# =========================================================

a = 25
b = 15

if a > b:
    print("a is greater than b.")
else:
    print("a is not greater than b.")

# Output:
# a is greater than b.


# =========================================================
# Example 8: Divisibility Check
# =========================================================

number = 15

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not Divisible by 5")

# Output:
# Divisible by 5


# =========================================================
# Example 9: Shopping Discount
# =========================================================

bill_amount = 750

if bill_amount >= 1000:
    print("Discount Applied!")
else:
    print("No Discount Available.")

# Output:
# No Discount Available.


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Forgetting the colon
#
# if age >= 18
#     print("Adult")
# else
#     print("Minor")


# ❌ Wrong indentation
#
# if age >= 18:
# print("Adult")
# else:
#     print("Minor")


# ❌ Using '=' instead of '=='
#
# if age = 18:
#     print("Adult")


# ❌ else cannot have a condition
#
# else age < 18:
#     print("Minor")


# =========================================================
# Best Practices
# =========================================================

# ✔ Use if-else when there are exactly two possible outcomes.

# ✔ Keep conditions simple and easy to understand.

# ✔ Use meaningful variable names.

# ✔ Maintain proper indentation.

# ✔ Avoid deeply nested if-else statements when possible.


# =========================================================
# Quick Revision
# =========================================================

# -> if checks a condition.
#
# -> else executes when the if condition is False.
#
# -> Exactly one block (if or else) executes.
#
# -> else does not have a condition.
#
# -> Both blocks must have proper indentation.
#
# -> Common comparison operators:
#    ==
#    !=
#    >
#    <
#    >=
#    <=