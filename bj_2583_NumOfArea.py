'''
전에 모눈종이 가로n, 세로m 칸
그 안에 직사각형들이 있고 왼쪽아래좌표와 오른쪽위좌표가 주어짐
직사각형들은 색칠되고, 색칠 되지 않은 영역(섬)들의 개수와 각 넓이를 오름차순으로 출력

예제 입력 1 
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
예제 출력 1 
3
1 7 13

https://www.acmicpc.net/problem/2583
'''
def solution(input_map, m, n): # m:세로 n:가로
    ans = list()
    cum = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    def helper(i, j):
        nonlocal input_map, visited, cum
        if not 0<=i<m or not 0<=j<n: return
        if visited[i][j]: return
        if not input_map[i][j]: return
        visited[i][j] = True
        cum += 1
        helper(i+1, j)
        helper(i-1, j)
        helper(i, j+1)
        helper(i, j-1)

    for i in range(m):
        for j in range(n):
            if input_map[i][j] and not visited[i][j]:
                helper(i, j)
                ans.append(cum)
                cum = 0
    return ans

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
m, n, k = map(int, input().split()) # m: 세로, n: 가로, k: 직사각형 개수
input_map = [[True for _ in range(n)] for _ in range(m)]
for _ in range(k):
    one, two, three, four = map(int, input().split())
    for i in range(m-four, m-two):
        for j in range(one, three):
            input_map[i][j] = False

ans = solution(input_map, m, n)
print(len(ans))
print(' '.join(map(str, sorted(ans))))
