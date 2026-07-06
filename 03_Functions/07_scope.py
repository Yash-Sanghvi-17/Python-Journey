"""
==================================================
Python Journey - Functions
File: 07_scope.py
Topic: Variable Scope
==================================================

Objective:
- Understand variable scope in Python.
- Learn the difference between local and global variables.
- Use the global keyword correctly.

Concepts Covered:
1. Local Scope
2. Global Scope
3. global Keyword
4. Variable Lifetime
"""

# ==================================================
# What is Variable Scope?
# ==================================================

# Scope determines where a variable can be accessed.
#
# There are two main types:
#
# 1. Local Scope
#    - Variable exists only inside a function.
#
# 2. Global Scope
#    - Variable exists throughout the program.


# ==================================================
# Example 1: Local Variable
# ==================================================

def greet():
    message = "Hello, Python!"
    print(message)


greet()

# print(message)   # Error: message is local to greet()

print()


# ==================================================
# Example 2: Global Variable
# ==================================================

language = "Python"

def display_language():
    print("Language:", language)


display_language()
print("Language:", language)

print()


# ==================================================
# Example 3: Local and Global Variables Together
# ==================================================

name = "Global Name"

def show_name():
    name = "Local Name"
    print("Inside Function :", name)


show_name()
print("Outside Function:", name)

print()


# ==================================================
# Example 4: Using the global Keyword
# ==================================================

count = 0

def increase_count():
    global count
    count += 1
    print("Inside Function:", count)


increase_count()
increase_count()

print("Outside Function:", count)

print()


# ==================================================
# Example 5: Variable Lifetime
# ==================================================

def demo():
    number = 100
    print("Inside Function:", number)


demo()

# The variable 'number' is destroyed after
# the function finishes execution.

print()


# ==================================================
# Local vs Global Variables
# ==================================================

# Local Variable
# --------------------------
# Created inside a function.
# Accessible only inside that function.
# Destroyed when the function ends.
#
# Global Variable
# --------------------------
# Created outside all functions.
# Accessible throughout the program.
# Exists until the program ends.


# ==================================================
# LEGB Rule (Introduction)
# ==================================================

# Python searches for variables in this order:
#
# L -> Local
# E -> Enclosing
# G -> Global
# B -> Built-in
#
# For now, focus on Local and Global.
# You'll learn Enclosing Scope later with nested functions.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# def example():
#     value = 10
#
# print(value)
#
# Error:
# NameError
#
# Because 'value' only exists inside the function.


# Wrong:
#
# count = 0
#
# def update():
#     count += 1
#
# Error:
# UnboundLocalError
#
# Fix:
#
# global count


# ==================================================
# Best Practices
# ==================================================

# ✓ Prefer local variables whenever possible.
# ✓ Avoid modifying global variables frequently.
# ✓ Use meaningful variable names.
# ✓ Use the global keyword only when necessary.


# ==================================================
# Summary
# ==================================================

# ✓ Scope determines where variables can be accessed.
# ✓ Local variables exist only inside functions.
# ✓ Global variables can be accessed throughout the program.
# ✓ The global keyword allows modification of global variables.
# ✓ Prefer local variables for cleaner and safer code.