'''
강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)
재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.)
재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다

예제 입력 1 
2 2
1 5
13 29

예제 출력 1 
1
5
67863915

https://www.acmicpc.net/problem/1010
'''

dp = [[0 for k in range(30)] for l in range(30)]
for i in range(30):
    dp[i][i] = 1
for j in range(30):
    dp[1][j] = j

def get_val(i,j):
    global dp
    if dp[i][j]: return dp[i][j]
    ans = get_val(i, j-1) * j * (1/(j-i))
    dp[i][j] = ans
    return int(ans)

import sys
for _ in range(int(input())):
    input_ = list(map(int, sys.stdin.readline().split()))
    print(get_val(input_[0], input_[1]))