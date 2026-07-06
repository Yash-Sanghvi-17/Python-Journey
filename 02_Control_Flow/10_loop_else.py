"""
==================================================
Python Journey - Control Flow
File: 10_loop_else.py
Topic: Loop Else
==================================================

Objective:
- Understand the purpose of the else block with loops.
- Learn when the else block executes.
- See the difference between normal loop completion and loop termination using break.

Concepts Covered:
1. for...else
2. while...else
3. break with else
"""

# ==================================================
# What is Loop Else?
# ==================================================

# In Python, loops can have an else block.
# The else block executes only if the loop finishes normally.
# If the loop is stopped using 'break', the else block is skipped.

# Syntax:
#
# for item in sequence:
#     # loop body
# else:
#     # executes if loop completes normally


# ==================================================
# Example 1: for loop with else
# ==================================================

print("Example 1")

for number in range(1, 6):
    print(number)

else:
    print("Loop completed successfully.")

print()


# ==================================================
# Example 2: break prevents else from executing
# ==================================================

print("Example 2")

for number in range(1, 6):
    print(number)

    if number == 3:
        print("Break encountered.")
        break

else:
    print("Loop completed successfully.")

print()


# ==================================================
# Example 3: while loop with else
# ==================================================

print("Example 3")

count = 1

while count <= 3:
    print("Count =", count)
    count += 1

else:
    print("While loop finished normally.")

print()


# ==================================================
# Example 4: Searching for an element
# ==================================================

numbers = [10, 20, 30, 40, 50]
target = 30

for num in numbers:
    if num == target:
        print(target, "found!")
        break

else:
    print(target, "not found.")

print()


# ==================================================
# Example 5: Element not found
# ==================================================

numbers = [10, 20, 30, 40, 50]
target = 99

for num in numbers:
    if num == target:
        print(target, "found!")
        break

else:
    print(target, "not found.")

print()


# ==================================================
# Common Mistakes
# ==================================================

# Wrong:
# Thinking the else belongs to the if statement.
#
# Correct:
# The else belongs to the loop, not the if.


# ==================================================
# Summary
# ==================================================

# ✓ Loops can have an else block.
# ✓ else executes only if the loop finishes normally.
# ✓ break skips the else block.
# ✓ Useful for searching operations.