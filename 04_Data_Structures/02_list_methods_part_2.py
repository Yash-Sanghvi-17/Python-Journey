# ==================================================
# insert()
# ==================================================

# Purpose:
# Inserts an element at a specified position.
#
# Unlike append(), insert() allows you to choose
# where the new element should be placed.


# Syntax:
#
# list.insert(index, item)


# Parameters:
#
# index -> Position where the element is inserted.
# item  -> Element to insert.


# Return Value:
#
# None
#
# The original list is modified.


# Example 1

fruits = ["Apple", "Banana", "Mango"]

fruits.insert(1, "Orange")

print(fruits)

print()


# Example 2

numbers = [20, 30, 40]

numbers.insert(0, 10)

print(numbers)

print()


# Example 3

languages = ["Python", "Java"]

languages.insert(10, "C++")

print(languages)

print()

# If the index is greater than the list length,
# Python adds the element at the end.


# Example 4

colors = ["Red", "Blue"]

colors.insert(-1, "Green")

print(colors)

print()

# Negative indexing works here as well.


# Time Complexity:
#
# Beginning : O(n)
# Middle    : O(n)
# End       : O(1) Approx.


# Common Mistakes

# Wrong:
#
# numbers = [1, 2]
# numbers = numbers.insert(0, 100)
#
# insert() returns None.


# Best Practice

# Use insert() only when position matters.
#
# Otherwise, prefer append() because it is faster.


# Real-World Usage

rankings = ["Silver", "Bronze"]

rankings.insert(0, "Gold")

print(rankings)

print()


# Did You Know?
#
# Inserting at the beginning of a large list is
# slower because all existing elements must shift.


# ==================================================
# remove()
# ==================================================

# Purpose:
# Removes the FIRST matching value from the list.


# Syntax:
#
# list.remove(value)


# Parameters:
#
# value -> Element to remove.


# Return Value:
#
# None


# Example 1

fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

print()


# Example 2

numbers = [10, 20, 20, 30]

numbers.remove(20)

print(numbers)

print()

# Only the FIRST occurrence is removed.


# Example 3

colors = ["Red", "Blue", "Green"]

colors.remove("Green")

print(colors)

print()


# Time Complexity:
#
# O(n)


# Common Mistakes

# Wrong:
#
# numbers.remove(100)
#
# Raises:
# ValueError
#
# Because the value doesn't exist.


# Safe Way

numbers = [10, 20, 30]

if 20 in numbers:
    numbers.remove(20)

print(numbers)

print()


# Best Practice

# Always check whether the value exists
# if you're unsure.


# Real-World Usage

cart = ["Laptop", "Mouse", "Keyboard"]

cart.remove("Mouse")

print(cart)

print()


# Did You Know?
#
# remove() searches from left to right and stops
# after removing the first matching value.


# ==================================================
# pop()
# ==================================================

# Purpose:
# Removes and RETURNS an element.


# Syntax:
#
# list.pop(index)
#
# index is optional.


# Return Value:
#
# Removed element.


# Example 1

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print("Removed:", removed)

print(numbers)

print()


# Example 2

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print("Removed:", removed)

print(numbers)

print()


# Example 3

stack = ["A", "B", "C"]

while stack:

    print("Popped:", stack.pop())

print()


# Example 4

tasks = ["Study", "Exercise", "Sleep"]

last_task = tasks.pop()

print("Completed:", last_task)

print(tasks)

print()


# Time Complexity:
#
# pop() from end       : O(1)
#
# pop(index) elsewhere : O(n)


# Common Mistakes

# Wrong:
#
# empty = []
# empty.pop()
#
# Raises:
# IndexError


# Safe Way

numbers = []

if numbers:
    numbers.pop()

print(numbers)

print()


# Best Practice

# Use pop() when you need the removed value.
#
# Use remove() when you already know the value.


# Real-World Usage

browser_history = [
    "Google",
    "YouTube",
    "GitHub"
]

last_page = browser_history.pop()

print("Back to:", browser_history[-1])

print("Closed:", last_page)

print()


# Interview Notes
#
# remove()
#
# Removes by VALUE.
#
# pop()
#
# Removes by INDEX.
#
# pop() also RETURNS the removed element.


# ==================================================
# Quick Comparison
# ==================================================

# append()
#
# Adds one element at the end.
#
# Time Complexity:
# O(1)


# extend()
#
# Adds multiple elements.
#
# Time Complexity:
# O(k)


# insert()
#
# Inserts at a specific position.
#
# Time Complexity:
# O(n)


# remove()
#
# Removes by value.
#
# Time Complexity:
# O(n)


# pop()
#
# Removes by index.
#
# Time Complexity:
# O(1) from end