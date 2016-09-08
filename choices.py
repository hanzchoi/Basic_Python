"""
    Create a function named nchoices() that takes an iterable and an integer.
    The function should return a list of n random items from the iterable where n is the integer.
    Duplicates are allowed.
"""
import random


def nchoice(some_list, num):
    rand_list = []

    for x in range(0, num):
        rand_list.append(random.choice(some_list))

    return rand_list