"""
==================================================
Python Journey - Control Flow
File: 12_pattern_printing.py
Topic: Pattern Printing
==================================================

Objective:
- Learn how to print different patterns using loops.
- Understand the relationship between rows and columns.
- Build logic for solving pattern-based problems.

Concepts Covered:
1. Star patterns
2. Number patterns
3. Right triangle
4. Inverted triangle
5. Pyramid
"""

# ==================================================
# What is Pattern Printing?
# ==================================================

# Pattern printing is the process of creating shapes
# using characters, numbers or symbols with loops.
#
# Most pattern problems use nested loops:
# - Outer loop -> controls rows
# - Inner loop -> controls columns


# ==================================================
# Pattern 1: Square
# ==================================================

print("Pattern 1: Square\n")

for row in range(5):
    for column in range(5):
        print("*", end=" ")
    print()

print()


# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *


# ==================================================
# Pattern 2: Right Triangle
# ==================================================

print("Pattern 2: Right Triangle\n")

for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()

print()


# Output:
# *
# * *
# * * *
# * * * *
# * * * * *


# ==================================================
# Pattern 3: Inverted Right Triangle
# ==================================================

print("Pattern 3: Inverted Right Triangle\n")

for row in range(5, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()

print()


# Output:
# * * * * *
# * * * *
# * * *
# * *
# *


# ==================================================
# Pattern 4: Number Triangle
# ==================================================

print("Pattern 4: Number Triangle\n")

for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()

print()


# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# ==================================================
# Pattern 5: Repeated Number Triangle
# ==================================================

print("Pattern 5: Repeated Number Triangle\n")

for row in range(1, 6):
    for column in range(row):
        print(row, end=" ")
    print()

print()


# Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


# ==================================================
# Pattern 6: Pyramid
# ==================================================

print("Pattern 6: Pyramid\n")

rows = 5

for row in range(rows):
    # Print spaces
    for space in range(rows - row - 1):
        print(" ", end="")

    # Print stars
    for star in range(2 * row + 1):
        print("*", end="")

    print()

print()


# Output:
#     *
#    ***
#   *****
#  *******
# *********


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Mixing up rows and columns.
#
# Wrong:
# Forgetting end=" " while printing.
#
# Wrong:
# Forgetting print() after each row.
#
# Tip:
# Think of every pattern one row at a time.


# ==================================================
# Summary
# ==================================================

# ✓ Outer loop controls rows.
# ✓ Inner loop controls columns.
# ✓ Use end="" or end=" " to print on the same line.
# ✓ Use print() to move to the next line.
# ✓ Pattern printing improves loop logic and problem-solving.