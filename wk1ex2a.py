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

    # Options is a list with what a weapon beats, for example paper beats stone
    options = {
        'steen': ['schaar', 'hagedis'],
        'papier': ['steen', 'spock'],
        'schaar': ['papier', 'hagedis'],
        'spock': ['steen', 'schaar'],
        'hagedis': ['papier', 'spock'],
    }

    # Loop through the program until the user exit it
    while True:
        _run(options)

        # Check if the user wants the exit the program
        again = input('Nog een keer spelen? [Yn] ')
        if again not in ['y', 'Y', '']:
            break
    print('Was leuk gespeeld te hebben 👋')


# Splitting of the repeating part of the function to make it look nicer
def _run(options):
    random.seed()

    # Get the options from the list with weapons
    user = input(f'Kies je wapen {", ".join(options.keys())}: ')
    comp = random.choice(list(options.keys()))

    print(f'\nJij koos {user}')
    print(f'Ik koos {comp}')

    # Check if the user gave a right answer
    if user not in options.keys():
        print(f'Ik herken {user} niet, dus ik neem deze win ;)')

    # If the user and the computer played the same thing
    elif user == comp:
        print(f'Wij hebben beide {comp} gekozen, dus het is gelijk')

    # Check if the user picked something that the computer beats
    elif user in options[comp]:
        print('Ha ik heb gewonnen >:D')

    # Otherwise the user wins
    else:
        print('Jij hebt gewonnen :(')
