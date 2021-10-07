# Programmeren I, week 3 opgave 2
# Bestandsnaam: wk3ex2.py
# Naam: Jonathan van der Meulen
# Probleemomschrijving: Slaapwandelende student

import random
import sys
import time

sys.setrecursionlimit(50000)


def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
    """
    random.seed()
    return random.choice([-1, 1])


def rwpos(start, nstep):
    """ rwpos set's steps in random directions rs() until the counter runs out
        arguments:
        start = The start position of the student
        nstep = the amount of steps to take
    """
    if nstep == 0:
        return start
    return rwpos(start + rs(), nstep - 1)


def rwsteps(start, low, hi):
    """ Make the student take steps until he/she/it hits a wall. Can take quite
        some time though

        Arguments:
        start = The start position of the student in the room
        low = Position of one of the walls
        hi = The position of the other one
    """
    if start > hi or start < low:
        return 0

    line = ' ' * (start - low) + 's'
    print(line)
    time.sleep(0.1)
    return 1 + rwsteps(start + rs(), low, hi)


def rwpos_plain(start, nstep):
    """ rwpos_plain set's steps in random directions rs() until the counter
        runs out.
        arguments:
        start = The start position of the student
        nstep = the amount of steps to take
    """
    if nstep == 0:
        return start
    return rwpos_plain(start + rs(), nstep - 1)


def ave_signed_displacement(numtrials):
    """ Get back the average deviation for rwpos_plain.
        Arguments:
        numtrials = amount of times to make the student run drunk.
    """
    runs = [rwpos_plain(0, 100) for _ in range(numtrials)]
    return sum(runs) / len(runs)


def ave_squared_displacement(numtrials):
    """ Basically the same thing as above, but this time squaring it for some
        reason. Nope I can't see why this is useful either.
        Arguments:
        numtrials = amount of times to make the student run drunk.
    """
    runs = [rwpos_plain(0, 100)**2 for _ in range(numtrials)]
    print(runs)
    return sum(runs) / len(runs)


"""
    Om de gemiddelde totale afwijking voor een
    toevalsbeweging met 100 willekeurige stappen
    te berekenen, heb ik ...

    simpel gezegd de functie x keer aangeroepen,
    in een lijst gestopt en daarvan het gemiddelde
    gepakt door het totaal van de lijst te delen
    met de lengte ervan. Tot absoluut niemand hun
    schok was de conclusie dat alle resultaten
    (die een redelijke sample size hebben) uit
    kwamen rond de 0. Wat ook het gemiddelde is
    van -1 en 1.

    Een paar voorbeelden:
    In [9]: ave_signed_displacement(100)
    Out[9]: 0.32

    In [10]: ave_signed_displacement(100)
    Out[10]: -0.64

    In [11]: ave_signed_displacement(100)
    Out[11]: 0.0

    In [12]: ave_signed_displacement(100)
    Out[12]: -0.58

    In [13]: ave_signed_displacement(1000)
    Out[13]: -0.202

    Op de squared heb ik hetzelfde gedaan, maar
    dan met rwpos_plain(...)**2. Hierbij kwam
    het gemiddelde uit rond de 100.
"""
