# ==================================================
# reverse()
# ==================================================

# Purpose:
# Reverses the ORIGINAL list.
#
# Unlike reversed(), reverse() modifies
# the original list.


# Syntax:
#
# list.reverse()


# Parameters:
#
# None


# Return Value:
#
# None


# Example 1

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

print()


# Example 2

letters = ["A", "B", "C", "D"]

letters.reverse()

print(letters)

print()


# Example 3

shopping_cart = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

shopping_cart.reverse()

print(shopping_cart)

print()


# Time Complexity:
#
# O(n)


# Common Mistake

# Wrong:
#
# numbers = numbers.reverse()
#
# reverse() returns None.


# Best Practice

# Use reverse()
# when you want to modify
# the original list.
#
# Use reversed()
# when you want a reverse iterator.


# Real-World Usage

history = [
    "Login",
    "Open Dashboard",
    "Logout"
]

history.reverse()

print(history)

print()


# ==================================================
# copy()
# ==================================================

# Purpose:
# Creates a shallow copy of the list.


# Syntax:
#
# list.copy()


# Parameters:
#
# None


# Return Value:
#
# A new list.


# Example 1

list1 = [10, 20, 30]

list2 = list1.copy()

print(list1)

print(list2)

print()


# Example 2

list2.append(40)

print(list1)

print(list2)

print()


# Example 3

fruits = ["Apple", "Banana"]

backup = fruits.copy()

backup.append("Mango")

print(fruits)

print(backup)

print()


# Time Complexity:
#
# O(n)


# Common Mistake

# Assignment does NOT copy a list.

list1 = [1, 2, 3]

list2 = list1

list2.append(4)

print(list1)

print(list2)

print()

# Both variables refer to the same list.


# Correct Way

list3 = list1.copy()

list3.append(100)

print(list1)

print(list3)

print()


# Best Practice

# Use copy()
# whenever you need an independent list.


# Real-World Usage

student_marks = [80, 90, 85]

backup_marks = student_marks.copy()

print(student_marks)

print(backup_marks)

print()


# ==================================================
# List Methods Summary
# ==================================================

# Method          Purpose
# ---------------------------------------------
# append()        Add one element
# extend()        Add multiple elements
# insert()        Insert at a position
# remove()        Remove by value
# pop()           Remove by index
# clear()         Remove all elements
# index()         Find first matching index
# count()         Count occurrences
# sort()          Sort original list
# reverse()       Reverse original list
# copy()          Create a shallow copy


# ==================================================
# Time Complexity Table
# ==================================================

# Method              Complexity
# ------------------------------------
# append()              O(1)
# extend()              O(k)
# insert()              O(n)
# remove()              O(n)
# pop() End             O(1)
# pop() Middle          O(n)
# clear()               O(n)
# index()               O(n)
# count()               O(n)
# sort()                O(n log n)
# reverse()             O(n)
# copy()                O(n)


# ==================================================
# Common Errors
# ==================================================

# Error 1
#
# numbers = []
# numbers.pop()
#
# IndexError


# Error 2
#
# fruits.remove("Orange")
#
# ValueError


# Error 3
#
# numbers = numbers.sort()
#
# numbers becomes None


# Error 4
#
# list2 = list1
#
# This creates another reference,
# NOT another copy.


# ==================================================
# Best Practices
# ==================================================

# ✓ Use append() to add one element.
#
# ✓ Use extend() to combine collections.
#
# ✓ Use insert() only when position matters.
#
# ✓ Use remove() when you know the value.
#
# ✓ Use pop() when you need the removed item.
#
# ✓ Use copy() before modifying important data.
#
# ✓ Use sort() only when changing
#   the original order is acceptable.
#
# ✓ Use clear() to empty a list
#   without deleting the variable.


# ==================================================
# Interview Questions
# ==================================================

# Q1.
#
# Difference between append() and extend()?


# Q2.
#
# Difference between sort() and sorted()?


# Q3.
#
# Difference between remove() and pop()?


# Q4.
#
# Difference between reverse() and reversed()?


# Q5.
#
# Difference between
#
# list2 = list1
#
# and
#
# list2 = list1.copy()


# ==================================================
# Mini Project
# ==================================================

shopping_cart = []

shopping_cart.append("Laptop")

shopping_cart.append("Mouse")

shopping_cart.append("Keyboard")

shopping_cart.remove("Mouse")

shopping_cart.insert(1, "Headphones")

shopping_cart.sort()

print("Shopping Cart")

for item in shopping_cart:

    print("-", item)

print()

print("Total Items:", len(shopping_cart))

print()


# ==================================================
# Cheat Sheet
# ==================================================

# Add One
#
# append()

# Add Many
#
# extend()

# Insert
#
# insert()

# Remove by Value
#
# remove()

# Remove by Index
#
# pop()

# Empty List
#
# clear()

# Find Position
#
# index()

# Count Occurrences
#
# count()

# Sort
#
# sort()

# Reverse
#
# reverse()

# Copy
#
# copy()


# ==================================================
# Summary
# ==================================================

# ✓ Lists provide many useful built-in methods.
#
# ✓ Most methods modify the original list.
#
# ✓ Most methods return None.
#
# ✓ copy() creates a shallow copy.
#
# ✓ Understanding these methods is essential
#   before learning tuples, sets and dictionaries.