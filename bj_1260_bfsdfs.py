import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())

graph = dict()
for i in range(m):
    fr, to = map(int, sys.stdin.readline().split())
    graph.setdefault(fr, list()).append(to)
    graph.setdefault(to, list()).append(fr)


def bfs(graph, root):
    path = list()
    visited = dict()
    queue = deque([root])
    visited[root] = True

    while queue:
        cur = queue.popleft()
        path.append(cur)
        togo = sorted(graph[cur]) if cur in graph else list()

        for loc in togo:
            if loc not in visited:
                queue.append(loc)
                visited[loc] = True

    return path

def dfs(graph, root):
    path = list()
    visited = dict()

    def dfs_helper(gra, start, path, visited):        
        visited[start] = True
        path.append(start)
        togo = sorted(gra[start]) if start in graph else list()
        
        for loc in togo:
            if loc not in visited:
                dfs_helper(gra, loc, path, visited)
    dfs_helper(graph, root, path, visited)
    return path

result_dfs = dfs(graph, v)
result_bfs = bfs(graph, v)
print(' '.join(map(str, result_dfs)))
print(' '.join(map(str, result_bfs)))





# for insert mode