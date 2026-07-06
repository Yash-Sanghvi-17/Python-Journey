"""
=========================================================
File: 06_for_loop.py
Topic: for Loop
Folder: 02_Control_Flow
=========================================================

Description:
------------
A for loop is used to iterate (repeat) over a sequence like
a string, list, tuple, set, dictionary, or range().

It is useful when the number of iterations is known or when
you want to visit each item in a collection.

Syntax:
-------
for variable in sequence:
    # Code Block
"""

# =========================================================
# Example 1: Basic for Loop
# =========================================================

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# =========================================================
# Example 2: Starting and Ending Values
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
# Example 3: Using Step Value
# =========================================================

for even in range(2, 11, 2):
    print(even)

# Output:
# 2
# 4
# 6
# 8
# 10


# =========================================================
# Example 4: Reverse Counting
# =========================================================

for num in range(10, 0, -1):
    print(num)

# Output:
# 10
# 9
# 8
# ...
# 1


# =========================================================
# Example 5: Iterating Through a String
# =========================================================

name = "Python"

for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n


# =========================================================
# Example 6: Iterating Through a List
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango


# =========================================================
# Example 7: Calculating Sum
# =========================================================

total = 0

for number in range(1, 6):
    total += number

print("Sum =", total)

# Output:
# Sum = 15


# =========================================================
# Example 8: Multiplication Table
# =========================================================

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Output:
# 5 x 1 = 5
# ...
# 5 x 10 = 50


# =========================================================
# Example 9: Counting Characters
# =========================================================

text = "Hello"

count = 0

for character in text:
    count += 1

print("Characters:", count)

# Output:
# Characters: 5


# =========================================================
# Example 10: Iterating Through a Tuple
# =========================================================

colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)

# Output:
# Red
# Green
# Blue


# =========================================================
# Example 11: Iterating Through a Set
# =========================================================

numbers = {10, 20, 30}

for value in numbers:
    print(value)

# Note:
# Sets are unordered, so output order may vary.


# =========================================================
# Example 12: Iterating Through a Dictionary
# =========================================================

student = {
    "Name": "Alice",
    "Age": 20,
    "Grade": "A"
}

for key in student:
    print(key, ":", student[key])

# Output:
# Name : Alice
# Age : 20
# Grade : A


# =========================================================
# Example 13: Nested for Preview
# =========================================================

for row in range(3):
    for column in range(2):
        print(row, column)

# Output:
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Forgetting the colon
#
# for i in range(5)
#     print(i)


# ❌ Wrong indentation
#
# for i in range(5):
# print(i)


# ❌ Modifying the loop variable
#
# for i in range(5):
#     i = 100
#
# This does not affect the loop.


# ❌ Forgetting that range() excludes the end value
#
# range(1, 5)
#
# Output:
# 1 2 3 4


# =========================================================
# Best Practices
# =========================================================

# ✔ Use meaningful variable names.

# ✔ Use range() when repeating a fixed number of times.

# ✔ Iterate directly over collections whenever possible.

# ✔ Keep loop bodies small and readable.

# ✔ Avoid unnecessary nested loops.


# =========================================================
# Quick Revision
# =========================================================

# -> for loops repeat code.

# -> They iterate over sequences.

# -> range() is commonly used with for loops.

# -> The end value in range() is NOT included.

# -> Step controls the increment/decrement.

# -> for loops can iterate over:
#    • Strings
#    • Lists
#    • Tuples
#    • Sets
#    • Dictionaries
#    • range()


# =========================================================
# Mini Challenge
# =========================================================

# 1. Print numbers from 1 to 20.

# 2. Print all even numbers between 1 and 50.

# 3. Print each character of your name.

# 4. Print the multiplication table of any number.

# 5. Find the sum of numbers from 1 to 100.