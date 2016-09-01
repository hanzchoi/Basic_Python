# Make a list to hold our items
shopping_list = []


def show_help():
    # print out instructions how to use the app
    print("What should we pick up the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' or this help.
Enter 'SHOW' to ee your current list.

    """)


def show_list():

    # print out the list
    print("Here's your list")

    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List no has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
    # ask for new items
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()

