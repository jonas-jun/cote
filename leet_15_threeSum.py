'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

**
when sum, sorting is useful!!
**

https://leetcode.com/problems/3sum/
'''

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    ans = list()
    ans_set = set()
    nums = sorted(nums)
    for i in range(len(nums)-2):
        left, right = i+1, len(nums)-1
        while left < right:
            sum_ = nums[i] + nums[left] + nums[right]
            if (sum_ == 0) and (nums[i], nums[left], nums[right]) not in ans_set:
                ans.append([nums[i], nums[left], nums[right]])
                ans_set.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum_ < 0:
                left += 1
            else:
                right -= 1
    return ans

# test
t1 = [-1, 0, 1, 2, -1, 4]
t2 = [0]

from time_check import check
print(check(threeSum, t1))
print(check(threeSum, t2))

# for insert mode