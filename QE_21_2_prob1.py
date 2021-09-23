'''
Convolutional Network 구현
padding은 없다고 가정
image size, filter size, stride 이용
'''

def conv_helper(A, B):
    ans = 0
    M, N = len(A), len(A[0]) # M height, N wide
    for i in range(M):
        for j in range(N):
            ans += A[i][j]*B[i][j]
    return ans

def get_mat(image, s_i, e_i, s_j, e_j):
    x = image[s_i: e_i]
    for i in range(len(x)):
        x[i] = x[i][s_j: e_j]
    return x

def conv(image, pattern, stride=1): # image (m,m) pattern (n,n)
    m, n = len(image), len(pattern)
    if m < n:
        raise ValueError ("Error: m > n")
    if n + stride > m:
        raise ValueError ('Incompatible params')
    ans = list()
    for i in range(0, m-n+1, stride):
        for j in range(0, m-n+1, stride):
            ans.append(conv_helper(get_mat(image, i, i+n, j, j+n), pattern))

    # reshape
    length = ((m-n) // stride) + 1
    new_ans = list()
    temp = list()
    for i in range(len(ans)):
        temp.append(ans[i])
        if len(temp) == length:
            new_ans.append(temp)
            temp = list()
    return new_ans

t1 = [[3,1,0,2,1],
[1,-1,0,1,2],
[2,2,1,1,3],
[1,-1,-1,0,-1],
[1,1,0,1,2]]

filter = [[1,-1, 0], [1, -1, 0], [1, -1, 0]]

print(conv(t1, filter, stride=2))