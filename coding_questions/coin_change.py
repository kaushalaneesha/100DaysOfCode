import itertools
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    if amount == 0:
        return 0
    coins.sort()
    coin_count = [0] * (amount + 1)
    for i in range(1, amount + 1):
        prev_count = [coin_count[i - coin] for coin in itertools.takewhile(lambda x: i >= x, coins) if coin_count[i - coin] >= 0]
        if not prev_count:
            coin_count[i] = -1
        else:
            coin_count[i] = min(prev_count) + 1
    return coin_count[amount]


print(coinChange([186, 419, 83, 408], 6249))
