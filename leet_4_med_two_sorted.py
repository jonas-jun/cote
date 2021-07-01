'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

ex1
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

https://leetcode.com/problems/median-of-two-sorted-arrays/
'''

from typing import List

def merge(l1, l2):
    merged = list()
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
        else:
            merged.append(l2[j])
            j += 1
    while i < len(l1):
        merged.append(l1[i])
        i += 1
    while j < len(l2):
        merged.append(l2[j])
        j += 1
    return merged

def get_medi(list_):
    length = len(list_)
    mid_idx = length//2
    if length % 2: # odd number
        return float(list_[mid_idx])
    else:
        return float((list_[mid_idx] + list_[mid_idx-1])/2)

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    merged = merge(nums1, nums2)
    return get_medi(merged)


# test
t1_nums1 = [1,3]
t1_nums2 = [2]
t2_nums1 = [1,2]
t2_nums2 = [3,4]
t3_nums1 = []
t3_nums2 = [1] # output 1

print(findMedianSortedArrays(t1_nums1, t1_nums2))
print(findMedianSortedArrays(t2_nums1, t2_nums2))
print(findMedianSortedArrays(t3_nums1, t3_nums2))


# for insert mode