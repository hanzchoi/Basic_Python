# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
# If you use .append(), you'll want to pass it a tuple of new values.

"""
    Create a function named combo() that takes two iterables and returns a list of tuples.
    Each tuple should hold the first item in each list, then the second set,
    then the third, and so on. Assume the iterables will be the same length.
"""


def combo(thing1, thing2):
    temp_tuple = ()

    for step in enumerate(thing1):
        print(step)
        temp_tuple = (thing1[step], thing2[step])

    return temp_tuple

print(combo([1, 2, 3], 'abc'))
