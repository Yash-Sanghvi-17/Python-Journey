"""
==================================================
Python Journey - Functions
File: 10_docstrings.py
Topic: Docstrings
==================================================

Objective:
- Understand what docstrings are.
- Learn how to document functions.
- Access docstrings using the __doc__ attribute.
- Follow Python documentation best practices.

Concepts Covered:
1. Docstrings
2. Single-line Docstrings
3. Multi-line Docstrings
4. Accessing Docstrings
"""

# ==================================================
# What is a Docstring?
# ==================================================

# A docstring (documentation string) is a string
# placed immediately below the definition of a
# function, class or module.
#
# It explains:
# - What the function does
# - What parameters it accepts
# - What it returns
#
# Python stores docstrings, allowing them to be
# viewed later using the __doc__ attribute.


# ==================================================
# Example 1: Single-Line Docstring
# ==================================================

def greet():
    """Display a welcome message."""
    print("Hello, Python!")


greet()

print()


# ==================================================
# Example 2: Viewing a Docstring
# ==================================================

print(greet.__doc__)

print()


# ==================================================
# Example 3: Multi-Line Docstring
# ==================================================

def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of the two numbers.
    """
    return a + b


result = add(10, 20)

print("Result:", result)

print()


# ==================================================
# Example 4: Another Function with a Docstring
# ==================================================

def square(number):
    """
    Return the square of a number.
    """
    return number ** 2


print(square(5))
print(square.__doc__)

print()


# ==================================================
# Example 5: Module Docstring
# ==================================================

# The large comment at the top of this file
# (inside triple quotes) is a module docstring.
#
# It describes the purpose of the entire module.


# ==================================================
# Why Use Docstrings?
# ==================================================

# Docstrings help:
#
# ✓ Explain what code does.
# ✓ Improve readability.
# ✓ Help other developers understand your code.
# ✓ Generate automatic documentation.
# ✓ Make maintenance easier.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# def add(a, b):
#     # Adds numbers
#     return a + b
#
# Better:
#
# def add(a, b):
#     """Return the sum of two numbers."""
#     return a + b


# Wrong:
# Writing very long or unclear docstrings.
#
# Keep them short, clear and meaningful.


# ==================================================
# Best Practices
# ==================================================

# ✓ Write a docstring for every important function.
# ✓ Start with a short summary sentence.
# ✓ Describe parameters and return values
#   for larger functions.
# ✓ Keep documentation updated when code changes.


# ==================================================
# Summary
# ==================================================

# ✓ A docstring documents code.
# ✓ It is written using triple quotes.
# ✓ It can be viewed using __doc__.
# ✓ Good documentation makes code easier to use.
# ✓ Docstrings are a standard Python practice.