dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(dicts, string):
    temp_list = []
    for sentence in dicts:
        temp_list.append(string.format(**sentence))

    return temp_list



print(string_factory(dicts, string))