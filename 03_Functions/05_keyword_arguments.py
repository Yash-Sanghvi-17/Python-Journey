"""
==================================================
Python Journey - Functions
File: 05_keyword_arguments.py
Topic: Keyword Arguments
==================================================

Objective:
- Understand what keyword arguments are.
- Learn how they improve code readability.
- Compare positional and keyword arguments.

Concepts Covered:
1. Keyword arguments
2. Positional vs keyword arguments
3. Mixing positional and keyword arguments
4. Rules for keyword arguments
"""

# ==================================================
# What are Keyword Arguments?
# ==================================================

# Keyword arguments are arguments passed using
# the parameter name.
#
# Instead of relying on position, Python matches
# the value with the parameter name.
#
# Syntax:
#
# function(parameter=value)


# ==================================================
# Example 1: Basic Keyword Arguments
# ==================================================

def student(name, age, course):
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")


student(name="Yash", age=20, course="Python")

print()


# ==================================================
# Example 2: Changing the Order
# ==================================================

# Since parameter names are used, the order
# of arguments does not matter.

student(course="Python", name="Yash", age=20)

print()


# ==================================================
# Example 3: Positional Arguments
# ==================================================

student("Virat", 36, "Cricket")

print()


# ==================================================
# Example 4: Mixing Positional and Keyword Arguments
# ==================================================

# Positional arguments must always come first.

student("Alice", age=21, course="AI")

print()


# ==================================================
# Example 5: Using Keyword Arguments with Defaults
# ==================================================

def greet(name, message="Welcome!"):
    print(f"{message} {name}")


greet("Yash")
greet("Rahul", message="Good Morning!")

print()


# ==================================================
# Positional vs Keyword Arguments
# ==================================================

# Positional Arguments
# --------------------
# - Order matters.
# - Faster to write.
#
# Keyword Arguments
# -----------------
# - Order does not matter.
# - More readable.
# - Easier to understand.


# ==================================================
# Rules for Keyword Arguments
# ==================================================

# ✔ Positional arguments come before keyword arguments.
#
# Correct:
#
# student("Yash", age=20, course="Python")
#
# Wrong:
#
# student(name="Yash", 20, "Python")
#
# This causes a SyntaxError.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Using the same parameter more than once.
#
# Example:
#
# student("Yash", name="Rahul", age=20)
#
# Error:
# TypeError
#
# Because 'name' receives two values.


# ==================================================
# Best Practices
# ==================================================

# ✓ Use keyword arguments when functions
#   have many parameters.
#
# ✓ Use descriptive parameter names.
#
# ✓ Prefer keyword arguments for optional values.
#
# ✓ Use positional arguments for short,
#   simple function calls.


# ==================================================
# Summary
# ==================================================

# ✓ Keyword arguments use parameter names.
# ✓ Order does not matter for keyword arguments.
# ✓ Positional arguments must come first.
# ✓ Keyword arguments improve readability.