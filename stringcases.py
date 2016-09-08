"""
    Create a function named stringcases that takes a string and returns a tuple of four versions of the string:
    uppercased, lowercased, titlecased
    (where every word's first letter is capitalized), and a reversed version of the string.
"""

# Handy functions:
# .upper() - uppercases a string
# .lower() - lowercases a string
# .title() - titlecases a string
# There is no function to reverse a string.
# Maybe you can do it with a slice?


def stringcases(some_string):
    reversed_string = some_string[len(some_string): 0: -1] + some_string[0]
    return some_string.upper(), some_string.lower(), some_string.title(), reversed_string


print(stringcases("racecar"))