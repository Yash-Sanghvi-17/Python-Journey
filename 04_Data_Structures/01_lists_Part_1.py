"""
==================================================
Python Journey - Data Structures
File: 01_lists.py
Topic: Lists
==================================================

Objective:
- Understand what lists are.
- Learn how to create, access and modify lists.
- Learn indexing, slicing and traversal.
- Perform common list operations.
- Build a strong foundation before learning list methods.

Prerequisites:
- Variables
- Data Types
- Operators
- Loops
- Functions

Concepts Covered:
1. Introduction to Lists
2. Features of Lists
3. Creating Lists
4. Accessing Elements
5. Indexing
6. Negative Indexing
7. Updating Elements
8. List Operators
9. Slicing
10. Traversing Lists
"""

# ==================================================
# What is a List?
# ==================================================

# A list is an ordered, mutable (changeable)
# collection of items.
#
# Lists are one of Python's most commonly used
# built-in data structures.
#
# Lists can store:
# - Integers
# - Floats
# - Strings
# - Booleans
# - Objects
# - Other Lists
#
# Lists are created using square brackets [].


# ==================================================
# Why Use Lists?
# ==================================================

# Imagine storing marks of 100 students.
#
# Without a list:
#
# mark1 = 95
# mark2 = 87
# mark3 = 76
# ...
#
# This becomes difficult to manage.
#
# With a list:
#
# marks = [95, 87, 76, ...]
#
# Everything is stored together.


# ==================================================
# Features of Lists
# ==================================================

# ✓ Ordered
# ✓ Mutable (Changeable)
# ✓ Dynamic Size
# ✓ Allows Duplicate Values
# ✓ Supports Indexing
# ✓ Supports Slicing
# ✓ Can Store Multiple Data Types


# ==================================================
# Real-World Applications
# ==================================================

# Lists are widely used in:
#
# ✓ Shopping carts
# ✓ Student records
# ✓ Employee databases
# ✓ AI datasets
# ✓ Cybersecurity password lists
# ✓ Sensor readings
# ✓ Expense trackers
# ✓ Game leaderboards


# ==================================================
# Syntax
# ==================================================

# list_name = [item1, item2, item3]


# ==================================================
# Example 1 : Creating Lists
# ==================================================

numbers = [10, 20, 30, 40, 50]

fruits = ["Apple", "Banana", "Mango"]

mixed = [100, "Python", 3.14, True]

empty_list = []

print(numbers)
print(fruits)
print(mixed)
print(empty_list)

print()


# ==================================================
# Example 2 : Accessing Elements
# ==================================================

languages = ["Python", "Java", "C++", "JavaScript"]

print("First Element :", languages[0])
print("Second Element:", languages[1])
print("Third Element :", languages[2])

print()


# ==================================================
# Understanding Indexing
# ==================================================

# Positive Index
#
#        0       1        2        3
#      +-------+--------+--------+-------------+
#      |Python | Java   | C++    | JavaScript  |
#      +-------+--------+--------+-------------+


# ==================================================
# Example 3 : Negative Indexing
# ==================================================

# Negative indexing starts from the end.
#
# -1 -> Last Element
# -2 -> Second Last
# -3 -> Third Last

print("Last Element       :", languages[-1])
print("Second Last Element:", languages[-2])
print("Third Last Element :", languages[-3])

print()


# ==================================================
# Example 4 : Updating Elements
# ==================================================

marks = [75, 82, 91]

print("Before:", marks)

marks[1] = 90

print("After :", marks)

print()


# ==================================================
# Example 5 : Adding New Values
# ==================================================

# (Using + operator)
#
# Better methods will be covered
# in 02_list_methods.py

numbers = [10, 20, 30]

numbers = numbers + [40]

print(numbers)

print()


# ==================================================
# Example 6 : List Operators
# ==================================================

list1 = [1, 2, 3]

list2 = [4, 5, 6]

# Concatenation

print("Concatenation:")
print(list1 + list2)

print()

# Repetition

print("Repetition:")
print(list1 * 3)

print()

# Membership

print("Membership:")

print(2 in list1)

print(10 in list1)

print()

print("Not In:")

print(100 not in list1)

print()


# ==================================================
# List Slicing
# ==================================================

# Syntax:
#
# list[start : stop : step]
#
# start -> Inclusive
# stop  -> Exclusive


# ==================================================
# Example 7 : Basic Slicing
# ==================================================

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])

print(numbers[:3])

print(numbers[3:])

print(numbers[:])

print()


# ==================================================
# Example 8 : Negative Slicing
# ==================================================

print(numbers[-4:-1])

print(numbers[:-2])

print(numbers[-3:])

print()


# ==================================================
# Example 9 : Step Slicing
# ==================================================

print(numbers[::2])

print(numbers[1::2])

print(numbers[::-1])      # Reverse

print(numbers[::-2])

print()


# ==================================================
# Traversing a List
# ==================================================

# Traversing means visiting every element.


# ==================================================
# Method 1 : for Loop
# ==================================================

cities = ["Ahmedabad", "Mumbai", "Delhi"]

for city in cities:
    print(city)

print()


# ==================================================
# Method 2 : range()
# ==================================================

for index in range(len(cities)):
    print(index, cities[index])

print()


# ==================================================
# Method 3 : enumerate()
# ==================================================

for index, city in enumerate(cities):
    print(index, city)

print()


# ==================================================
# Method 4 : while Loop
# ==================================================

index = 0

while index < len(cities):
    print(cities[index])
    index += 1

print()


# ==================================================
# Mutable Nature of Lists
# ==================================================

# Lists are mutable.
#
# This means their contents can be changed
# after creation.

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

print()


# ==================================================
# Preview of List Methods
# ==================================================

# Lists provide many built-in methods.
#
# append()
# extend()
# insert()
# remove()
# pop()
# clear()
# index()
# count()
# sort()
# reverse()
# copy()
#
# They will be covered completely
# in the next file.
