'''
0은 land, 1은 water로 이뤄진 matrix가 주어짐
새로운 matrix를 구성해라
- water는 0, land는 인접한 곳에서 0 또는 1씩 커져야 함
- 동서남북으로만 인접한다고 봄

example 1
[[1, 0],
[0, 0]]이 주어졌을 때
[[1, 0],
[2, 1]]이 땅의 모양

example 2
[[0,0,1],
[1,0,0],
[0,0,0]]
이 주어졌을 때
[[1,1,0],
[0,1,1],
[1,2,2]]
가 땅의 모양

Solution
기본적으로 물에서부터 시작해서 BFS를 통해 같은 breath에 있는 것들은 +1 씩 늘려가기
겹치는 부분에서는 작은 쪽의 숫자를 따라야 함 

sol_1 같은 경우는 모든 water에서 각각 height_map을 만들고 각각의 최소값들을 답으로 뽑았다면
sol_2는 water를 동등한 level로 보고 각각에서 꺼내서 출발하다보면 자연스럽게 중간 지점에서 만나게 됨.. 1 차이로 만나게 됨

https://leetcode.com/problems/map-of-highest-peak
'''
from collections import deque
def sol_1(isWater):
    r = len(isWater)
    c = len(isWater[0])
    
    def get_start():
        nonlocal isWater, r, c
        points = list()
        for i in range(r):
            for j in range(c):
                if isWater[i][j] == 1:
                    points.append((i,j))
        return points
    points = get_start()

    ans = [[0 for k in range(c)] for l in range(r)]

    def bfs_helper(root):
        nonlocal r, c, ans
        h_map = [[0 for i in range(c)] for j in range(r)]
        visited_map = [[0 for i in range(c)] for j in range(r)]
        visited_map[root[0]][root[1]] = 1

        def check_loc(loc):
            nonlocal r, c, visited_map
            i, j = loc[0], loc[1]
            if i < 0 or i >= r: return False
            if j < 0 or j >= c: return False
            if visited_map[i][j]: return False
            return loc
        
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            togo = list(map(check_loc, [(cur[0]+1, cur[1]), (cur[0]-1, cur[1]), (cur[0], cur[1]+1), (cur[0], cur[1]-1)]))
            for loc in togo: # (0,1), (1,2)
                if loc:
                    val = h_map[cur[0]][cur[1]] + 1
                    h_map[loc[0]][loc[1]] = val
                    visited_map[loc[0]][loc[1]] = 1
                    queue.append(loc)
                    if loc not in points:
                        if ans[loc[0]][loc[1]]:
                            ans[loc[0]][loc[1]] = min(ans[loc[0]][loc[1]], val)
                        else:
                            ans[loc[0]][loc[1]] = val

    for loc in points:
        bfs_helper(loc)     
    return ans

def sol_2(isWater):
    r = len(isWater)
    c = len(isWater[0])
    newiswater = [[None for k in range(c)] for l in range(r)]
    deq = deque()

    for row in range(r):
        for col in range(c):
            if isWater[row][col] == 1:
                deq.append([row, col])
                newiswater[row][col] = 0
    # 다 None에 (0,2) (1,0)만 0
    while deq:
        row, col = deq.popleft() # (0,2)
        for new_row, new_col in [(row+1, col), (row-1, col), (row, col-1), (row, col+1)]:
            if 0 <= new_row < r and 0 <= new_col < c and newiswater[new_row][new_col] is None: # ()
                newiswater[new_row][new_col] = newiswater[row][col] + 1
                deq.append((new_row, new_col))
    return newiswater

# for test
t1 = [[0,0,1],[1,0,0],[0,0,0]]
t2 = [[0,1],[0,0]]

from time_check import check
print('case 1')
print(check(sol_1, t1))
print(check(sol_2, t1))

print('case 2')
print(check(sol_1, t2))
print(check(sol_2, t2))

# for insert mode