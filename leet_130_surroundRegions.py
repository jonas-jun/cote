'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

모든 면이 X로 둘러싸인 O 들은 다시 X로 바꿔줌
O가 보더라인에 있어서 한면이라도 X로 둘러싸이지 않았다면 그대로 남겨 둠
inplace 방식으로 할 것

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

https://leetcode.com/problems/surrounded-regions/
'''

def solve(board) -> None:
    m, n = len(board), len(board[0])
    visited_map = [[False for k in range(n)] for l in range(m)]
    path = list()
    check = False

    def dfs_helper(i,j):
        nonlocal board, visited_map, path, check, m, n
        path.append((i,j))
        visited_map[i][j] = True
        if i == 0 or j == 0 or i == m-1 or j == n-1:
            check = True

        togo = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for loc in togo:
            idx_i, idx_j = loc[0], loc[1]
            if 0 <= idx_i < m and 0 <= idx_j < n and not visited_map[idx_i][idx_j] and board[idx_i][idx_j] == 'O':
                dfs_helper(idx_i, idx_j)

    change = list()
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and not visited_map[i][j]:
                dfs_helper(i,j)
                if not check: change += path
                path = list()
                check = False

    for loc in change:
        board[loc[0]][loc[1]] = 'X'
    return

def solve2(board) -> None:
    '''
    보더라인에서 출발하는 dfs만 O로 남기고 나머지는 X처리
    '''
    m, n = len(board), len(board[0])
    visited_map = [[False for k in range(n)] for l in range(m)]
    path = list()
    
    def dfs_helper(i,j):
        nonlocal board, visited_map, path, m, n
        path.append((i,j))
        visited_map[i][j] = True

        togo = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        for loc in togo:
            idx_i, idx_j = loc[0], loc[1]
            if 0 <= idx_i < m and 0 <= idx_j < n and not visited_map[idx_i][idx_j] and board[idx_i][idx_j] == 'O':
                dfs_helper(idx_i, idx_j)
    
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and not visited_map[i][j] and (i==0 or j==0 or i==m-1 or j==n-1):
                dfs_helper(i,j)

    path = set(path)            
    for i in range(m):
        for j in range(n):
            if (i,j) not in path:
                board[i][j] = 'X'
    return


# for test
from time_check import check
t1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(check(solve, t1))
t1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(check(solve2, t1))

print(t1)


# for insert mode