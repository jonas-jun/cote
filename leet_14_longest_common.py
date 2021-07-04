'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

https://leetcode.com/problems/longest-common-prefix/
'''

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortest = min(map(len, strs))
    standard = strs[0]
    max_idx = 0
    for i in range(shortest):
        std = standard[i]
        for s in strs:
            if s[i] != std:
                return standard[:max_idx]
        max_idx += 1
    return standard[:max_idx]

# test
t1 = ['flower', 'flow', 'flight']
t2 = ['dog', 'racecar', 'car']

from time_check import check
print(check(longestCommonPrefix, t1))
print(check(longestCommonPrefix, t2))

