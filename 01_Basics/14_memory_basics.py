# ============================================
# Topic: Memory Basics
# Folder: 01_Basics
# Description: Understanding how Python stores variables in memory.
# ============================================

# --------------------------------------------
# Variables Store References
# --------------------------------------------

a = 10
b = a

print(a)
print(b)

# Both variables refer to the same integer object.

# --------------------------------------------
# Checking Memory Address
# --------------------------------------------

x = 100
y = 100

print(id(x))
print(id(y))

# id() returns the memory address (or unique identity)
# of an object.

# --------------------------------------------
# Different Objects
# --------------------------------------------

name1 = "Python"
name2 = "Java"

print(id(name1))
print(id(name2))

# Different values usually have different memory addresses.

# --------------------------------------------
# Reassigning Variables
# --------------------------------------------

num = 50

print(num)
print(id(num))

num = 100

print(num)
print(id(num))

# The variable now refers to a different object.

# --------------------------------------------
# Immutable Objects
# --------------------------------------------

a = 10
b = a

a = 20

print(a)
print(b)

# Changing 'a' does not affect 'b'
# because integers are immutable.

# --------------------------------------------
# Mutable Objects
# --------------------------------------------

list1 = [1, 2, 3]
list2 = list1

list1.append(4)

print(list1)
print(list2)

# Both variables refer to the same list object,
# so changes are reflected in both.

# --------------------------------------------
# Copying a List
# --------------------------------------------

list3 = list1.copy()

list1.append(5)

print(list1)
print(list3)

# copy() creates a new list object.

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

numbers1 = [10, 20]
numbers2 = numbers1

numbers2.append(30)

print(numbers1)

# Both variables point to the same list.

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Use copy() when creating an independent copy.
# ✔ Remember that immutable objects create new references.
# ✔ Use id() only for learning and debugging purposes.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# • Variables store references to objects.
# • id() returns an object's identity.
# • Integers and strings are immutable.
# • Lists are mutable.
# • copy() creates a separate list.

# --------------------------------------------
# End of File
# --------------------------------------------