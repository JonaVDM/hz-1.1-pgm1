#
# wk1ex2a.py
#

import random


def rps():
    """ this plays a game of rock-paper-scissors in Dutch ("steen"-"papier"-"schaar")
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """

    print('Welkom bij een leuk spel steen papier schaar')

    # Options is a list with what a wapon beats, for example paper beats stone
    options = {
        'steen': ['schaar', 'hagedis'],
        'papier': ['steen', 'spock'],
        'schaar': ['papier', 'hagedis'],
        'spock': ['steen', 'schaar'],
        'hagedis': ['papier', 'spock'],
    }

    while True:
        _run(options)
        again = input('Nog een keer spelen? [Yn] ')
        if again not in ['y', 'Y', '']:
            break


def _run(options):
    random.seed()

    user = input(f'Kies je wapen {", ".join(options.keys())}: ')
    comp = random.choice(list(options.keys()))

    print(f'\nJij koos {user}')
    print(f'Ik koos {comp}')

    if user not in options.keys():
        print(f'Ik herken {user} niet, dus ik neem deze win ;)')
    elif user == comp:
        print(f'Wij hebben bijde {comp} gekozen, dus het is gelijk')
    elif user in options[comp]:
        print(f'Ha ik heb gewonnen')
    else:
        print(f'Jij hebt gewonnen :(')
