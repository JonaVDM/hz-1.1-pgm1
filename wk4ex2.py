def encipher(s: str, n: int) -> str:
    """ Returns the string s with all letters
        changed by adding the number n to it
    """
    if s == '':
        return ''

    return rot(s[0], n) + encipher(s[1:], n)


def rot(c: str, n: int) -> str:
    """ Help function for encipher
        returns the single character of
        the changed string.
    """
    is_lower = 'a' <= c <= 'z'
    is_upper = 'A' <= c <= 'Z'
    l = ord(c)

    if is_lower or is_upper:
        l += n

    if is_lower and l > 122:
        l -= 26

    if is_upper and l > 90:
        l -= 26

    return chr(l)


assert encipher('xyza', 1) == 'yzab'
assert encipher('Z A', 1) == 'A B'
assert encipher('*ab?', 1) == '*bc?'
assert encipher('Dit is een string!', 1) == 'Eju jt ffo tusjoh!'
assert encipher('Caesarcijfer? Ik heb liever Caesarsalade.',
                25) == 'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.'


def decipher(s: str) -> str:
    """ Returns (hopefully) the right
        decoded string.
    """
    # holy fuck just let us use normal for loops, this is getting
    # kinda ridiculous.
    pos = [encipher(s, x) for x in range(26)]
    al = [(sum([letter_prob(y) for y in x]), x) for x in pos]
    return max(al)[1]


def letter_prob(c):
    """If c is an alphabetic character,
       we return its monogram probability (for Dutch),
       otherwise we return 1.0.  We ignore capitalization.
       Adapted from
       https://www.sttmedia.com/characterfrequency-nederlands
    """
    if c == 'e' or c == 'E':
        return 0.1909
    if c == 'n' or c == 'N':
        return 0.0991
    if c == 'a' or c == 'A':
        return 0.0769
    if c == 't' or c == 'T':
        return 0.0642
    if c == 'i' or c == 'I':
        return 0.0630
    if c == 'o' or c == 'O':
        return 0.0581
    if c == 'r' or c == 'R':
        return 0.0562
    if c == 'd' or c == 'D':
        return 0.0541
    if c == 's' or c == 'S':
        return 0.0384
    if c == 'l' or c == 'L':
        return 0.0380
    if c == 'h' or c == 'H':
        return 0.0312
    if c == 'g' or c == 'G':
        return 0.0312
    if c == 'k' or c == 'K':
        return 0.0279
    if c == 'm' or c == 'M':
        return 0.0256
    if c == 'v' or c == 'V':
        return 0.0224
    if c == 'u' or c == 'U':
        return 0.0212
    if c == 'j' or c == 'J':
        return 0.0182
    if c == 'w' or c == 'W':
        return 0.0172
    if c == 'z' or c == 'Z':
        return 0.0160
    if c == 'p' or c == 'P':
        return 0.0149
    if c == 'b' or c == 'B':
        return 0.0136
    if c == 'c' or c == 'C':
        return 0.0130
    if c == 'f' or c == 'F':
        return 0.0073
    if c == 'y' or c == 'Y':
        return 0.0006
    if c == 'x' or c == 'X':
        return 0.0005
    if c == 'q' or c == 'Q':
        return 0.0001
    return 1.0


assert decipher(
    'Bzdrzqbhiedq? Hj gda khdudq Bzdrzqrzkzcd.') == 'Caesarcijfer? Ik heb liever Caesarsalade.'
assert decipher(
    'Aadxas ue exqotfe pq haadflqffuzs hmz baxufuqw yqf mzpqdq yuppqxqz.') == 'Oorlog is slechts de voortzetting van politiek met andere middelen.'


def blsort(l: list) -> list:
    """ Sort zeros and ones. But without actually
        sorting it, for some reason
    """
    a1 = sum([1 for x in l if x == 1])
    a2 = len(l) - a1
    return [0] * a2 + [1] * a1


assert blsort([1, 0, 1]) == [0, 1, 1]
assert blsort([1, 0, 1, 0, 1, 0, 1]) == [0, 0, 0, 1, 1, 1, 1]


def rem_one(e, L):
    """Returns sequence L with one e removed
    """
    if len(L) == 0:
        return L
    if L[0] != e:
        return L[0:1] + rem_one(e, L[1:])
    return L[1:]


def gensort(l: list) -> list:
    """ A simple sort function, using recursing
        for some weird reason.
    """
    if len(l) == 0:
        return l
    x = min(l)
    return [x] + gensort(rem_one(x, l))


assert gensort([42, 1, 3.14]) == [1, 3.14, 42]
assert gensort([7, 9, 4, 3, 0, 5, 2, 6, 1, 8]) == [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def lingo(s: str, t: str) -> int:
    """ Get the lingo score between two
        words
    """
    if s == '' or t == '':
        return 0

    if s[0] in t:
        return 1 + lingo(s[1:], rem_one(s[0], t))
    return lingo(s[1:], t)


assert lingo('diner', 'proza') == 1
assert lingo('beeft', 'euvel') == 2
assert lingo('gattaca', 'aggtccaggcgc') == 5
assert lingo('gattaca', '') == 0


def exact_change(target_amount: int, l: list) -> bool:
    """ Calculate if we can get the number target
        with some of the items in the list.
    """
    if (target_amount == 0):
        return True

    if l == []:
        return False

    ui = exact_change(target_amount-l[0], l[1:])
    li = exact_change(target_amount, l[1:])

    return ui or li


assert exact_change(42, [25, 1, 25, 10, 5, 1]) == True
assert exact_change(42, [25, 1, 25, 10, 5]) == False
assert exact_change(42, [23, 1, 23, 100]) == False
assert exact_change(42, [23, 17, 2, 100]) == True
assert exact_change(42, [25, 16, 2, 15]) == True
assert exact_change(0, [4, 5, 6]) == True
assert exact_change(-47, [4, 5, 6]) == False
assert exact_change(0, []) == True
assert exact_change(42, []) == False


def lcs(s: str, t: str) -> str:
    """ Find the longest common subsequence
        between strings s and t. using recursing
        obviously.
    """
    if s == '' or t == '':
        return ''

    if s[0] == t[0]:
        return s[0] + lcs(s[1:], t[1:])

    l1 = lcs(s[1:], t)
    l2 = lcs(s, t[1:])

    if len(l1) > len(l2):
        return l1
    return l2


assert lcs('mens', 'chimpansee') == 'mns'
assert lcs('gattaca', 'tacgaacta') == 'gaaca'
assert lcs('wow', 'wauw') == 'ww'
assert lcs('', 'wauw') == ''
assert lcs('abcdefgh', 'efghabcd') == 'abcd'
