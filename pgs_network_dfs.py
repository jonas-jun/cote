'''
네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

입출력 예
n	computers	return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

https://programmers.co.kr/learn/courses/30/lessons/43162

PSEUDO
build graph_dict
visited_map: [False]*n
ans = 0

dfs_helper(root):
    nonlocal graph_dict, visited_map
    visited_map[root] = True
    for loc in graph_dict[root]:
        if not visited_map[loc]: dfs_helper(loc)

do dfs_helper at all spots, and ans += 1
'''

def solution(n, computers):
    graph = dict()
    for i in range(n):
        graph[i] = list()
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1: # and i != j:
                graph[i].append(j)
    
    ans = 0
    visited_map = [False]*n
    
    # make dfs_helper
    def dfs_helper(root):
        nonlocal graph, visited_map
        visited_map[root] = True
        for loc in graph[root]:
            if not visited_map[loc]:
                dfs_helper(loc)
        
    # do dfs at all spot
    for i in range(len(visited_map)):
        if not visited_map[i]:
            dfs_helper(i)
            ans += 1
    return ans

# for test
t1_coms = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
t1_n = 3
t2_coms = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
t2_n = 3

from time_check import check
print(check(solution, t1_n, t1_coms))
print(check(solution, t2_n, t2_coms))

# for insert mode