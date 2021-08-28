'''
Given an m x n matrix, return all elements of the matrix in spiral order.
시계방향으로 돌면서 값들을 list에 넣어서 return해라.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Solution
문제를 나눠서 겉 한바퀴 + 안쪽 한바퀴 + 그 안쪽 한바퀴 (recursion)
return 조건을 잘 생각해보기
'''

def spiral(matrix):
    ans = list()
    def helper(s_i, s_j, e_i, e_j): # i는 세로, j는 가로
        nonlocal ans
        if s_i > e_i or s_j > e_j: return
        if s_i == e_i:
            for j in range(s_j, e_j+1):
                ans.append(matrix[s_i][j])
            return
        if s_j == e_j:
            for i in range(s_i, e_i+1):
                ans.append(matrix[i][s_j])
            return
        for j in range(s_j, e_j+1):
            #indexes.append((s_i, j))
            ans.append(matrix[s_i][j])
        for i in range(s_i+1, e_i+1):
            #indexes.append((i, e_j))
            ans.append(matrix[i][e_j])
        for j in range(e_j-1, s_j-1, -1):
            #indexes.append((e_i, j))
            ans.append(matrix[e_i][j])
        for i in range(e_i-1, s_i, -1):
            #indexes.append((i, s_j))
            ans.append(matrix[i][s_j])
        helper(s_i+1, s_j+1, e_i-1, e_j-1)

    helper(0, 0, len(matrix)-1, len(matrix[0])-1)

    return ans
    
t1 = [[1,2,3],[4,5,6],[7,8,9]]
t2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
t3 = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
print(spiral(t1))
print(spiral(t2))
print(spiral(t3))

