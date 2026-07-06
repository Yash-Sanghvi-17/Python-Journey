"""
=========================================================
File: 07_while_loop.py
Topic: while Loop
Folder: 02_Control_Flow
=========================================================

Description:
------------
A while loop repeatedly executes a block of code as long as
its condition remains True.

It is commonly used when the number of iterations is
unknown beforehand.

Syntax:
-------
while condition:
    # Code Block
"""

# =========================================================
# Example 1: Basic while Loop
# =========================================================

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# =========================================================
# Example 2: Countdown
# =========================================================

number = 5

while number > 0:
    print(number)
    number -= 1

print("Blast Off!")

# Output:
# 5
# 4
# 3
# 2
# 1
# Blast Off!


# =========================================================
# Example 3: User Input Validation
# =========================================================

password = ""

while password != "python123":
    password = input("Enter password: ")

print("Access Granted")

# The loop continues until the correct password is entered.


# =========================================================
# Example 4: Sum of Numbers
# =========================================================

count = 1
total = 0

while count <= 5:
    total += count
    count += 1

print("Sum =", total)

# Output:
# Sum = 15


# =========================================================
# Example 5: Multiplication Table
# =========================================================

number = 7
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# Output:
# 7 x 1 = 7
# ...
# 7 x 10 = 70


# =========================================================
# Example 6: Even Numbers
# =========================================================

number = 2

while number <= 20:
    print(number)
    number += 2

# Output:
# 2
# 4
# ...
# 20


# =========================================================
# Example 7: Guessing Game
# =========================================================

secret = 8
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

print("Correct!")

# The loop stops only when the correct number is guessed.


# =========================================================
# Example 8: Infinite Loop (Avoid)
# =========================================================

# while True:
#     print("Hello")

# This loop never stops unless interrupted manually.
# Press Ctrl + C in the terminal to stop it.


# =========================================================
# Example 9: Boolean Flag
# =========================================================

running = True
count = 1

while running:
    print("Iteration:", count)

    if count == 3:
        running = False

    count += 1

# Output:
# Iteration: 1
# Iteration: 2
# Iteration: 3


# =========================================================
# Example 10: Menu Program
# =========================================================

choice = ""

while choice != "exit":
    choice = input("Type 'exit' to quit: ")

print("Program Closed")

# Useful in menu-driven applications.


# =========================================================
# Common Mistakes
# =========================================================

# ❌ Forgetting to update the loop variable
#
# count = 1
#
# while count <= 5:
#     print(count)
#
# This creates an infinite loop.


# ❌ Wrong indentation
#
# while count <= 5:
# print(count)


# ❌ Forgetting the colon
#
# while count <= 5


# ❌ Incorrect condition
#
# count = 10
#
# while count < 5:
#     print(count)
#
# The loop never executes because the condition
# is already False.


# =========================================================
# Best Practices
# =========================================================

# ✔ Always update the loop variable.

# ✔ Ensure the loop has a stopping condition.

# ✔ Use meaningful variable names.

# ✔ Avoid unnecessary infinite loops.

# ✔ Keep loop logic simple and readable.


# =========================================================
# Quick Revision
# =========================================================

# -> while loops execute as long as the condition is True.

# -> They are ideal when the number of iterations
# is unknown.

# -> Update the loop variable to avoid infinite loops.

# -> The condition is checked before every iteration.

# -> If the condition is False initially,
# the loop never executes.


# =========================================================
# Did You Know?
# =========================================================

# 💡 A while loop may execute zero times if its
# condition is False at the beginning.

# 💡 Login systems and menu-driven programs often
# use while loops.

# 💡 Infinite loops can consume CPU resources if
# they are not stopped properly.


# =========================================================
# Mini Challenge
# =========================================================

# 1. Print numbers from 10 to 1.

# 2. Find the factorial of a number.

# 3. Keep asking for a password until it is correct.

# 4. Print all odd numbers from 1 to 25.

# 5. Create a simple menu that exits only when the
# user enters "exit".