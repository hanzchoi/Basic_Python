"""
    Enumerate gives you back the current step
    at the loop and the value at that step

    Enumerate gives us back a series of tuples which has a loop step
"""

my_alphabet_list = list('abcdefghijklmnopqrstuvwxyz')


count = 0
for letter in my_alphabet_list():
    print('{} : {}'.format(count, letter))
    count += 1

help(enumerate)


for index, letter in enumerate(my_alphabet_list):
    print("{} : {}".format(index, letter))


for step in enumerate(my_alphabet_list):
    print("{} : {}".format(step[0], step[1]))


"""
    A single star takes apart tuples or lists
    and two star takes apart dictionaries
"""

for step in enumerate(my_alphabet_list):
    print("{}: {}".format(*step))


my_dict = {'name': 'Kenneth', 'job': 'teacher', 'employer':'Treehouse'}

for key, value in my_dict.items():
    print("{}: {}".format(key.title(), value))


