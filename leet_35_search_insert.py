'''
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity. (Binary Search!!)

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

PSEUDO
use binary search and recursion
def helper(nums, target, start, end):
    target > nums[end]: return end+1
    target < nums[start]: return start

    mid = (start+end) // 2
    if target == nums[mid]: return mid
    elif target < nums[mid]: helper(start, mid)
    else: helper(mid, end)
helper(nums, target, 0, len(nums)-1)
'''

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    def helper(nums, target, start, end):
        if target > nums[end]: return end+1
        if target < nums[start]: return start
        mid = (start+end) // 2
        if target == nums[mid]: return mid
        elif target < nums[mid]:
            ans = helper(nums, target, start, mid)
        else:
            ans = helper(nums, target, mid+1, end)
        return ans
    return helper(nums, target, 0, len(nums)-1)

# for test
nums = [1,3,5,6]
print(searchInsert(nums, 5))
print(searchInsert(nums, 2))
print(searchInsert(nums, 7))
print(searchInsert(nums, 0))

# for insert mode