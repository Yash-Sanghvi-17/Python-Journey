"""
==================================================
Python Journey - Functions
File: 01_function_basics.py
Topic: Function Basics
==================================================

Objective:
- Understand what functions are.
- Learn how to create and call functions.
- Understand why functions make code reusable.

Concepts Covered:
1. Defining a function
2. Calling a function
3. Function syntax
4. Code reusability
"""

# ==================================================
# What is a Function?
# ==================================================

# A function is a reusable block of code that performs
# a specific task.
#
# Instead of writing the same code multiple times,
# we can write it once inside a function and call it
# whenever needed.
#
# Think of a function like a machine:
#
# Input ---> Function ---> Output


# ==================================================
# Function Syntax
# ==================================================

# def function_name():
#     # Function body
#
# function_name()


# ==================================================
# Example 1: Creating Your First Function
# ==================================================

def greet():
    print("Hello!")
    print("Welcome to Python Journey.")


greet()

print()


# ==================================================
# Example 2: Calling a Function Multiple Times
# ==================================================

def welcome():
    print("Welcome to Python!")

welcome()
welcome()
welcome()

print()


# ==================================================
# Example 3: Function for a Specific Task
# ==================================================

def display_info():
    print("Name : Yash")
    print("Course : Python Journey")
    print("Language : Python")


display_info()

print()


# ==================================================
# Example 4: Function Doesn't Run Automatically
# ==================================================

def say_hi():
    print("Hi!")

# Nothing happens until the function is called.

say_hi()

print()


# ==================================================
# Example 5: Reusability
# ==================================================

def separator():
    print("-" * 30)


separator()
print("Chapter 1")

separator()
print("Chapter 2")

separator()

print()


# ==================================================
# Why Use Functions?
# ==================================================

# Functions help us:
#
# ✓ Avoid repeating code.
# ✓ Make programs easier to read.
# ✓ Divide large programs into smaller parts.
# ✓ Make debugging easier.
# ✓ Improve code organization.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Forgetting parentheses while calling a function.
#
# greet
#
# Correct:
#
# greet()


# Wrong:
# Calling a function before it is defined.
#
# Python reads code from top to bottom.


# ==================================================
# Best Practices
# ==================================================

# ✓ Give functions meaningful names.
# ✓ One function should perform one task.
# ✓ Keep functions short and readable.
# ✓ Use snake_case for function names.


# ==================================================
# Summary
# ==================================================

# ✓ A function is a reusable block of code.
# ✓ Functions are created using the 'def' keyword.
# ✓ A function runs only when it is called.
# ✓ Functions improve readability and reusability.
# ✓ Good function names make code easier to understand.