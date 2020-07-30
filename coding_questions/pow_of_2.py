import itertools
from typing import List


def isPowerOfTwo(n: int) -> bool:
    if n == 1:
        return True
    elif n == 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1


print(isPowerOfTwo(32))
