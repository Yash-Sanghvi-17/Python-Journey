"""
==================================================
Python Journey - Functions
File: 06_variable_length_arguments.py
Topic: Variable Length Arguments
==================================================

Objective:
- Understand why variable length arguments are needed.
- Learn how to use *args and **kwargs.
- Understand packing and unpacking of arguments.

Concepts Covered:
1. *args
2. **kwargs
3. Packing arguments
4. Unpacking arguments
"""

# ==================================================
# Why Variable Length Arguments?
# ==================================================

# Sometimes we don't know how many arguments
# a function will receive.
#
# Instead of creating many parameters,
# Python provides:
#
# *args   -> Multiple positional arguments
# **kwargs -> Multiple keyword arguments


# ==================================================
# Example 1: *args
# ==================================================

# *args collects multiple positional arguments
# into a tuple.

def add_numbers(*args):
    print("Arguments:", args)
    print("Type:", type(args))


add_numbers(10, 20, 30)
add_numbers(1, 2, 3, 4, 5)

print()


# ==================================================
# Example 2: Loop Through *args
# ==================================================

def total(*numbers):
    total_sum = 0

    for number in numbers:
        total_sum += number

    print("Total =", total_sum)


total(5, 10)
total(10, 20, 30)
total(1, 2, 3, 4, 5)

print()


# ==================================================
# Example 3: **kwargs
# ==================================================

# **kwargs collects multiple keyword arguments
# into a dictionary.

def student_info(**kwargs):
    print(kwargs)
    print(type(kwargs))


student_info(name="Yash", age=20, course="Python")

print()


# ==================================================
# Example 4: Loop Through **kwargs
# ==================================================

def display_details(**details):

    for key, value in details.items():
        print(f"{key} : {value}")


display_details(
    name="Alice",
    age=21,
    city="Ahmedabad"
)

print()


# ==================================================
# Example 5: Using *args and **kwargs Together
# ==================================================

def demo(*args, **kwargs):

    print("Positional Arguments:")
    print(args)

    print()

    print("Keyword Arguments:")
    print(kwargs)


demo(
    10,
    20,
    30,
    name="Yash",
    course="Python"
)

print()


# ==================================================
# Packing Arguments
# ==================================================

# Packing means collecting multiple values
# into one variable.
#
# Example:
#
# def example(*args):
#     pass
#
# args becomes a tuple.


# ==================================================
# Unpacking Arguments
# ==================================================

numbers = [10, 20, 30]

print("Unpacking List")

def add(a, b, c):
    print(a + b + c)


add(*numbers)

print()


student = {
    "name": "Yash",
    "age": 20
}

print("Unpacking Dictionary")

def introduce(name, age):
    print(f"{name} is {age} years old.")


introduce(**student)

print()


# ==================================================
# Rules
# ==================================================

# Function parameter order:
#
# 1. Normal parameters
# 2. *args
# 3. Default parameters
# 4. **kwargs
#
# Example:
#
# def example(a, *args, b=10, **kwargs):
#     pass


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Forgetting * while unpacking.
#
# add(numbers)
#
# Correct:
#
# add(*numbers)


# Wrong:
# Forgetting ** while unpacking dictionaries.
#
# introduce(student)
#
# Correct:
#
# introduce(**student)


# ==================================================
# Best Practices
# ==================================================

# ✓ Use *args when the number of positional
#   arguments is unknown.
#
# ✓ Use **kwargs for optional named arguments.
#
# ✓ Give meaningful names instead of always
#   using args and kwargs when appropriate.
#
# ✓ Don't overuse variable length arguments
#   when fixed parameters are sufficient.


# ==================================================
# Summary
# ==================================================

# ✓ *args collects positional arguments into a tuple.
# ✓ **kwargs collects keyword arguments into a dictionary.
# ✓ Packing groups multiple values together.
# ✓ Unpacking separates values using * or **.
# ✓ Variable length arguments make functions flexible.