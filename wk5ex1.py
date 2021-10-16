def is_odd(n: int) -> bool:
    return n % 2 == 1


assert is_odd(42) == False
assert is_odd(43) == True


def num_to_binary(n: int) -> str:
    """ Convert a number into a binary string
    """
    if n == 0:
        return ''

    if n % 2 == 1:
        return num_to_binary(n // 2) + '1'

    return num_to_binary(n // 2) + '0'


assert num_to_binary(0) == ""
assert num_to_binary(42) == "101010"


def binary_to_num(s: str) -> int:
    """ Convert a string of bits into
        a number
    """
    if s == '':
        return 0

    if s[0] == '1':
        return binary_to_num(s[1:]) + 2 ** (len(s) - 1)

    return binary_to_num(s[1:])


assert binary_to_num('') == 0
assert binary_to_num('101010') == 42
assert binary_to_num("00001011") == 11
assert binary_to_num("1100100") == 100


def increment(s: str) -> str:
    """ Takes in a string of bits and returns
        it again but added 1
    """
    n = binary_to_num(s)
    b = num_to_binary(n + 1)
    if len(b) > 8:
        b = ''
    return (8 - len(b)) * '0' + b


assert increment("00000000") == '00000001'
assert increment("00000001") == '00000010'
assert increment("00000111") == '00001000'
assert increment("11111111") == '00000000'


def count(s: str, n: int) -> None:
    """ Count the string s up n times.
        You know that a for i loop makes
        way more sense here right?
    """
    print(s)

    if n == 0:
        return

    return count(increment(s), n - 1)


"""
Het getal 59 komt uit op 2012
Als we dit gaan uitrekenen volgens de enige manier
die ik ken komt het uit op:

59 / 3 = 19 rest 2
19 / 3 = 6  rest 1
6  / 3 = 2  rest 0
2  / 3 = 0  rest 2

En als we de resten bij elkaar voegen komen we op 2012 uit

Een control ronde
2 keer 3 tot de macht 3 = 2 * 27 = 54
0 keer 2 tot de macht 3 = 0 * 9  = 0
1 keer 1 tot de macht 3 = 1 * 3  = 3
2 keer 0 tot de macht 3 = 2 * 1  = 2

54 + 0 + 3 + 2 = 59
"""


def num_to_ternary(n: int) -> str:
    """ Transform a number into a
        ternary
    """
    if n == 0:
        return ''

    if n % 3 == 2:
        return num_to_ternary(n // 3) + '2'

    if n % 3 == 1:
        return num_to_ternary(n // 3) + '1'

    return num_to_ternary(n // 3) + '0'


assert num_to_ternary(42) == '1120'
assert num_to_ternary(4242) == '12211010'
assert num_to_ternary(59) == '2012'


def ternary_to_num(s: str) -> int:
    """ Convert a string of bits into
        a number
    """
    if s == '':
        return 0

    if s[0] == '2':
        return ternary_to_num(s[1:]) + 2 * 3 ** (len(s) - 1)

    if s[0] == '1':
        return ternary_to_num(s[1:]) + 3 ** (len(s) - 1)

    return ternary_to_num(s[1:])


assert ternary_to_num('1120') == 42
assert ternary_to_num('12211010') == 4242
assert ternary_to_num('2012') == 59


def balanced_ternary_to_num(s: str) -> int:
    """ Convert a string of balanced ternary
        into a normal number.
    """
    if s == '':
        return 0

    if s[0] == '-':
        return balanced_ternary_to_num(s[1:]) + -1 * 3 ** (len(s) - 1)

    if s[0] == '+':
        return balanced_ternary_to_num(s[1:]) + 3 ** (len(s) - 1)

    return balanced_ternary_to_num(s[1:])


assert balanced_ternary_to_num('+---0') == 42
assert balanced_ternary_to_num('++-0+') == 100


def num_to_balanced_ternary(n: int) -> str:
    """ Transform a number into a
        balanced ternary! Wait what?
    """
    if n == 0:
        return ''

    if n % 3 == 2:
        return num_to_balanced_ternary(n // 3 + 1) + '-'

    if n % 3 == 1:
        return num_to_balanced_ternary(n // 3) + '+'

    return num_to_balanced_ternary(n // 3) + '0'


assert num_to_balanced_ternary(42) == '+---0'
assert num_to_balanced_ternary(100) == '++-0+'
