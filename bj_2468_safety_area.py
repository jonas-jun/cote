'''
장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
어떤 지역의 높이 정보는 행과 열의 크기가 각각 N인 2차원 배열 형태로 주어지며 배열의 각 원소는 해당 지점의 높이를 표시하는 자연수이다. 

5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

5
https://www.acmicpc.net/problem/2468
'''

def sol(map_, length):
    #visited = [[False]*length]*length
    visited = [[False for i in range(length)] for j in range(length)]
    max_height = max(max(map_))

    def check_loc(loc, standard, visited):
        nonlocal map_, length
        i,j = loc[0], loc[1]
        if i < 0 or i >= length: return False
        if j < 0 or j >= length: return False
        if map_[i][j] <= standard: return False
        if visited[i][j]: return False
        return loc
    
    def dfs_helper(root, standard):
        i, j = root[0], root[1]
        visited[i][j] = True
        #print('aaa', visited)
        togo = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        #print('root:', root)
        
        togo1 = [check_loc(loc, standard, visited) for loc in togo]
        #print('togo:', togo1)
        for loc in togo1:
            if loc: dfs_helper(loc, standard)
    
    ans = 0
    for height in range(max_height):
        temp = 0
        for i in range(length):
            for j in range(length):
                if not visited[i][j] and map_[i][j] > height:
                    dfs_helper((i,j), height)
                    temp += 1
        ans = max(ans, temp)
        visited = [[False for i in range(length)] for j in range(length)]
    
    return ans

import sys
sys.setrecursionlimit(10**6)
map1 = list()
n = int(input())
for _ in range(n):
    map1.append(list(map(int, sys.stdin.readline().split())))

print(sol(map1, n))

# for insert mode