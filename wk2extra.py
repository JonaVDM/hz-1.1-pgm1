#
# Strings
#
def hello_name(name):
    return 'Hello ' + name + '!'


def make_abba(a, b):
    return a + b + b + a


def make_tags(tag, word):
    return '<%s>%s</%s>' % (tag, word, tag)


def make_out_word(out, word):
    return out[:2] + word + out[2:]


def extra_end(str):
    return 3 * str[-2:]


def first_two(str):
    return str[:2]


def first_half(str):
    c = len(str) // 2
    return str[:c]


def without_end(str):
    return str[1:-1]


def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    return a + b + a


def non_start(a, b):
    return a[1:] + b[1:]


def left2(str):
    return str[2:] + str[:2]

#
# Lists
#


def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


def same_first_last(nums):
    if len(nums) == 0:
        return False
    return nums[0] == nums[-1]


def make_pi():
    return [3, 1, 4]


def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


def sum3(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    return total


def rotate_left3(nums):
    return nums[1:] + nums[:1]


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    if nums[0] > nums[2]:
        nums[1] = nums[2] = nums[0]
    else:
        nums[1] = nums[0] = nums[2]

    return nums


def sum2(nums):
    return sum(nums[:2])


def middle_way(a, b):
    return [a[1], b[1]]


def make_ends(nums):
    return [nums[0], nums[-1]]


def has23(nums):
    return 2 in nums or 3 in nums
