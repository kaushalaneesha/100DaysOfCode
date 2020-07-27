#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the caesar cipher function below.
def caesarCipher(s, k):
    new_str = [''] * len(s)
    for i, ch in enumerate(s):
        ord_s = ord(ch)
        if is_alphabet(ord_s):
            pos = ord_s + k % 26
            if (upper_alpha(ord_s) and pos > 90) or (lower_alpha(ord_s) and pos > 122):
                pos -= 26
            new_str[i] = chr(pos)
        else:
            new_str[i] = ch
    return ''.join(new_str)


def is_alphabet(pos):
    return upper_alpha(pos) or lower_alpha(pos)


def upper_alpha(pos):
    return 65 <= pos <= 90


def lower_alpha(pos):
    return 97 <= pos <= 122


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')

    # fptr.close()
