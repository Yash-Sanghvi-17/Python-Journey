# ============================================
# Topic: Keywords
# Folder: 01_Basics
# Description: Reserved words in Python.
# ============================================

import keyword

# --------------------------------------------
# Display All Keywords
# --------------------------------------------

print(keyword.kwlist)

# --------------------------------------------
# Total Number of Keywords
# --------------------------------------------

print(len(keyword.kwlist))

# --------------------------------------------
# Checking a Keyword
# --------------------------------------------

print(keyword.iskeyword("for"))
print(keyword.iskeyword("python"))

# --------------------------------------------
# Common Keywords
# --------------------------------------------

# False
# None
# True
# and
# as
# assert
# break
# class
# continue
# def
# del
# elif
# else
# except
# finally
# for
# from
# global
# if
# import
# in
# is
# lambda
# nonlocal
# not
# or
# pass
# raise
# return
# try
# while
# with
# yield

# --------------------------------------------
# Common Mistakes
# --------------------------------------------

# Wrong
# class = "Python"

# Correct
course = "Python"

# --------------------------------------------
# Best Practices
# --------------------------------------------

# ✔ Never use keywords as variable names.
# ✔ Use keyword.iskeyword() to verify if needed.

# --------------------------------------------
# Quick Revision
# --------------------------------------------

# • Keywords are reserved words.
# • Their meaning is predefined.
# • They cannot be used as identifiers.

# --------------------------------------------
# End of File
# --------------------------------------------