"""
==================================================
Python Journey - Control Flow
File: 11_nested_loops.py
Topic: Nested Loops
==================================================

Objective:
- Understand what nested loops are.
- Learn how inner and outer loops work together.
- Practice printing simple patterns using nested loops.

Concepts Covered:
1. Nested for loops
2. Nested while loops
3. Loop execution order
4. Pattern generation
"""

# ==================================================
# What are Nested Loops?
# ==================================================

# A nested loop is a loop inside another loop.
#
# The outer loop executes once, then the inner loop
# completes all its iterations.
#
# This repeats until the outer loop finishes.

# Syntax:
#
# for i in range(...):
#     for j in range(...):
#         # Code


# ==================================================
# Example 1: Basic Nested for Loop
# ==================================================

print("Example 1")

for row in range(1, 4):
    for column in range(1, 4):
        print(f"({row}, {column})", end=" ")
    print()

print()


# ==================================================
# Example 2: Multiplication Table (1 to 3)
# ==================================================

print("Example 2")

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()


# ==================================================
# Example 3: Nested while Loop
# ==================================================

print("Example 3")

row = 1

while row <= 3:
    column = 1

    while column <= 3:
        print(f"Row {row}, Column {column}")
        column += 1

    row += 1

print()


# ==================================================
# Example 4: Printing a Rectangle
# ==================================================

print("Example 4")

for row in range(4):
    for column in range(5):
        print("*", end=" ")
    print()

print()


# ==================================================
# Example 5: Number Grid
# ==================================================

print("Example 5")

for row in range(1, 4):
    for column in range(1, 4):
        print(column, end=" ")
    print()

print()


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Forgetting to reset the inner loop variable
# in nested while loops.
#
# Wrong:
# Mixing up the row and column variables.


# ==================================================
# Summary
# ==================================================

# ✓ A nested loop is a loop inside another loop.
# ✓ The inner loop completes all iterations
#   for each outer loop iteration.
# ✓ Useful for tables, matrices and patterns.
# ✓ Commonly used in problem solving.