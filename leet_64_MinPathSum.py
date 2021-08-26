'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

2차원 행렬이 주어졌을 때 왼쪽위에서 오른쪽아래로 이동하는 경로(path) 중 합이 최소가 되는 경우의 합을 구해라
오른쪽이나 아래로 밖에 이동 못함

sol1: DFS 오른, 아래 로 togo를 잡고 오른아래끝에 도착하면 sum(path) 계산
sol2: DP. 경로와 똑같은 2차원 행렬 그려놓고 dp[i][j]는 그 지점까지 올 수 있는 최소값

https://leetcode.com/problems/minimum-path-sum
'''

from typing import List
def sol1(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0]) #m; 세로, n:가로
    ans = float('inf') 
    
    def dfs_helper(start, path):
        nonlocal grid, m, n, ans
        path.append(grid[start[0]][start[1]])
        if start == (m-1, n-1):
            ans = min(ans, sum(path))
            return
        
        if start[0]+1 < m:
            dfs_helper((start[0]+1, start[1]), path[:])
        if start[1]+1 < n:
            dfs_helper((start[0], start[1]+1), path[:])
        
    dfs_helper((0,0), list())
    return ans

def sol2(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0]) #m; 세로, n:가로
    dp = [[False for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for idx in range(1, m):
        dp[idx][0] = dp[idx-1][0] + grid[idx][0]
    for idx in range(1, n):
        dp[0][idx] = dp[0][idx-1] + grid[0][idx]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[-1][-1]

from time_check import check
t1 = [[1,3,1],[1,5,1],[4,2,1]]
t2 = [[1,2,3,5,2,1], [3,2,35,6,1,2], [2,1,8,9,0,34], [4,5,7,2,3,9], [10,3,7,3,21,4]]

print('case 1')
print(check(sol1, t1))
print(check(sol2, t1))

print('case 2')
print(check(sol1, t2))
print(check(sol2, t2))