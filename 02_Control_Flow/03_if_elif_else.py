"""
=========================================================
File: 03_if_elif_else.py
Topic: if-elif-else Statement
Folder: 02_Control_Flow
=========================================================

Description:
------------
The 'if-elif-else' statement is used when there are multiple
conditions to check. Python checks each condition from top
to bottom. As soon as one condition becomes True, its block
executes and the remaining conditions are skipped.

Syntax:
-------
if condition1:
    # Code Block

elif condition2:
    # Code Block

elif condition3:
    # Code Block

else:
    # Executes if none of the above conditions are True
"""

# =========================================================
# Example 1: Basic if-elif-else
# =========================================================

marks = 82

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 35:
    print("Grade C")

else:
    print("Fail")

# Output:
# Grade A


# =========================================================
# Example 2: User Input
# =========================================================

age = int(input("Enter your age: "))

if age < 13:
    print("Child")

elif age < 18:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")

# Try:
# Input: 16
# Output: Teenager


# =========================================================
# Example 3: Traffic Signal
# =========================================================

signal = "yellow"

if signal == "red":
    print("Stop")

elif signal == "yellow":
    print("Get Ready")

elif signal == "green":
    print("Go")

else:
    print("Invalid Signal")

# Output:
# Get Ready


# =========================================================
# Example 4: Temperature Check
# =========================================================

temperature = 34

if temperature >= 40:
    print("Very Hot")

elif temperature >= 30:
    print("Hot")

elif temperature >= 20:
    print("Pleasant")

elif temperature >= 10:
    print("Cold")

else:
    print("Very Cold")

# Output:
# Hot


# =========================================================
# Example 5: Calculator Operation
# =========================================================

operation = "+"

if operation == "+":
    print("Addition Selected")

elif operation == "-":
    print("Subtraction Selected")

elif operation == "*":
    print("Multiplication Selected")

elif operation == "/":
    print("Division Selected")

else:
    print("Invalid Operation")

# Output:
# Addition Selected


# =========================================================
# Example 6: Login Role
# =========================================================

role = "admin"

if role == "admin":
    print("Full Access")

elif role == "manager":
    print("Limited Access")

elif role == "user":
    print("Basic Access")

else:
    print("Guest Access")

# Output:
# Full Access


# =========================================================
# Example 7: Month Number
# =========================================================

month = 4

if month == 1:
    print("January")

elif month == 2:
    print("February")

elif month == 3:
    print("March")

elif month == 4:
    print("April")

else:
    print("Month Not Listed")

# Output:
# April


# =========================================================
# Example 8: Electricity Bill Category
# =========================================================

units = 275

if units <= 100:
    print("Low Usage")

elif units <= 200:
    print("Medium Usage")

elif units <= 300:
    print("High Usage")

else:
    print("Very High Usage")

# Output:
# High Usage


# =========================================================
# Example 9: Percentage Division
# =========================================================

percentage = 67

if percentage >= 75:
    print("Distinction")

elif percentage >= 60:
    print("First Class")

elif percentage >= 50:
    print("Second Class")

elif percentage >= 35:
    print("Pass")

else:
    print("Fail")

# Output:
# First Class


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Wrong Order of Conditions
#
# marks = 95
#
# if marks >= 35:
#     print("Pass")
# elif marks >= 90:
#     print("A+")
#
# Since 95 >= 35 is already True,
# Python never reaches the second condition.


# ❌ Multiple else Blocks
#
# if condition:
#     pass
# else:
#     pass
# else:
#     pass


# ❌ Using elif without if
#
# elif condition:
#     print("Hello")


# ❌ Forgetting Colon
#
# elif marks >= 60


# =========================================================
# Best Practices
# =========================================================

# ✔ Arrange conditions from most specific to least specific.

# ✔ Keep conditions readable.

# ✔ Avoid unnecessary elif statements.

# ✔ Use meaningful variable names.

# ✔ Add comments when logic becomes complex.


# =========================================================
# Quick Revision
# =========================================================

# -> if is checked first.
#
# -> elif means "else if".
#
# -> Python checks conditions from top to bottom.
#
# -> Only the first True block executes.
#
# -> Remaining conditions are skipped.
#
# -> else executes only when all conditions are False.
#
# Flow:
#
# if
#   ↓
# elif
#   ↓
# elif
#   ↓
# else