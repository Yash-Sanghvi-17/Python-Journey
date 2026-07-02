# ============================================
# Topic: Type Casting
# Folder: 01_Basics
# Description: Converting one data type into another.
# ============================================

# --------------------------------------------
# Integer to Float
# --------------------------------------------

num = 10

result = float(num)

print(result)
print(type(result))

# --------------------------------------------
# Float to Integer
# --------------------------------------------

price = 99.99

value = int(price)

print(value)

# Decimal part is removed (not rounded).

# --------------------------------------------
# Integer to String
# --------------------------------------------

age = 20

text = str(age)

print(text)
print(type(text))

# --------------------------------------------
# String to Integer
# --------------------------------------------

marks = "95"

number = int(marks)

print(number)
print(type(number))

# --------------------------------------------
# String to Float
# --------------------------------------------

cgpa = "8.75"

value = float(cgpa)

print(value)

# --------------------------------------------
# Boolean Conversion
# --------------------------------------------

print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))

print(bool([]))
print(bool([1, 2, 3]))

# --------------------------------------------
# List, Tuple and Set Conversion
# --------------------------------------------

numbers = [1, 2, 3]

print(tuple(numbers))

print(set(numbers))

# --------------------------------------------
# Invalid Conversion
# --------------------------------------------

# text = "Hello"

# int(text)
# ValueError

# --------------------------------------------
# Implicit Type Casting
# --------------------------------------------

a = 10
b = 2.5

print(a + b)

# Python automatically converts int to float.

# --------------------------------------------
# Explicit Type Casting
# --------------------------------------------

x = "100"

y = int(x)

print(y + 50)

# --------------------------------------------
# End of File
# --------------------------------------------