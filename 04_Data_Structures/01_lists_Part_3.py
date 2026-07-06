# ==================================================
# Packing and Unpacking
# ==================================================

# Packing means storing multiple values together.

numbers = [10, 20, 30, 40]

print(numbers)

print()


# Unpacking means assigning elements
# to multiple variables.

a, b, c, d = numbers

print(a)
print(b)
print(c)
print(d)

print()


# Using * for Multiple Values

numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First :", first)
print("Middle:", middle)
print("Last  :", last)

print()


# ==================================================
# Nested Lists
# ==================================================

# A nested list is a list inside another list.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

print()

print(matrix[0])

print(matrix[1])

print(matrix[2])

print()

print(matrix[1][2])

print()


# Traversing Nested Lists

for row in matrix:

    for value in row:

        print(value, end=" ")

    print()

print()


# ==================================================
# Copying Lists
# ==================================================

# Assignment copies the reference,
# NOT the actual list.

list1 = [10, 20, 30]

list2 = list1

list2[0] = 100

print(list1)

print(list2)

print()


# Proper Copy

list3 = list1.copy()

list3[1] = 999

print(list1)

print(list3)

print()


# ==================================================
# Common Errors
# ==================================================

# 1. IndexError

# numbers = [10,20,30]
# print(numbers[5])

# Because index 5 doesn't exist.


# 2. TypeError

# numbers = [10,20,30]
# print(numbers["1"])

# Index must be an integer.


# 3. ValueError

# numbers = [10,20,30]
# numbers.remove(100)

# Value doesn't exist.


# ==================================================
# Best Practices
# ==================================================

# ✓ Store similar types together.

# ✓ Use meaningful variable names.

# ✓ Use enumerate() while looping.

# ✓ Prefer append() over + when adding one item.

# ✓ Use copy() when creating another list.

# ✓ Avoid modifying a list while iterating over it.

# ✓ Keep nested lists readable.

# ✓ Choose the right data structure for the task.


# ==================================================
# Performance Notes
# ==================================================

# Lists are implemented as dynamic arrays.

# Advantages
#
# ✓ Fast indexing
# ✓ Dynamic resizing
# ✓ Easy traversal

# Disadvantages
#
# ✗ Slow insertion in the middle
# ✗ Slow deletion in the middle
# ✗ Search is linear


# ==================================================
# Time Complexity
# ==================================================

# Operation                 Complexity
# ------------------------------------
# Index Access                 O(1)
# Update                       O(1)
# Append                       O(1) Average
# Insert Beginning             O(n)
# Insert Middle                O(n)
# Delete End                   O(1)
# Delete Middle                O(n)
# Search                       O(n)
# Traversal                    O(n)
# Copy                         O(n)
# Reverse (reversed())         O(n)
# Sort                         O(n log n)


# ==================================================
# Interview Notes
# ==================================================

# Q1.
# Why are lists mutable?

# Because their elements can be changed
# after creation.


# Q2.
# Difference between List and Tuple?

# List
# ----
# Mutable
# Uses []
#
# Tuple
# -----
# Immutable
# Uses ()


# Q3.
# Difference between append() and extend()?

# append()
#
# Adds one object.
#
# extend()
#
# Adds multiple elements.
#
# Covered in next file.


# Q4.
# Difference between sort() and sorted()?

# sorted()
#
# Returns a NEW list.
#
# sort()
#
# Modifies original list.


# ==================================================
# Mini Project
# ==================================================

shopping_cart = []

shopping_cart.append("Laptop")

shopping_cart.append("Mouse")

shopping_cart.append("Keyboard")

print("Shopping Cart")

for item in shopping_cart:

    print("-", item)

print()

print("Total Items:", len(shopping_cart))

print()


# ==================================================
# Quick Revision
# ==================================================

# Lists
#
# ✓ Ordered
# ✓ Mutable
# ✓ Dynamic
# ✓ Allows Duplicates
# ✓ Supports Indexing
# ✓ Supports Slicing
# ✓ Supports Nesting


# ==================================================
# Cheat Sheet
# ==================================================

# Create
#
# numbers = [1,2,3]

# Access
#
# numbers[0]

# Update
#
# numbers[0] = 100

# Slice
#
# numbers[1:4]

# Reverse
#
# numbers[::-1]

# Length
#
# len(numbers)

# Maximum
#
# max(numbers)

# Minimum
#
# min(numbers)

# Sum
#
# sum(numbers)

# Loop
#
# for item in numbers:

# Enumerate
#
# enumerate(numbers)

# Combine
#
# zip(list1, list2)


# ==================================================
# Summary
# ==================================================

# ✓ Lists are ordered collections.
# ✓ Lists are mutable.
# ✓ Lists support indexing and slicing.
# ✓ Lists can store any data type.
# ✓ Lists support many useful built-in functions.
# ✓ Lists are one of Python's most important
#   data structures.
# ✓ Understanding lists makes learning
#   tuples, sets and dictionaries easier.