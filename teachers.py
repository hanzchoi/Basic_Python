# The dictionary will be something like:
# {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Often, it's a good idea to hold onto a max_count variable.
# Update it when you find a teacher with more classes than
# the current count. Better hold onto the teacher name somewhere
# too!
#
# Your code goes below here.


"""
    write a function named courses that takes the teachers dictionary.
    It should return a single list of all of the courses offered by all of the teachers.
"""
"""
    Great work! Finally, write a function named courses that takes the teachers dictionary.
    It should return a single list of all of the courses offered by all of the teachers.
"""


def courses(teachers_dict):
    course_list = []
    for classes in teachers_dict.values():  # gets a **list** contain teachers courses.
        # extends courseList the contents of your [] list. which is a single item: the teachers course list
        course_list.extend([classes])  # <-- fix by removing "[" and "]" from around `classes`
    return course_list

"""
    Create a function named most_classes that takes a dictionary of teachers.
    Each key is a teacher's name and their value is a list of classes they've taught.
    most_classes should return the teacher with the most classes.
"""


def most_classes(teachers):
    max_count = 0
    popular_teacher = ''

    for key in teachers:
        if max_count < len(teachers[key]):
            max_count = len(teachers[key])
            popular_teacher = key

    return popular_teacher


"""
    Next, create a function named num_teachers that takes the same dictionary of teachers and classes.
    Return the total number of teachers.

"""


def num_teachers(teachers):
    busy_teacher = 0
    for key in teachers.keys():
        busy_teacher += 1

    return busy_teacher

"""
    Now, create a function named stats that takes the teacher dictionary.
    Return a list of lists in the format [<teacher name>, <number of classes>].
    For example, one item in the list would be ['Dave McFarland', 1].

"""


def stats(dict):
    new_list = []

    for k, v in dict.items():
        new_string = [k, int(len(v))]
        new_list.append(new_string)

    return new_list




teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}

print(courses(teachers))