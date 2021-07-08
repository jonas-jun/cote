'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Pseudo Code
1. sorting
2. for first in range(len(nums)-2):
3. second, third -> the biggest combi. (len(nums)-2, len(nums-1))
    if sum < target: check and substitute & continue (not check this first!)
4. second, third = first + 1, len(nums)-1. check from each side
'''

from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    nums = sorted(nums)
    ans = int()
    distance = float('inf')

    def check_and_sub(nums, first, second, third, target, ans, distance):
        sum1 = nums[first] + nums[second] + nums[third]
        if abs(sum1 - target) < distance:
            ans = sum1
            distance = abs(sum1 - target)
            return ans, distance
        return ans, distance

    for fst in range(len(nums)-2):
        if nums[fst] + nums[len(nums)-2] + nums[len(nums)-1] < target:
            ans, distance = check_and_sub(nums, fst, len(nums)-2, len(nums)-1, target, ans, distance)
            continue
        scd, thd = fst+1, len(nums)-1
        while scd < thd:
            sum2 = nums[fst] + nums[scd] + nums[thd]
            if sum2 == target:
                return target
            ans, distance = check_and_sub(nums, fst, scd, thd, target, ans, distance)
            if sum2 < target:
                scd += 1
            else:
                thd -= 1

    return ans

# test
t1 = [3, 5, 11, -3, 7, 1, -2]
t1_target = 5
t2 = [-1, 2, 1, -4]
t2_target = 1

from time_check import check
print(check(threeSumClosest, t1, t1_target))
print(check(threeSumClosest, t2, t2_target))

# for insert mode