"""
==================================================
Python Journey - Functions
File: 08_lambda_functions.py
Topic: Lambda Functions
==================================================

Objective:
- Understand what lambda functions are.
- Learn when to use lambda functions.
- Compare lambda functions with normal functions.
- Use lambda with common built-in functions.

Concepts Covered:
1. Lambda Functions
2. Lambda vs Normal Functions
3. map()
4. filter()
5. sorted()
"""

# ==================================================
# What is a Lambda Function?
# ==================================================

# A lambda function is a small anonymous function.
#
# Anonymous means it has no name.
#
# Lambda functions are generally used for short,
# simple operations that are needed only once.
#
# Syntax:
#
# lambda parameters: expression
#
# Example:
#
# square = lambda x: x * x


# ==================================================
# Example 1: Normal Function vs Lambda Function
# ==================================================

# Normal Function

def square(number):
    return number * number


print("Normal Function:", square(5))

# Lambda Function

square_lambda = lambda number: number * number

print("Lambda Function:", square_lambda(5))

print()


# ==================================================
# Example 2: Multiple Parameters
# ==================================================

add = lambda a, b: a + b

print("Sum:", add(10, 20))

print()


# ==================================================
# Example 3: Using lambda with map()
# ==================================================

# map() applies a function to every element
# in an iterable.

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("Original:", numbers)
print("Squares :", squares)

print()


# ==================================================
# Example 4: Using lambda with filter()
# ==================================================

# filter() keeps only the elements for which
# the function returns True.

numbers = [10, 15, 20, 25, 30]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)

print()


# ==================================================
# Example 5: Using lambda with sorted()
# ==================================================

students = [
    ("Rahul", 82),
    ("Alice", 95),
    ("Bob", 76),
    ("Yash", 90)
]

# Sort by marks (second element of each tuple)

sorted_students = sorted(students, key=lambda student: student[1])

print("Sorted by Marks:")

for student in sorted_students:
    print(student)

print()


# ==================================================
# Normal Function vs Lambda Function
# ==================================================

# Normal Function
# --------------------------
# Uses the def keyword.
# Can contain multiple statements.
# Suitable for large tasks.
#
# Lambda Function
# --------------------------
# Uses the lambda keyword.
# Contains only one expression.
# Best for short, simple tasks.


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# Trying to write multiple statements
# inside a lambda function.
#
# Lambda functions can contain only
# a single expression.


# Wrong:
#
# Using lambda for complex logic.
#
# In such cases, use a normal function.


# ==================================================
# Best Practices
# ==================================================

# ✓ Use lambda for small, simple operations.
# ✓ Use normal functions for larger logic.
# ✓ Keep lambda expressions short and readable.
# ✓ Use lambda with functions like map(),
#   filter() and sorted() when appropriate.


# ==================================================
# Summary
# ==================================================

# ✓ Lambda functions are anonymous functions.
# ✓ They are created using the lambda keyword.
# ✓ They contain only one expression.
# ✓ They are commonly used with map(),
#   filter() and sorted().
# ✓ Use normal functions for complex tasks.