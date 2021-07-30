'''
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Input: nums = [3,2,1,0,4]
Output: false

PSEUDO
sol 1
cur_max update: max(cur_max, i+nums[i])
sol 2: Dynamic Programing
dp[i]: cur_max
dp[i+1] = max(dp[i], i+1+nums[i+1])

https://leetcode.com/problems/jump-game
'''

from typing import List

def sol_1(nums: List[int]) -> bool:
    max_idx = 0
    i = 0
    while i < len(nums):
        max_idx = max(max_idx, i+nums[i])
        if max_idx >= len(nums)-1: return True
        i += 1
        if i > max_idx: return False

def sol_2(nums) -> bool:
    length = len(nums)
    dp = [0 for _ in range(length)]
    dp[0] = nums[0]

    for i in range(1, length):
        if i > dp[i-1]: return False
        dp[i] = max(dp[i-1], i+nums[i])
        if dp[i] >= length-1: return True

# for test
from time_check import check
t1 = [2,3,1,1,4,1,5,2,0,3,4,1,2,3,0,0,3,4,2,1,1]
t2 = [3,2,1,0,4]
print('case 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('case 2')
print(check(sol_1, t2))
print(check(sol_2, t2))

# for insert mode