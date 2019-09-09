import math


def comparison_small(num):
    """小于比较"""

    print("这是一个小于")


def comparison_big(num):
    """大于比较"""

    num = int(num)
    num_one = num//100
    num_two = num%100//10
    num_three = num%100%10
    print("百位是{}".format(num_one))
    print("十位是{}".format(num_two))
    print("个位是{}".format(num_three))
    # return num_one
