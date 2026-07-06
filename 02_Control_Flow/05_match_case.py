"""
=========================================================
File: 05_match_case.py
Topic: match-case Statement
Folder: 02_Control_Flow
=========================================================

Description:
------------
The match-case statement is used to compare one value against
multiple possible cases. It provides a cleaner alternative
to long if-elif-else chains when checking a single variable.

Introduced in:
--------------
Python 3.10+

Syntax:
-------
match variable:
    case value1:
        # Code Block

    case value2:
        # Code Block

    case _:
        # Default Block
"""

# =========================================================
# Example 1: Basic match-case
# =========================================================

day = 3

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case _:
        print("Invalid Day")

# Output:
# Wednesday


# =========================================================
# Example 2: User Input
# =========================================================

choice = int(input("Enter a number (1-3): "))

match choice:
    case 1:
        print("You selected One")

    case 2:
        print("You selected Two")

    case 3:
        print("You selected Three")

    case _:
        print("Invalid Choice")


# =========================================================
# Example 3: Calculator Menu
# =========================================================

operation = "+"

match operation:
    case "+":
        print("Addition")

    case "-":
        print("Subtraction")

    case "*":
        print("Multiplication")

    case "/":
        print("Division")

    case _:
        print("Invalid Operation")

# Output:
# Addition


# =========================================================
# Example 4: Traffic Signal
# =========================================================

signal = "green"

match signal:
    case "red":
        print("Stop")

    case "yellow":
        print("Get Ready")

    case "green":
        print("Go")

    case _:
        print("Unknown Signal")

# Output:
# Go


# =========================================================
# Example 5: Month Name
# =========================================================

month = 5

match month:
    case 1:
        print("January")

    case 2:
        print("February")

    case 3:
        print("March")

    case 4:
        print("April")

    case 5:
        print("May")

    case _:
        print("Invalid Month")

# Output:
# May


# =========================================================
# Example 6: Multiple Values in One Case
# =========================================================

day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")

    case _:
        print("Invalid Day")

# Output:
# Weekend


# =========================================================
# Example 7: Simple Grade Checker
# =========================================================

grade = "A"

match grade:
    case "A":
        print("Excellent")

    case "B":
        print("Good")

    case "C":
        print("Average")

    case "D":
        print("Needs Improvement")

    case _:
        print("Invalid Grade")

# Output:
# Excellent


# =========================================================
# Example 8: Boolean Values
# =========================================================

is_logged_in = True

match is_logged_in:
    case True:
        print("Welcome!")

    case False:
        print("Please Login")

# Output:
# Welcome!


# =========================================================
# Example 9: Default Case
# =========================================================

language = "Python"

match language:
    case "Java":
        print("Java Selected")

    case "C++":
        print("C++ Selected")

    case _:
        print("Language Not Available")

# Output:
# Language Not Available


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Forgetting the colon
#
# match day
#     case 1:


# ❌ Forgetting the default case
#
# Although optional, using case _ is recommended.


# ❌ Using match in Python versions below 3.10
#
# It will result in a SyntaxError.


# ❌ Incorrect indentation
#
# match value:
# case 1:
#     print("Hello")


# =========================================================
# Best Practices
# =========================================================

# ✔ Use match-case when checking one variable
# against many possible values.

# ✔ Always include case _ as the default case.

# ✔ Keep each case simple and readable.

# ✔ Use if-elif-else when conditions involve
# ranges (>, <, >=, <=) or multiple variables.


# =========================================================
# Quick Revision
# =========================================================

# -> match-case is similar to switch-case.

# -> Introduced in Python 3.10.

# -> match checks one variable.

# -> case defines each possible value.

# -> case _ acts like the default case.

# -> Use | to combine multiple values.

# -> Better readability than long if-elif-else
# when comparing a single variable.


# =========================================================
# Comparison: if-elif-else vs match-case
# =========================================================

# if-elif-else
# -------------
# ✔ Supports ranges
# ✔ Supports complex conditions
# ✔ Supports multiple variables

# match-case
# ----------
# ✔ Cleaner for fixed values
# ✔ Easier to read
# ✔ Better for menus and commands


# =========================================================
# Mini Challenge
# =========================================================

# Create a simple menu-driven calculator.

# Menu:
# 1 -> Addition
# 2 -> Subtraction
# 3 -> Multiplication
# 4 -> Division

# Use match-case to print the selected operation.