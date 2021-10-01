'''
선이수 과목들이 주어질 때, 해당 클래스들을 다 들을 수 있는지?

Solution
cycle이 있는지 체크하는 문제
current path에 있는 과목이 다시 등장하면 cycle이 있는 것
한번 지나간 visited는 다시 체크해보지 않아도 됨.


https://leetcode.com/problems/course-schedule
'''


from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # build graph
    graph = dict()
    for num in range(numCourses):
        graph[num] = list()
    for edge in prerequisites:
        graph[edge[0]].append(edge[1])

    iscycle = False
    visited = set()
    cur_path = set()

    def dfs_helper(root):
        nonlocal graph, iscycle, visited, cur_path
        if root in visited: return
        if root in cur_path:
            iscycle = True
            return
        cur_path.add(root)
        for node in graph[root]:
            dfs_helper(node)
        visited.add(root) # 이게 핵심.
    
    for node in graph:
        dfs_helper(node)
    
    return True if not iscycle else False

t1 = 2
t1_edges = [[1,0]]
t2 = 2
t2_edges = [[1,0], [0,1]]

print(canFinish(t1, t1_edges))
print(canFinish(t2, t2_edges))