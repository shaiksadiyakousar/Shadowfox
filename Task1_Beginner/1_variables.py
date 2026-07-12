"""
ShadowFox Python Development Internship
Task 1 (Beginner) - Topic 1: Variables
Author: Shaik Sadiya Kousar
"""

# ---------------------------------------------------------
# 1. Create a variable named pi and store the value 22/7 in it.
#    Check the data type of this variable.
# ---------------------------------------------------------
pi = 22 / 7
print("1. Value of pi:", pi)
print("   Data type of pi:", type(pi))
print()


# ---------------------------------------------------------
# 2. Create a variable called 'for' and assign it a value 4.
#    See what happens and find out the reason behind it.
# ---------------------------------------------------------
# Uncommenting the line below will raise a SyntaxError:
# for = 4
#
# Reason: 'for' is a reserved KEYWORD in Python (used to build for-loops).
# Python keywords cannot be used as variable names because the interpreter
# needs them to remain fixed, unambiguous parts of its grammar.
# You can check all reserved keywords like this:
import keyword
print("2. Is 'for' a Python keyword?", keyword.iskeyword("for"))
print("   All Python keywords:", keyword.kwlist)
print()


# ---------------------------------------------------------
# 3. Store principal, rate of interest, and time in variables,
#    then calculate Simple Interest for 3 years.
#    Formula: Simple Interest = P x R x T / 100
# ---------------------------------------------------------
principal = 10000      # amount in rupees
rate = 8                # rate of interest in %
time = 3                 # time in years

simple_interest = (principal * rate * time) / 100
print("3. Principal:", principal, "| Rate:", rate, "% | Time:", time, "years")
print("   Simple Interest for 3 years:", simple_interest)
