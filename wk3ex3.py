# Programmeren I, Week 3 Opgave 3
# Bestandsnaam: wk3ex3.py
# Naam:
# Probleemomschrijving: List comprehensions


# hiermee krijgen we functies als sin en cos...
from math import *


# twee extra functies (die niet in de module math hierboven zitten)


def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2 * x


def sq(x):
    """Squarer!  argument: x, a number"""
    return x ** 2


# voorbeelden om aan list comprehensions te wennen...


def lc_mult(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each multiplied by 2**
    """
    return [2 * x for x in range(n)]


def lc_idiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x // 2) for x in range(n)]


def lc_fdiv(n):
    """This example accepts an integer n
       and returns a list of integers
       from 0 to n-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x / 2 for x in range(n)]


assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]


def unitfracs(n):
    """ Return the fractions between 0 and 1
        with the divider n
    """
    return [x / n for x in range(n)]


assert unitfracs(4) == [0.0, 0.25, 0.5, 0.75]
assert unitfracs(10) == [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
assert unitfracs(2) == [0.0, 0.5]


def scaledfracs(low, hi, n):
    """ Get the the fraction n between low and hi
    """
    return [(hi - low) * (x / n) + low for x in range(n)]


assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25,
                                  41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]


def sqfracs(low, hi, n):
    """ Get the fractions n between low and hi. Again,
        but this time it is going to be squared!
    """
    return [((hi - low) * (x / n) + low) ** 2 for x in range(n)]


assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]
assert sqfracs(10, 20, 10) == [100.0, 121.0, 144.0,
                               169.0, 196.0, 225.0, 256.0, 289.0, 324.0, 361.0]


def f_of_fracs(f, low, hi, n):
    """ Execute function f on the fractions between
        low and hi. With n being the amount of steps
    """
    return [f((hi - low) * (x / n) + low) for x in range(n)]


assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0]


def integrate(f, low, hi, n):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where n steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of n uniform steps
       from low to hi
    """
    scale = scaledfracs(low, hi, n)[1]
    frac = sum(f_of_fracs(f, low, hi, n))
    return scale * frac


assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

""" Vraag 1

    Omdat het nooit een perfecte rechte lijn word gaat
    gaat het er altijd een beetje onder zitten.
"""

""" Vraag 2

    Hoe dichterbij n naar infinity gaat, hoe dichterbij de
    return komt tot het mooie getal PI.

    Bij 200 is het 3.1511769448395297..
    Bij 2000 is het 3.1425795059119643..

    Bij 1000000 3.141594652413976..
    Komt al redelijk dichtbij...
"""
