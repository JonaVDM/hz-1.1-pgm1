def dbl(x):
    """
    Returns twice the argument

    Spam is great, and dbl("spam") is better!

    :param x: The value to double
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 2 * x


def tpl(x):
    """
    Returns thrice the argument

    :param x: The value to triple
    :type x: int, float or string
    :rtype: int, float or string
    """
    return 3 * x


def sq(x):
    """
    Returns the number x squared

    :param x: The value to be squared
    :type x: int, float
    :rtype int, float
    """
    return x ** 2


def interp(low, hi, fraction):
    """
    Returns something

    :param low: The starting point
    :type low: int, float

    :param hi: The end point
    :type hi: int, float

    :param fraction: The fraction
    :type fraction: int, float

    :rtype: float
    """
    return (hi - low) * fraction + low


def checkends(s):
    """
    Checks if the first and last character of a string are the same

    :param s: The string to check
    :type s: string
    :rtype: boolean
    """
    return s[0] == s[-1]


def flipside(s):
    """
    Reverse the two halves of the string

    :param s: The string to reverse
    :type s: string
    :rtype: string
    """
    x = len(s) // 2
    return s[x:] + s[:x]


def convert_from_seconds(s):
    """
    Returns the amount of days, hours, minutes and seconds there are in s

    :param s: the time in seconds
    :type s: int
    :rtype: array
    """
    days = s // (24 * 60 * 60)
    s = s % (24 * 60 * 60)
    hours = s // (60 * 60)
    s = s % (60 * 60)
    minutes = s // 60
    seconds = s % 60
    return [days, hours, minutes, seconds]
