"""
==================================================
Python Journey - Functions
File: 03_return_statement.py
Topic: Return Statement
==================================================

Objective:
- Understand the purpose of the return statement.
- Learn the difference between print() and return.
- Return single and multiple values from functions.

Concepts Covered:
1. return statement
2. Returning a value
3. Returning multiple values
4. print() vs return
"""

# ==================================================
# What is the Return Statement?
# ==================================================

# The return statement is used to send a value
# back from a function.
#
# Once Python executes the return statement,
# the function immediately stops executing.
#
# Syntax:
#
# def function_name():
#     return value


# ==================================================
# Example 1: Returning a Value
# ==================================================

def square(number):
    return number ** 2


result = square(5)

print("Square:", result)

print()


# ==================================================
# Example 2: Using the Returned Value
# ==================================================

def add(a, b):
    return a + b


sum_result = add(10, 20)

print("Sum:", sum_result)
print("Double of Sum:", sum_result * 2)

print()


# ==================================================
# Example 3: Returning Multiple Values
# ==================================================

def student():
    name = "Yash"
    age = 20
    return name, age


student_name, student_age = student()

print("Name:", student_name)
print("Age :", student_age)

print()


# ==================================================
# Example 4: return Ends the Function
# ==================================================

def message():
    print("Before return")
    return
    print("After return")  # This line never executes.


message()

print()


# ==================================================
# Example 5: print() vs return
# ==================================================

def multiply(a, b):
    return a * b


result = multiply(4, 5)

print("Result:", result)

print()


# ==================================================
# print() vs return
# ==================================================

# print()
# -------------------------
# Displays output.
# Does not send a value back.
#
# return
# -------------------------
# Sends a value back to the caller.
# Allows the value to be stored,
# reused or further processed.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# def add(a, b):
#     print(a + b)
#
# result = add(5, 3)
#
# print(result)
#
# Output:
# 8
# None
#
# Why?
# Because print() displays the value,
# but the function returns nothing.


# ==================================================
# Best Practices
# ==================================================

# ✓ Use return when a value needs to be reused.
# ✓ Use print() only for displaying output.
# ✓ Keep return statements simple and meaningful.
# ✓ Return only the data needed.


# ==================================================
# Summary
# ==================================================

# ✓ return sends a value back from a function.
# ✓ A function stops executing after return.
# ✓ Multiple values can be returned.
# ✓ print() displays data, while return sends data back.
# ✓ return makes functions reusable and flexible.