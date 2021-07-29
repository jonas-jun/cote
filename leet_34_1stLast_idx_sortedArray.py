'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

PSEUDO
Bianry Search로 접근 (O(n)을 위해서)
sol1: BS로 target_idx를 하나 찾은 다음 앞뒤로 같은 값이 나오는 부분까지 search하기
sol2: BS로 left, right idx를 찾음
    left: 가장 앞 target_idx
    right: 가장 뒤 target_idx

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
'''

def sol_1(nums, target):
    if not nums: return [-1, -1]

    def bs(list1, start, end, target):
        if start > end: return -1
        if start == end and list1[start] == target:
            return start
        mid = (start + end+1)//2
        if list1[mid] == target: return mid
        elif list1[mid] > target:
            return bs(list1, start, mid-1, target)
        else:
            return bs(list1, mid+1, end, target)
    
    target_idx = bs(nums, 0, len(nums)-1, target)
    if target_idx == -1: return [-1, -1]

    left, right = target_idx, target_idx
    while right < len(nums):
        if nums[right] != target:
            break
        right += 1
    while left >= 0:
        if nums[left] != target:
            break
        left -= 1
    return [left+1, right-1]


def sol_2(nums, target):
    l, r = 0, len(nums)-1
    first = last = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            first = m
            r = m-1
        elif nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1

    l, r = 0, len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            last = m
            l = m+1
        elif nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
    return [first, last]

# for test
t1 = [5,7,7,8,8,10,14,15,15,16,18,20]
from time_check import check
print('case 1')
print(check(sol_1, t1, 8))
print(check(sol_2, t1, 8))

print('case 2')
print(check(sol_1, t1, 17))
print(check(sol_2, t1, 17))

# for insert mode