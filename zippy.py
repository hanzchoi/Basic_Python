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
    temp_list = []

    for index, item1 in enumerate(thing1):
        temp_tuple = (item1, thing2[index])
        temp_list.append(temp_tuple)

    return temp_list

print(combo([1, 2, 3], 'abc'))

"""
def combo(iterable_1, iterable_2):
   list_of_tuples = []
   for index, item2 in enumerate(iterable_2):
     list_of_tuples.append( (iterable_1[index], item2) )

   return list_of_tuples
"""