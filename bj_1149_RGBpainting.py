'''
N개의 집이 일자로 놓여있다. (RGB 색)
집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

Dynamic Programing
이전 최소값을 활용해서 다음 개수의 최소값을 구할 수 있다. (바로 앞 집의 색이 R, G, B인 경우 별개로 계산해봐야 함)

https://www.acmicpc.net/problem/114색
'''


from typing import List
from collections import defaultdict

def get_next(before: List, cost: List):
    
    r_g = before[0] + cost[1]
    r_b = before[0] + cost[2]
    g_r = before[1] + cost[0]
    g_b = before[1] + cost[2]
    b_r = before[2] + cost[0]
    b_g = before[2] + cost[1]

    return [min(g_r, b_r), min(r_g, b_g), min(r_b, g_b)]

def solution(cost_table):
    n = len(cost_table)
    dp = defaultdict(lambda: list())
    dp[0] = [0,0,0]

    for i in range(1, len(cost_table)+1):
        dp[i] = get_next(dp[i-1], cost_table[i-1])
    
    return min(dp[n])

# for test
cost = [[26, 40, 83],
    [49, 60, 57],
    [13, 89, 99]]

print(solution(cost))


# import sys
# n = int(input())
# for i in range(1, n+1):
#     cost = list(map(int, sys.stdin.readline().split()))
#     dp[i] = get_next(dp[i-1], cost)

# print(min(dp[n]))
