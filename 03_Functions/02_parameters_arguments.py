"""
==================================================
Python Journey - Functions
File: 02_parameters_arguments.py
Topic: Parameters and Arguments
==================================================

Objective:
- Understand the difference between parameters and arguments.
- Learn how data is passed into functions.
- Create functions that work with different values.

Concepts Covered:
1. Parameters
2. Arguments
3. Multiple parameters
4. Positional arguments
"""

# ==================================================
# What are Parameters and Arguments?
# ==================================================

# Parameter:
# A variable defined in the function definition.
#
# Argument:
# The actual value passed to the function when it is called.
#
# Example:
#
# def greet(name):    <-- name is a parameter
#     print(name)
#
# greet("Yash")       <-- "Yash" is an argument


# ==================================================
# Example 1: Single Parameter
# ==================================================

def greet(name):
    print(f"Hello, {name}!")


greet("Yash")

print()


# ==================================================
# Example 2: Multiple Parameters
# ==================================================

def student_info(name, age, course):
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Course : {course}")


student_info("Yash", 20, "Python")

print()


# ==================================================
# Example 3: Positional Arguments
# ==================================================

# Arguments are assigned based on their position.

def introduce(first_name, last_name):
    print(f"Full Name: {first_name} {last_name}")


introduce("Virat", "Kohli")

print()


# ==================================================
# Example 4: Passing Different Values
# ==================================================

def square(number):
    print(f"Square of {number} = {number ** 2}")


square(4)
square(7)
square(10)

print()


# ==================================================
# Example 5: Greeting Different Users
# ==================================================

def welcome(name):
    print(f"Welcome, {name}!")


welcome("Alice")
welcome("Bob")
welcome("Charlie")

print()


# ==================================================
# Parameters vs Arguments
# ==================================================

# Parameter                     Argument
# -----------------------------------------------
# Variable in function           Actual value
# Defined with def               Passed while calling
# Placeholder                    Real data


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Passing fewer arguments than required.
#
# def add(a, b):
#     print(a + b)
#
# add(5)
#
# Error:
# TypeError


# Wrong:
# Passing arguments in the wrong order.
#
# student_info(20, "Yash", "Python")


# ==================================================
# Best Practices
# ==================================================

# ✓ Use meaningful parameter names.
# ✓ Pass arguments in the correct order.
# ✓ Keep the number of parameters reasonable.
# ✓ Make function names descriptive.


# ==================================================
# Summary
# ==================================================

# ✓ Parameters receive data inside a function.
# ✓ Arguments are the values passed to a function.
# ✓ Positional arguments depend on order.
# ✓ Functions become flexible by accepting parameters.