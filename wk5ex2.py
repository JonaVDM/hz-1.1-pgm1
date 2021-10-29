def num_to_base_b(n: int, b: int) -> str:
    """ Convert a number (base10) into a base
        of choice.
    """
    if n == 0:
        return ''

    return num_to_base_b(n // b, b) + str(n % b)


assert num_to_base_b(3116, 9) == '4242'
assert num_to_base_b(141474, 8) == '424242'
assert num_to_base_b(42, 8) == '52'
assert num_to_base_b(42, 5) == '132'
assert num_to_base_b(42, 10) == '42'
assert num_to_base_b(42, 2) == '101010'
assert num_to_base_b(4, 2) == '100'
assert num_to_base_b(4, 3) == '11'
assert num_to_base_b(4, 4) == '10'
assert num_to_base_b(0, 4) == ''
assert num_to_base_b(0, 2) == ''


def base_b_to_num(s: str, b: int) -> int:
    """ Convert a number of a base of choice into
        base 10.
    """
    if s == '':
        return 0

    return base_b_to_num(s[1:], b) + int(s[0]) * b ** (len(s) - 1)


assert base_b_to_num("5733", 9) == 4242
assert base_b_to_num("1474462", 8) == 424242
assert base_b_to_num("222", 4) == 42
assert base_b_to_num("101010", 2) == 42
assert base_b_to_num("101010", 3) == 273
assert base_b_to_num("101010", 10) == 101010
assert base_b_to_num("11", 2) == 3
assert base_b_to_num("11", 3) == 4
assert base_b_to_num("11", 10) == 11
assert base_b_to_num("", 10) == 0


def base_to_base(b1: int, b2: int, s_in_b1: str) -> str:
    return num_to_base_b(base_b_to_num(s_in_b1, b1), b2)


assert base_to_base(2, 10, "11") == '3'
assert base_to_base(10, 2, "3") == '11'
assert base_to_base(3, 5, "11") == '4'
assert base_to_base(2, 3, "101010") == '1120'
assert base_b_to_num("1120", 3) == 42
assert base_to_base(2, 4, "101010") == '222'
assert base_to_base(2, 10, "101010") == '42'
assert base_to_base(5, 2, "4321") == '1001001010'
assert base_to_base(2, 5, "1001001010") == '4321'


def add(s, t):
    """ Add two binary numbers together
        but not using binary numbers to
        add them together...
    """
    return num_to_base_b(base_b_to_num(s, 2) + base_b_to_num(t, 2), 2)


assert add("11", "1") == '100'
assert add("11", "100") == '111'
assert add("110", "11") == '1001'
assert add("11100", "11110") == '111010'
assert add("10101", "10101") == '101010'


def add_b(s: str, t: str) -> str:
    """ Add two binary numbers together!
    """
    if len(s) == 0:
        return t
    elif len(t) == 0:
        return s

    if s[-1] == "0" and t[-1] == "0":
        return add_b(s[:-1], t[:-1]) + "0"
    elif s[-1] == "0" and t[-1] == "1":
        return add_b(s[:-1], t[:-1]) + "1"
    elif s[-1] == "1" and t[-1] == "0":
        return add_b(s[:-1], t[:-1]) + "1"
    carry = add_b("1", s[:-1])
    return add_b(carry, t[:-1]) + "0"


assert add_b("11", "100") == "111"
assert add_b("11100", "11110") == "111010"
assert add_b("110", "11") == "1001"
assert add_b("110101010", "11111111") == "1010101001"
assert add_b("1", "1") == "10"


def get_pairs(s: str, c: int = 1) -> list:
    """ Get a list of all the pairs in a string

        Returns a list of tuples containing the letter
        with the amount of times it's repeated
    """
    if len(s) == 1:
        return [(s, c)]

    if s[0] != s[1]:
        return [(s[0], c)] + get_pairs(s[1:])

    return get_pairs(s[1:], c=c+1)


def make_seven(b: str) -> str:
    """ Turn a byte of any length into a length of seven,
        given that it is not already longer than seven
    """
    return "0" * (7 - len(b)) + b


def compress(b: str) -> str:
    """ Compress a list of bytes into a slightly smaller
        list of bytes
    """
    p = [s + make_seven(num_to_base_b(c, 2)) for s, c in get_pairs(b)]
    return ''.join(p)


assert compress(64 * "0") == '01000000'
assert compress("11111") == '10000101'
assert compress(("0" * 16 + "1" * 16) *
                2) == '00010000100100000001000010010000'


def uncompress(b: str) -> str:
    """ Uncompress a compressed string
    """
    if b == '':
        return ''

    return b[0] * base_b_to_num(b[1:8], 2) + uncompress(b[8:])


assert uncompress("10000101") == '11111'
assert uncompress(
    "00010000100100000001000010010000") == '0000000000000000111111111111111100000000000000001111111111111111'
assert uncompress('01000000') == 64 * '0'
