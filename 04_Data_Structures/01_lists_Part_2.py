# ==================================================
# Built-in Functions for Lists
# ==================================================

# Built-in functions are functions provided by Python
# that work with many different data types, including lists.


# ==================================================
# 1. len()
# ==================================================

# Purpose:
# Returns the total number of elements in a list.

# Syntax:
# len(list_name)

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))

print()

# Time Complexity:
# O(1)

# Common Mistake:
# len(numbers) gives the number of elements,
# NOT the last index.


# ==================================================
# 2. max()
# ==================================================

# Purpose:
# Returns the largest element.

# Syntax:
# max(list_name)

numbers = [25, 67, 14, 98, 45]

print("Maximum:", max(numbers))

print()

# Works with strings too.

fruits = ["Apple", "Mango", "Banana"]

print(max(fruits))

print()

# Time Complexity:
# O(n)


# ==================================================
# 3. min()
# ==================================================

# Purpose:
# Returns the smallest element.

numbers = [25, 67, 14, 98, 45]

print("Minimum:", min(numbers))

print()

# Time Complexity:
# O(n)


# ==================================================
# 4. sum()
# ==================================================

# Purpose:
# Adds all numeric values.

numbers = [10, 20, 30, 40]

print("Total:", sum(numbers))

print()

# Optional starting value.

print(sum(numbers, 100))

print()

# Time Complexity:
# O(n)

# Common Mistake:
# sum() works only with numeric values.


# ==================================================
# 5. sorted()
# ==================================================

# Purpose:
# Returns a NEW sorted list.
# Original list remains unchanged.

numbers = [50, 10, 30, 20, 40]

ascending = sorted(numbers)

descending = sorted(numbers, reverse=True)

print("Original :", numbers)
print("Ascending:", ascending)
print("Descending:", descending)

print()

# Time Complexity:
# O(n log n)


# ==================================================
# 6. reversed()
# ==================================================

# Purpose:
# Returns a reverse iterator.

numbers = [1, 2, 3, 4, 5]

reverse_numbers = list(reversed(numbers))

print(reverse_numbers)

print()

# Time Complexity:
# O(n)

# Note:
# reversed() does NOT modify the original list.


# ==================================================
# 7. list()
# ==================================================

# Purpose:
# Creates a list from another iterable.

text = "Python"

characters = list(text)

print(characters)

print()

tuple_data = (10, 20, 30)

print(list(tuple_data))

print()

# Time Complexity:
# O(n)


# ==================================================
# 8. any()
# ==================================================

# Purpose:
# Returns True if at least one element is True.

values = [False, False, True]

print(any(values))

print()

numbers = [0, 0, 5]

print(any(numbers))

print()

# Time Complexity:
# O(n)


# ==================================================
# 9. all()
# ==================================================

# Purpose:
# Returns True if every element is True.

values = [True, True, True]

print(all(values))

print()

values = [True, False, True]

print(all(values))

print()

# Time Complexity:
# O(n)


# ==================================================
# 10. enumerate()
# ==================================================

# Purpose:
# Returns both index and value.

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

print()

# Custom starting index.

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

print()

# Time Complexity:
# O(n)


# ==================================================
# 11. zip()
# ==================================================

# Purpose:
# Combines multiple iterables.

names = ["Alice", "Bob", "Charlie"]

marks = [85, 90, 95]

combined = list(zip(names, marks))

print(combined)

print()

# Three lists.

cities = ["Ahmedabad", "Mumbai", "Delhi"]

details = list(zip(names, marks, cities))

print(details)

print()

# Time Complexity:
# O(n)


# ==================================================
# Bonus Built-in Functions
# ==================================================

# These are also useful when working with lists.


# ==================================================
# sorted() with key
# ==================================================

students = ["Rahul", "Alice", "Bob", "Christopher"]

print(sorted(students, key=len))

print()


# ==================================================
# max() with key
# ==================================================

print(max(students, key=len))

print()


# ==================================================
# min() with key
# ==================================================

print(min(students, key=len))

print()


# ==================================================
# Practical Example
# ==================================================

marks = [91, 84, 77, 95, 89]

print("Highest :", max(marks))
print("Lowest  :", min(marks))
print("Average :", sum(marks) / len(marks))
print("Sorted  :", sorted(marks))

print()


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
#
# max([10, "Python"])
#
# Error:
# TypeError
#
# Because integers and strings
# cannot be compared.


# Wrong:
#
# sum(["A", "B"])
#
# Error:
# TypeError


# Wrong:
#
# reversed(list)
#
# It returns an iterator.
#
# Use:
#
# list(reversed(list_name))


# ==================================================
# Best Practices
# ==================================================

# ✓ Use len() instead of manual counting.
#
# ✓ Use sorted() when you want to keep
#   the original list unchanged.
#
# ✓ Use enumerate() instead of manually
#   managing indexes.
#
# ✓ Use zip() to combine related data.
#
# ✓ Use any() and all() for cleaner conditions.


# ==================================================
# Interview Notes
# ==================================================

# Question:
# Difference between sort() and sorted()?
#
# sorted()
# ----------
# Built-in Function
# Returns a NEW list
# Original list remains unchanged
#
# sort()
# ----------
# List Method
# Modifies original list
# Returns None
#
# (Covered completely in 02_list_methods.py)