"""
    Tuples are immutable, heavily restricted list
    Thus, meaning that tuples have fixed size in memory.
    Which is great if you want to reduce the memory foot print of a script
    Also used for swapping values around
    We cannot pop or insert item to tuple if it already exists
"""


my_tuple = (1, 2, 3)

my_second_tuple = 1, 2, 3

my_third_tuple = tuple([1, 2, 3])

print(my_third_tuple[1])

dir(tuple)

"""
    Tuple Packing And Unpacking
"""

# Simultaneous assignment
a, b = 1, 2

c = (3, 4)

d, e = c

f = d, e

# We packed d and e into f
f == c

del a
del b

a = 1
b = 2

a, b = b, a


def my_func():
    return 1, 2, 3

x, y, z = my_func()