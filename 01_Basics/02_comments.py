# ============================================
# Topic: Comments
# Folder: 01_Basics
# Description: Understanding comments in Python.
# ============================================

# --------------------------------------------
# Single-line Comments
# --------------------------------------------

# Anything after '#' is ignored by Python.

print("Hello, World!")  # This comment explains the statement.

# Comments improve code readability.
# They help other developers (and your future self) understand the code.

# --------------------------------------------
# Multi-line Comments
# --------------------------------------------

# Python doesn't have true multi-line comments.
# Instead, write multiple single-line comments.

# This is line 1.
# This is line 2.
# This is line 3.

# --------------------------------------------
# Docstrings
# --------------------------------------------

"""
Triple quotes create a string.

When placed inside functions, classes, or modules,
they act as documentation (Docstrings).

Outside them, they are simply ignored if unused.
"""

# Example Function with a Docstring

def greet():
    """Prints a greeting message."""
    print("Welcome!")

greet()

# --------------------------------------------
# Best Practices
# --------------------------------------------

# Good Comment
radius = 10  # Radius of the circle in centimeters

# Bad Comment
# x = 10      # Assigning 10 to x (too obvious)

# Use comments to explain WHY, not WHAT.

# --------------------------------------------
# End of File
# --------------------------------------------