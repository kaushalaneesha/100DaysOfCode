"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
from typing import List


def largest_divisible_subset(nums: List[int]) -> List[int]:
    # Sort numbers
    nums.sort()

    # Find the length of max subset
    len_nums = len(nums)
    dp = [1] * len_nums
    max_len = 1
    for i in range(1, len_nums):
        j, curr_max = 0, 1
        while j < i:
            if nums[i] % nums[j] == 0 and dp[j] + 1 > curr_max:
                curr_max = dp[j] + 1
                # print(j)
            j += 1
        # print(curr_max)
        dp[i] = curr_max
        if curr_max > max_len:
            max_len = curr_max
        # print(dp)
    prev = -1
    res = set()
    for i in range(len_nums - 1, -1, -1):
        if dp[i] == max_len and (prev < 0 or prev % nums[i] == 0):
            res.add(nums[i])
            max_len -= 1
            prev = nums[i]
    return res
