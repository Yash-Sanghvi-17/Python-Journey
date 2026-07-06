"""
=========================================================
File: 09_range_function.py
Topic: range() Function
Folder: 02_Control_Flow
=========================================================

Description:
------------
The range() function generates a sequence of numbers.

It is commonly used with for loops when you want to repeat
a block of code a specific number of times.

Note:
-----
The ending value is NOT included in the sequence.

Syntax:
-------
range(stop)

range(start, stop)

range(start, stop, step)
"""

# =========================================================
# Example 1: range(stop)
# =========================================================

for number in range(5):
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4


# =========================================================
# Example 2: range(start, stop)
# =========================================================

for number in range(1, 6):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# =========================================================
# Example 3: range(start, stop, step)
# =========================================================

for number in range(2, 11, 2):
    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10


# =========================================================
# Example 4: Reverse Counting
# =========================================================

for number in range(10, 0, -1):
    print(number)

# Output:
# 10
# 9
# 8
# ...
# 1


# =========================================================
# Example 5: Skipping Numbers
# =========================================================

for number in range(0, 21, 5):
    print(number)

# Output:
# 0
# 5
# 10
# 15
# 20


# =========================================================
# Example 6: Multiplication Table
# =========================================================

table = 7

for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")

# Output:
# 7 x 1 = 7
# ...
# 7 x 10 = 70


# =========================================================
# Example 7: Sum of Numbers
# =========================================================

total = 0

for number in range(1, 101):
    total += number

print("Sum =", total)

# Output:
# Sum = 5050


# =========================================================
# Example 8: Convert range to List
# =========================================================

numbers = list(range(1, 6))

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# =========================================================
# Example 9: Using len() with range()
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

for index in range(len(fruits)):
    print(index, fruits[index])

# Output:
# 0 Apple
# 1 Banana
# 2 Mango


# =========================================================
# Example 10: Empty range
# =========================================================

for number in range(5, 1):
    print(number)

# Output:
# No Output

# Since the start value is greater than the stop value
# and no negative step is provided.


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Expecting the stop value to be included
#
# range(1, 5)
#
# Output:
# 1 2 3 4


# ❌ Forgetting a negative step while counting backwards
#
# range(5, 1)
#
# Produces an empty sequence.


# ❌ Using step = 0
#
# range(1, 10, 0)
#
# Error:
# ValueError


# =========================================================
# Best Practices
# =========================================================

# ✔ Use range(stop) when counting from 0.

# ✔ Use range(start, stop) when a custom start
# value is needed.

# ✔ Use a step value for skipping numbers.

# ✔ Prefer iterating directly over collections
# unless the index is required.


# =========================================================
# Quick Revision
# =========================================================

# range(stop)
# ----------------
# Starts from 0.
#
# Example:
# range(5)
# -> 0 1 2 3 4


# range(start, stop)
# ------------------
# Starts from start.
#
# Example:
# range(3, 7)
# -> 3 4 5 6


# range(start, stop, step)
# ------------------------
# Moves by the given step.
#
# Example:
# range(2, 11, 2)
# -> 2 4 6 8 10


# Remember:
#
# ✔ Stop value is NOT included.
#
# ✔ Positive step -> Forward.
#
# ✔ Negative step -> Backward.


# =========================================================
# Did You Know?
# =========================================================

# 💡 range() does not create all numbers at once.
# It generates them efficiently as needed.

# 💡 range() can be converted into a list, tuple,
# or other collections if required.

# 💡 Most counting-based algorithms use range().


# =========================================================
# Mini Challenge
# =========================================================

# 1. Print numbers from 50 to 100.

# 2. Print odd numbers from 1 to 25.

# 3. Print numbers from 20 to 0.

# 4. Print multiples of 7 below 100.

# 5. Create a list containing numbers from
# 100 to 110 using range().