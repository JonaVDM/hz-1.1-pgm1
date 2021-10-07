# Programmeren I, Week 2 Opgave 3
# Bestandsnaam: wk2ex3.py
# Naam:
# Problemomschrijving: Feest met functies!

def mult(n, m):
    """
    Multiply two numbers using recursion

    :param n: The first number
    :type n: int

    :param m: The second number
    :type m: int

    :rtype: int
    """
    if n == 0 or m == 0:
        return 0

    if m < 0:
        return -n + mult(n, m + 1)

    return n + mult(n, m - 1)


# Tests for the mult function
assert mult(6, 7) == 42
assert mult(6, -7) == -42
assert mult(-6, 7) == -42
assert mult(-6, -7) == 42
assert mult(6, 0) == 0
assert mult(0, 7) == 0
assert mult(0, 0) == 0


def dot(l, k):
    """
    Calculate the dot product of two arrays

    :param l: The first list
    :type l: list

    :param l: The second
    :type l: list

    :rtype: float
    """
    if len(l) != len(k) or len(l) == 0:
        return 0.0

    return l[0] * k[0] + dot(l[1:], k[1:])


# Tests for the dot function
assert dot([5, 3], [6, 4]) == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6]) == 0.0
assert dot([], [6]) == 0.0
assert dot([], []) == 0.0


def ind(e, l):
    """
    find the index of e in l

    returns the length of the list/string when no match is found

    :param e: The item to be found
    :type e: any

    :param l: The list or to find the item in
    :type l: list or string

    :rtype: int
    """
    if len(l) == 0 or e == l[0]:
        return 0

    return 1 + ind(e, l[1:])


# Tests for the ind function
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100))) == 42
assert ind("hoi", ["hallo", 42, True]) == 3
assert ind("hoi", ["oh", "hoi", "daar"]) == 1
assert ind("i", "team") == 4
assert ind(" ", "nader onderzoek") == 5


def letter_score(let):
    """
    Get the score that represents the leter

    :param let: The letter
    :type let: string

    :rtype: int
    """
    if let in 'adeinorst':
        return 1

    if let in 'ghl':
        return 2

    if let in 'bcmp':
        return 3

    if let in 'jkuvw':
        return 4

    if let in 'f':
        return 5

    if let in 'z':
        return 6

    if let in 'xy':
        return 8

    if let in 'q':
        return 10

    return 0


def scrabble_score(s):
    """
    Get the scrabble score of a string

    :param s: The string to calculate
    :type s: string

    :rtype: int
    """
    if len(s) == 0:
        return 0

    return letter_score(s[0]) + scrabble_score(s[1:])


# Tests for the scrabble score, boring game gotta say
assert scrabble_score("quotums") == 24
assert scrabble_score("jacquet") == 24
assert scrabble_score("pyjama") == 20
assert scrabble_score("abcdefghijklmnopqrstuvwxyz") == 84
assert scrabble_score("?!@#$%^&*()") == 0
assert scrabble_score("") == 0


def one_dna_to_rna(c):
    """
    Conver a DNA nucleotide to a RNA nucleotide

    :param c: The dna to convert
    :type c: string

    :rtype: string
    """
    if c == 'A':
        return 'U'

    if c == 'C':
        return 'G'

    if c == 'G':
        return 'C'

    if c == 'T':
        return 'A'

    return ''


def transcribe(s):
    """
    Transribe DNA into RNA

    :param s: the dna to transribe
    :type s: string

    :rtype: string
    """
    if len(s) == 0:
        return ''

    return one_dna_to_rna(s[0]) + transcribe(s[1:])


# Tests for the transcribe function
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU'  # De spatie verdwijnt
assert transcribe('GATTACA') == 'CUAAUGU'
assert transcribe('hanze') == ''         # Andere tekens verdwijnen
assert transcribe('') == ''


#
# Ik heb alle STRING-opgaven van CodingBat gemaakt.
#

#
# Ik heb alle LIJST-opgaven van CodingBat gemaakt.
#

# If you guys wanna confirm it:
# https://github.com/JonaVDM/hz-1.1-pgm1/blob/main/wk2extra.py

def piglet_latin(s):
    """
    Convert a word into a weak version of pig latin
    :param s: The string to convert
    :type s: string
    :rtype: string
    """
    if s == '':
        return ''

    if s[0] in 'aeiou':
        return s + 'hee'

    return s[1:] + s[0] + 'ee'


assert piglet_latin('aap') == 'aaphee'
assert piglet_latin('straat') == 'traatsee'
assert piglet_latin('noot') == 'ootnee'


def starts_with_vowel(s):
    """
    Check if letter is a vowel

    :param s: The letter to check
    :type s: string

    :rtype: boolean
    """
    if len(s) == 0:
        return False

    # Makig sure that only one letter is picked in case of a longer string
    return s[0] in 'aeiou'


def move_non_vowel(s):
    """
    move the first letter to the end as long as it isn't a vowel

    :param s: string to conver
    :type s: string

    :rtype: string
    """
    if starts_with_vowel(s):
        return s

    return move_non_vowel(s[1:] + s[0])


def pig_latin(s):
    """
    Convert a word into pig latin

    :param s: the word to convert
    :type s: string

    :rtype: string
    """
    # starts_with_y = s[0] == 'y'
    if s[0] == 'y' and not starts_with_vowel(s[1]):
        return s + 'hee'

    # Check if it starts with a vowel
    if starts_with_vowel(s):
        return s + 'hee'

    return move_non_vowel(s) + 'ee'


assert(pig_latin('veel')) == 'eelvee'
assert(pig_latin('yoghurt')) == 'oghurtyee'
assert(pig_latin('ypsilon')) == 'ypsilonhee'
assert(pig_latin('straat')) == 'aatstree'
assert(pig_latin('jonathan')) == 'onathanjee'
assert(pig_latin('hanze')) == 'anzehee'
assert(pig_latin('groningen')) == 'oningengree'
