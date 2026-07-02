# ============================================
# Topic: Constants
# Folder: 01_Basics
# Description: Understanding constants in Python.
# ============================================

# --------------------------------------------
# What are Constants?
# --------------------------------------------

# Python does not have true constants.
# By convention, variables written in UPPER_CASE
# are treated as constants.

PI = 3.14159
GRAVITY = 9.8
MAX_USERS = 100

print(PI)
print(GRAVITY)
print(MAX_USERS)

# --------------------------------------------
# Constants Can Still Change
# --------------------------------------------

PI = 3.14

print(PI)

# Python allows reassignment,
# but it is discouraged.

# --------------------------------------------
# Naming Convention
# --------------------------------------------

DATABASE_NAME = "StudentDB"
API_KEY = "ABC123XYZ"

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# Using lowercase for constants.

# Bad
pi = 3.14

# Good
PI = 3.14

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Use UPPER_CASE for constants.
# ✔ Avoid changing constants after declaration.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# • No true constants.
# • UPPER_CASE naming convention.
# • Avoid modifying them.

# --------------------------------------------
# End of File
# --------------------------------------------