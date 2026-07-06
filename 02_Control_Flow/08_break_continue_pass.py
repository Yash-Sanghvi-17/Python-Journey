"""
=========================================================
File: 08_break_continue_pass.py
Topic: break, continue, and pass Statements
Folder: 02_Control_Flow
=========================================================

Description:
------------
These statements control the flow of loops.

break
-----
Immediately exits the nearest loop.

continue
--------
Skips the current iteration and moves to the next one.

pass
----
Does nothing. It is used as a placeholder where Python
expects a statement.

Syntax:
-------
break

continue

pass
"""

# =========================================================
# break Statement
# =========================================================

# Example 1: Exit Loop Early

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5


# =========================================================
# Example 2: Stop When Item Found
# =========================================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

for fruit in fruits:

    if fruit == "Mango":
        print("Fruit Found!")
        break

    print(fruit)

# Output:
# Apple
# Banana
# Fruit Found!


# =========================================================
# Example 3: Password Attempts
# =========================================================

correct_password = "python123"

while True:

    password = input("Enter Password: ")

    if password == correct_password:
        print("Access Granted")
        break

    print("Incorrect Password")

# Loop stops only after correct password.


# =========================================================
# continue Statement
# =========================================================

# Example 4: Skip One Number

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

# Output:
# 1
# 2
# 4
# 5


# =========================================================
# Example 5: Print Only Even Numbers
# =========================================================

for number in range(1, 11):

    if number % 2 != 0:
        continue

    print(number)

# Output:
# 2
# 4
# 6
# 8
# 10


# =========================================================
# Example 6: Skip a Character
# =========================================================

word = "PYTHON"

for letter in word:

    if letter == "H":
        continue

    print(letter)

# Output:
# P
# Y
# T
# O
# N


# =========================================================
# pass Statement
# =========================================================

# Example 7: Empty if Block

age = 18

if age >= 18:
    pass

print("Program Continues")

# Output:
# Program Continues


# =========================================================
# Example 8: Empty Loop
# =========================================================

for number in range(5):
    pass

print("Loop Finished")

# Output:
# Loop Finished


# =========================================================
# Example 9: Placeholder Function
# =========================================================

def future_feature():
    pass

print("Function Created Successfully")

# Output:
# Function Created Successfully


# =========================================================
# Example 10: Combining break and continue
# =========================================================

for number in range(1, 11):

    if number == 3:
        continue

    if number == 8:
        break

    print(number)

# Output:
# 1
# 2
# 4
# 5
# 6
# 7


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Using break outside a loop
#
# break
#
# Error:
# SyntaxError


# ❌ Using continue outside a loop
#
# continue
#
# Error:
# SyntaxError


# ❌ Forgetting that break ends the loop completely
#
# It does NOT continue to the next iteration.


# ❌ Confusing continue with pass
#
# continue → Skips current iteration.
# pass → Does absolutely nothing.


# =========================================================
# Best Practices
# =========================================================

# ✔ Use break when the required result is found.

# ✔ Use continue to skip unwanted iterations.

# ✔ Use pass as a temporary placeholder.

# ✔ Avoid excessive use of break and continue,
# as it may reduce code readability.


# =========================================================
# Quick Revision
# =========================================================

# break
# -----
# -> Immediately exits the nearest loop.

# continue
# --------
# -> Skips the current iteration.

# pass
# ----
# -> Does nothing.

# Remember:
#
# break    = Stop the loop.
#
# continue = Skip this iteration.
#
# pass     = Ignore for now.


# =========================================================
# Comparison Table
# =========================================================

# Statement   Effect
# ---------   -------------------------------
# break       Exits the loop completely.
# continue    Skips the current iteration.
# pass        Performs no action.


# =========================================================
# Did You Know?
# =========================================================

# 💡 break only exits the nearest enclosing loop.

# 💡 continue does not stop the loop—it simply skips
# the remaining code for the current iteration.

# 💡 pass is often used while writing code that will
# be implemented later.


# =========================================================
# Mini Challenge
# =========================================================

# 1. Print numbers from 1 to 20, but skip multiples of 3.

# 2. Stop printing numbers when you reach 15.

# 3. Ask the user for a password until it is correct.

# 4. Create an empty function using pass.

# 5. Print all letters of your name except vowels.