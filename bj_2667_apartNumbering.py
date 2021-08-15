def solution(n, map1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cum = 0
    ans = list()
    
    def dfs_helper(i, j):
        nonlocal cum, n, map1, visited
        visited[i][j] = True
        cum += 1

        togo = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        togo = [(i,j) for (i,j) in togo if 0<=i<n and 0<=j<n]
        for loc in togo:
            if not visited[loc[0]][loc[1]] and map1[loc[0]][loc[1]]:
                dfs_helper(loc[0], loc[1])

    for i in range(n):
        for j in range(n):
            if map1[i][j] and not visited[i][j]:
                dfs_helper(i, j)
                ans.append(cum)
                cum = 0
    return len(ans), sorted(ans)

# input
test = [[0, 1, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 1, 0, 1],
[1, 1, 1, 0, 1, 0, 1],
[0, 0, 0, 0, 1, 1, 1],
[0, 1, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 0, 0, 0]]

print(solution(len(test), test))