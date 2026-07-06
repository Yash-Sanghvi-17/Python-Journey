"""
==================================================
Python Journey - Functions
File: 04_default_arguments.py
Topic: Default Arguments
==================================================

Objective:
- Understand what default arguments are.
- Learn how they make functions more flexible.
- Use default values when arguments are not provided.

Concepts Covered:
1. Default arguments
2. Overriding default values
3. Mixing required and default parameters
4. Rules for default arguments
"""

# ==================================================
# What are Default Arguments?
# ==================================================

# A default argument is a parameter that already has
# a predefined value.
#
# If the caller does not provide an argument,
# Python automatically uses the default value.
#
# Syntax:
#
# def function_name(parameter=default_value):
#     # Function body


# ==================================================
# Example 1: Basic Default Argument
# ==================================================

def greet(name="Guest"):
    print(f"Hello, {name}!")


greet()
greet("Yash")

print()


# ==================================================
# Example 2: Default Age
# ==================================================

def student(name, age=18):
    print(f"Name : {name}")
    print(f"Age  : {age}")


student("Alice")
print()

student("Bob", 20)

print()


# ==================================================
# Example 3: Default Quantity
# ==================================================

def order(item, quantity=1):
    print(f"Item     : {item}")
    print(f"Quantity : {quantity}")


order("Laptop")
print()

order("Mouse", 2)

print()


# ==================================================
# Example 4: Multiple Default Arguments
# ==================================================

def employee(name, department="IT", city="Ahmedabad"):
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"City       : {city}")


employee("Rahul")

print()

employee("Priya", "HR", "Mumbai")

print()


# ==================================================
# Example 5: Overriding Default Values
# ==================================================

def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(5, 3))

print()


# ==================================================
# Rules for Default Arguments
# ==================================================

# Rule 1:
# Parameters with default values must come AFTER
# required parameters.
#
# Correct:
#
# def example(name, age=18):
#     pass
#
# Wrong:
#
# def example(age=18, name):
#     pass


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Placing required parameters after default parameters.
#
# Wrong:
# Assuming the default value is always used.
# If an argument is passed, it replaces the default.


# ==================================================
# Best Practices
# ==================================================

# ✓ Use default values for optional information.
# ✓ Keep default values simple and meaningful.
# ✓ Place required parameters first.
# ✓ Avoid unnecessary default arguments.


# ==================================================
# Summary
# ==================================================

# ✓ Default arguments provide predefined values.
# ✓ They are used when no argument is supplied.
# ✓ Passing an argument overrides the default value.
# ✓ Required parameters must come before default parameters.