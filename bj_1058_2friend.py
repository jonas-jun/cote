'''
2-친구의 수가 가장 많은 사람의 2-친구의 수 (직접 친구거나, 공통의 친구가 한명 이상 존재하거나)

Sol
BFS를 통해 2칸 이내로 떨어진 사람의 수 구하기

https://www.acmicpc.net/problem/1058
'''

from collections import deque, defaultdict
def solution(graph):
    
    def bfs_helper(root):
        nonlocal graph
        visited = set()
        queue = deque()
        queue.append((root, 0)) # (node, count)의 형태
        while queue:
            node, cnt = queue.popleft()
            if cnt >= 2: break
            for n in graph[node]:
                if n not in visited:
                    queue.append((n, cnt+1))
                    visited.add(n)
        return len(visited)-1
    ans = 0
    for node in graph:
        ans = max(ans, bfs_helper(node))
        print(node, ans)                
    return ans

# import sys
# graph = defaultdict(lambda: list())
# input = sys.stdin.readline
# for i in range(int(input())):
#     line = list(input().rstrip())
#     for j in range(len(line)):
#         if line[j] == 'Y':
#             graph[i+1].append(j+1)
# print(solution(graph))


from collections import defaultdict
graph = defaultdict(lambda: list())
graph[1] = [2,3,4]
graph[2] = [1,3,5]
graph[3] = [1,2]
graph[4] = [1]
graph[5] = [2]

graph2 = defaultdict(lambda: list())
graph2[1] = [2,3]
graph2[2] = [1,3]
graph2[3] = [1,2]
print(solution(graph))
#print(solution(graph2))