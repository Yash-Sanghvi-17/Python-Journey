"""
==================================================
Python Journey - Data Structures
File: 02_list_methods.py
Topic: List Methods
==================================================

Objective:
- Learn all commonly used list methods.
- Understand how each method modifies a list.
- Differentiate between similar methods.
- Write cleaner and more efficient Python code.

Prerequisites:
- Lists
- Indexing
- Slicing
- Loops

Concepts Covered:
1. append()
2. extend()
3. insert()
4. remove()
5. pop()
6. clear()
7. index()
8. count()
9. sort()
10. reverse()
11. copy()
"""

# ==================================================
# What are List Methods?
# ==================================================

# List methods are built-in functions that belong
# specifically to Python lists.
#
# Unlike built-in functions such as len() or max(),
# list methods are called using dot (.) notation.
#
# Syntax:
#
# list_name.method()


# ==================================================
# append()
# ==================================================

# Purpose:
# Adds ONE element to the end of the list.


# Syntax:
#
# list.append(item)


# Parameters:
#
# item -> The element to be added.


# Return Value:
#
# None
#
# The original list is modified.


# Example 1

fruits = ["Apple", "Banana"]

fruits.append("Mango")

print(fruits)

print()


# Example 2

numbers = [10, 20]

numbers.append(30)

print(numbers)

print()


# Example 3

languages = ["Python", "Java"]

new_language = "C++"

languages.append(new_language)

print(languages)

print()


# Example 4
# Appending another list

list1 = [1, 2]

list2 = [3, 4]

list1.append(list2)

print(list1)

print()

# Output:
# [1, 2, [3, 4]]
#
# append() adds the entire list
# as ONE element.


# Time Complexity:
#
# O(1) Average


# Common Mistakes

# Wrong:
#
# numbers = [1,2]
# numbers = numbers.append(3)
#
# append() returns None.


# Best Practice

# Use append() when adding
# a single element.


# Real-World Usage

# Shopping Cart

cart = []

cart.append("Laptop")

cart.append("Mouse")

print(cart)

print()


# Interview Note

# append() always adds exactly
# one object.


# ==================================================
# extend()
# ==================================================

# Purpose:
# Adds multiple elements from another iterable.


# Syntax:
#
# list.extend(iterable)


# Parameters:
#
# iterable
#
# (list, tuple, string, set, etc.)


# Return Value:
#
# None


# Example 1

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

print()


# Example 2

languages = ["Python"]

languages.extend(("Java", "C++"))

print(languages)

print()


# Example 3

letters = ["A"]

letters.extend("BCD")

print(letters)

print()


# Example 4

list1 = [10, 20]

list2 = [30, 40]

list1.extend(list2)

print(list1)

print()


# Time Complexity:
#
# O(k)
#
# k = Number of inserted elements.


# Common Mistakes

# Confusing append() and extend()

# append([3,4])
#
# [1,2,[3,4]]

# extend([3,4])
#
# [1,2,3,4]


# Best Practice

# Use extend()
# when adding multiple values.


# Real-World Usage

student_names = ["Alice", "Bob"]

new_students = ["Charlie", "David"]

student_names.extend(new_students)

print(student_names)

print()


# ==================================================
# append() vs extend()
# ==================================================

list1 = [1, 2]

list1.append([3, 4])

print("append():", list1)

print()

list2 = [1, 2]

list2.extend([3, 4])

print("extend():", list2)

print()


# Summary
#
# append()
#
# Adds ONE object.
#
# extend()
#
# Adds EACH element individually.