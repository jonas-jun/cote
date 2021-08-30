'''
A peak element is an element that is strictly greater than its neighbors.
peak element를 찾아서 index를 return. 양 끝은 -inf라 생각하고, time_complexity는 O(logn)으로 찾아라.

Solution
binary search로 찾아야 하고
양끝에 -inf를 붙여주면 좋다.

https://leetcode.com/problems/find-peak-element
'''

from typing import List
def findPeakElement(nums: List[int]) -> int:
    nums = [-float('inf')] + nums + [-float('inf')]
    ans = list()
    def helper(s,e):
        nonlocal nums, ans
        if ans: return # 하나라도 찾아져 있으면 return 해버림.
        if s>e: return
        mid_idx = (s+e)//2
        if mid_idx == -1: return
        if mid_idx == len(nums)-1: return
        
        if nums[mid_idx-1] < nums[mid_idx] and nums[mid_idx] > nums[mid_idx+1]:
            ans.append(mid_idx)
            return
        else:
            helper(s, mid_idx-1)
            helper(mid_idx+1, e)
    
    helper(0, len(nums)-1)
    return ans[0]-1

# for test
print(findPeakElement([1,2,3,1]))
print(findPeakElement([1,2,1,3,5,6,4]))