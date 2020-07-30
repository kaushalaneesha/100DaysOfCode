import itertools
from typing import List


def change(amount: int, coins: List[int]) -> int:
    rows, cols = len(coins) + 1, amount + 1
    dp = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(rows):
        dp[i][0] = 1
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j >= coins[i - 1] else 0)
    return dp[rows - 1][amount]


print(change(5, [1, 2, 5]))
