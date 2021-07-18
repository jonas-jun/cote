import sys

'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

example
input
7
6
1 2
2 3
1 5
5 2
5 6
4 7

output print(4)

PSEUDO
graph 만들기 {0: [1,3], 1: [3,4], 2: []...}
visited = [False]* num_computers + 1
cnt = 0
def dfs_helper(root):
    global cnt
    visited[root] = True
    cnt += 1
    for loc in graph[root]:
        if not visited[loc]:
            dfs_helper(loc)
dfs_helper(1)
print(cnt-1)
'''
import sys
num_c = int(input())
visited = [False] * (num_c+1)

# build graph
graph = dict()
for node in range(1, num_c+1):
    graph[node] = list()
num_edge = int(input())
for _ in range(num_edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

def dfs_helper(root):
    global cnt
    if visited[root]:
        return
    visited[root] = True
    cnt += 1
    for loc in graph[root]:
        if not visited[loc]: dfs_helper(loc)
    return

dfs_helper(1)
print(cnt-1)

# for insert mode