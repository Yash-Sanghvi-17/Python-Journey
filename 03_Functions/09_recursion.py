"""
==================================================
Python Journey - Functions
File: 09_recursion.py
Topic: Recursion
==================================================

Objective:
- Understand what recursion is.
- Learn the importance of the base case.
- Compare recursion with loops.
- Solve simple problems using recursion.

Concepts Covered:
1. Recursive Functions
2. Base Case
3. Recursive Case
4. Recursion vs Iteration
"""

# ==================================================
# What is Recursion?
# ==================================================

# Recursion is a programming technique where
# a function calls itself to solve a problem.
#
# Every recursive function must have:
#
# 1. Base Case
#    - Stops the recursion.
#
# 2. Recursive Case
#    - Calls the function again.
#
# Without a base case, recursion continues
# indefinitely and results in an error.


# ==================================================
# Example 1: Basic Recursion
# ==================================================

def countdown(number):
    if number == 0:          # Base Case
        print("Done!")
        return

    print(number)
    countdown(number - 1)    # Recursive Call


countdown(5)

print()


# ==================================================
# Example 2: Factorial
# ==================================================

def factorial(number):

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("5! =", factorial(5))

print()


# ==================================================
# Example 3: Sum of Numbers
# ==================================================

def find_sum(number):

    if number == 1:
        return 1

    return number + find_sum(number - 1)


print("Sum =", find_sum(5))

print()


# ==================================================
# Example 4: Fibonacci Series
# ==================================================

def fibonacci(number):

    if number <= 1:
        return number

    return fibonacci(number - 1) + fibonacci(number - 2)


print("First 8 Fibonacci Numbers:")

for i in range(8):
    print(fibonacci(i), end=" ")

print("\n")


# ==================================================
# Example 5: Recursion vs Loop
# ==================================================

# Recursive Version

def recursive_count(number):

    if number == 0:
        return

    print(number)
    recursive_count(number - 1)


recursive_count(3)

print()

# Loop Version

for number in range(3, 0, -1):
    print(number)

print()


# ==================================================
# Recursion vs Iteration
# ==================================================

# Recursion
# --------------------------
# Function calls itself.
# Elegant for some problems.
# Uses more memory.
#
# Iteration
# --------------------------
# Uses loops.
# Usually faster.
# Uses less memory.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# def example():
#     example()
#
# Error:
# RecursionError
#
# Because there is no base case.


# Wrong:
# Forgetting to make progress toward
# the base case.


# ==================================================
# Best Practices
# ==================================================

# ✓ Always define a base case.
# ✓ Ensure each recursive call moves
#   closer to the base case.
# ✓ Use recursion for naturally recursive
#   problems like trees and file systems.
# ✓ Prefer loops for simple repetitive tasks.


# ==================================================
# Summary
# ==================================================

# ✓ Recursion means a function calls itself.
# ✓ Every recursive function needs a base case.
# ✓ The recursive case reduces the problem size.
# ✓ Missing the base case causes a RecursionError.
# ✓ Some problems are easier to solve recursively.