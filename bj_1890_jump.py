'''
N×N 게임판에 수가 적혀져 있다. 이 게임의 목표는 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프를 해서 가는 것이다.
각 칸에 적혀있는 수는 현재 칸에서 갈 수 있는 거리를 의미한다. 반드시 오른쪽이나 아래쪽으로만 이동해야 한다.
한번 점프할 때 방향을 바꿀 수는 없다.

sol_1: DFS
sol_2: DP (시간이 빠름 -> 경로는 DP로 파악해볼 것!!)

https://www.acmicpc.net/problem/1890
'''

def sol_1(map_, N):
    ans = 0

    def helper(i,j):
        nonlocal map_, N, ans
        if i == N-1 and j == N-1:
            ans += 1
            return
        d = map_[i][j]
        if i+d < N: helper(i+d, j)
        if j+d < N: helper(i, j+d)
    
    helper(0,0)
    return ans

def sol_2(map_, N):
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if dp[i][j] == 0:
                continue
            if map_[i][j] == 0:
                continue
            d = map_[i][j]
            if i+d < N:
                dp[i+d][j] += dp[i][j]
            if j+d < N:
                dp[i][j+d] += dp[i][j]

    return dp[N-1][N-1]

# for test
N = 4
map_ = [[2, 3, 3, 1],
        [1, 2, 1, 3],
        [1, 2, 3, 1],
        [3, 1, 1, 0]]

from time_check import check
print(check(sol_1, map_, N))
print(check(sol_2, map_, N))
