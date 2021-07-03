'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container.

example
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

https://leetcode.com/problems/container-with-most-water/
'''

from typing import List

# sol1 easy, O(n^2), but time limit exceeded
def get_area(i, j, arr):
    return abs(i-j) * min(arr[i], arr[j])

def maxArea(height: List[int]) -> int:
    ans = 0
    len_ = len(height)
    for id1 in range(len_-1):
        for id2 in range(id1+1, len_):
            cur = get_area(id1, id2, height)
            if ans < cur:
                ans = cur
    return ans

# sol2 medium, O((1/2) * n^2), dfs, time limit exceeded
def check_idx(height, visited, togo):
    new = list()
    for loc in togo:
        if loc[0] < len(height) and loc[1] < len(height) and loc[0] < loc[1] and not visited[loc[0]][loc[1]]:
            new.append(loc)
    return new

def maxArea_2(height):
    visited = [[None for i in range(len(height))] for j in range(len(height))]
    for i in range(len(height)):
        visited[i][i] = 1
    ans = 0

    def dfs_helper(root, ans):
        cur = get_area(root[0], root[1], height)
        visited[root[0]][root[1]] = cur
        ans = max(ans, cur)
        togo = check_idx(height, visited, [(root[0]+1, root[1]), (root[0], root[1]+1)])
        for loc in togo:
            ans = dfs_helper(loc, ans)
        return ans
    
    ans = dfs_helper((0,1), ans)
    return ans

def maxArea_3(height):
    'set standard first and go better'
    left, right = 0, len(height)-1
    ans = 0
    while left < right:
        ans = max(ans, get_area(left, right, height))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans

# test
from time_check import check

t1 = [1,8,6,2,5,4,8,3,7]
t2 = [1,1]
t3 = [4,3,2,1,4]
t4 = [1,2,1]

print('>> func 1')
print(check(maxArea, t1))
print(check(maxArea, t2))
print(check(maxArea, t3))
print(check(maxArea, t4))
print('>> func 2')
print(check(maxArea_2, t1))
print(check(maxArea_2, t2))
print(check(maxArea_2, t3))
print(check(maxArea_2, t4))
print('>> func 3')
print(check(maxArea_3, t1))
print(check(maxArea_3, t2))
print(check(maxArea_3, t3))
print(check(maxArea_3, t4))


# for insert mode