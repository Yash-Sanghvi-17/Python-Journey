# ==================================================
# clear()
# ==================================================

# Purpose:
# Removes ALL elements from the list.
#
# The list itself still exists,
# but becomes empty.


# Syntax:
#
# list.clear()


# Parameters:
#
# None


# Return Value:
#
# None


# Example 1

fruits = ["Apple", "Banana", "Mango"]

fruits.clear()

print(fruits)

print()


# Example 2

numbers = [10, 20, 30, 40]

print("Before:", numbers)

numbers.clear()

print("After :", numbers)

print()


# Time Complexity:
#
# O(n)


# Common Mistakes

# clear() does NOT delete the variable.
#
# Wrong Thinking:
#
# numbers.clear()
# print(numbers)
#
# This works perfectly.
#
# Output:
# []


# Best Practice

# Use clear() when you want to reuse
# the same list later.


# Real-World Usage

shopping_cart = [
    "Laptop",
    "Mouse",
    "Keyboard"
]

print("Order Completed!")

shopping_cart.clear()

print(shopping_cart)

print()


# Did You Know?
#
# clear() is cleaner than repeatedly
# removing each element one by one.


# ==================================================
# index()
# ==================================================

# Purpose:
# Returns the index of the FIRST occurrence
# of a value.


# Syntax:
#
# list.index(value)
#
# list.index(value, start)
#
# list.index(value, start, end)


# Parameters:
#
# value -> Element to search.
#
# start -> Optional starting index.
#
# end -> Optional ending index.


# Return Value:
#
# Index of the first matching element.


# Example 1

fruits = ["Apple", "Banana", "Mango"]

print(fruits.index("Banana"))

print()


# Example 2

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))

print()


# Example 3

numbers = [5, 10, 15, 10, 20]

print(numbers.index(10, 2))

print()

# Search starts from index 2.


# Time Complexity:
#
# O(n)


# Common Mistakes

# Wrong:
#
# fruits.index("Orange")
#
# Raises:
# ValueError


# Safe Way

if "Banana" in fruits:
    print(fruits.index("Banana"))

print()


# Best Practice

# Check whether the element exists
# before calling index()
# when uncertain.


# Real-World Usage

students = [
    "Alice",
    "Bob",
    "Charlie"
]

position = students.index("Charlie")

print(position)

print()


# ==================================================
# count()
# ==================================================

# Purpose:
# Counts how many times
# an element appears.


# Syntax:
#
# list.count(value)


# Parameters:
#
# value -> Element to count.


# Return Value:
#
# Integer


# Example 1

numbers = [10, 20, 20, 30, 20]

print(numbers.count(20))

print()


# Example 2

letters = [
    "A",
    "B",
    "A",
    "C",
    "A"
]

print(letters.count("A"))

print()


# Example 3

marks = [90, 80, 90, 95, 90]

count_90 = marks.count(90)

print(count_90)

print()


# Time Complexity:
#
# O(n)


# Common Mistakes

# count() returns the NUMBER
# of occurrences.
#
# It does NOT return indexes.


# Best Practice

# Use count()
# when frequency matters.


# Real-World Usage

votes = [
    "Yes",
    "No",
    "Yes",
    "Yes",
    "No"
]

print("Yes Votes:", votes.count("Yes"))

print()


# Did You Know?
#
# count() scans the entire list
# before returning the answer.


# ==================================================
# sort()
# ==================================================

# Purpose:
# Sorts the ORIGINAL list.
#
# The original order is permanently changed.


# Syntax:
#
# list.sort()
#
# list.sort(reverse=True)
#
# list.sort(key=function)


# Parameters:
#
# reverse
#
# key


# Return Value:
#
# None


# Example 1

numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

print()


# Example 2

numbers = [50, 10, 40, 20, 30]

numbers.sort(reverse=True)

print(numbers)

print()


# Example 3

students = [
    "Rahul",
    "Amit",
    "Christopher",
    "Bob"
]

students.sort(key=len)

print(students)

print()


# Example 4

words = [
    "banana",
    "Apple",
    "cherry"
]

words.sort(key=str.lower)

print(words)

print()


# Time Complexity:
#
# O(n log n)


# Common Mistakes

# Wrong:
#
# numbers = numbers.sort()
#
# sort() returns None.


# Best Practice

# Use sort()
# when you want to modify
# the original list.
#
# Use sorted()
# when you want a NEW list.


# Real-World Usage

scores = [75, 90, 60, 100, 85]

scores.sort(reverse=True)

print(scores)

print()


# Interview Notes

# sort()
#
# Modifies original list.
#
# sorted()
#
# Returns a new list.


# ==================================================
# Quick Comparison
# ==================================================

# clear()
#
# Removes all elements.


# index()
#
# Returns first matching index.


# count()
#
# Counts occurrences.


# sort()
#
# Sorts the original list.