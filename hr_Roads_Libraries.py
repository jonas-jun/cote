'''
도시의 수, 도서관 비용, 길 비용, 연결가능한 길(엣지)이 주어졌을 때 모든 도시의 사람들이 도서관에 갈 수 있도록
도서관과 길을 공사하는 최소 비용은?

Solution
1) 길 비용 >= 도서관 비용: 전체 도시에 도서관을 짓는 게 저렴
2) 길 비용 < 도서관 비용: 연결 가능한 길들은 다 연결하고 각 싸이클마다 도서관 하나씩 짓는 게 저렴

한 싸이클 내에서 생각
모두 도서관: c_lib * num_cities
모두 엣지로 연결하고 도서관 1개: c_lib *1 + c_road* (num_cities-1)
도서관 k개: c_lib * k + c_road * (num_cities - k)

PSEUDO
연결 가능한 길 --> 그래프로 만들기
DFS 돌면서 실제 연결해야하는 길의 개수 세기
한 DFS 싸이클마다 도서관을 하나씩 지어야 함
길 비용 * 실제 DFS가 이동한 길 개수 + 도서관 비용 * 싸이클의 개수
'''

from collections import defaultdict
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib: return c_lib * n
    
    def build_graph(edges):
        rst = defaultdict(lambda: list())
        for edge in edges:
            rst[edge[0]].append(edge[1])
            rst[edge[1]].append(edge[0])
        return rst
    graph= build_graph(cities)
    
    visited = [False for _ in range(n+1)]
    num_roads = 0
    def dfs_helper(root):
        nonlocal graph, visited, num_roads
        visited[root] = True
        for loc in graph[root]:
            if not visited[loc]:
                num_roads += 1
                dfs_helper(loc)
    
    num_cycles = 0
    for city in range(1, n+1):
        if not visited[city]:
            dfs_helper(city)
            num_cycles += 1
    
    return (c_lib * num_cycles) + (c_road * num_roads)

# for test
print('case 1')
t1_cities = 6
t1_c_lib = 2
t1_c_road = 5
t1_edges = [[1,3], [3,4], [2,4], [1,2], [2,3], [5,6]]
print(roadsAndLibraries(t1_cities, t1_c_lib, t1_c_road, t1_edges))

print('case 2')
t2_cities = 5
t2_c_lib = 6
t2_c_road = 1
t2_edges = [[1,2], [1,3], [1,4]]
print(roadsAndLibraries(t2_cities, t2_c_lib, t2_c_road, t2_edges))

# for insert mode