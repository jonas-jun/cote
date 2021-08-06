'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

PSEUDO
외곽 사각형 테두리부터 안쪽으로 들어가면서 회전
def helper(first, last):
    각 모서리 숫자들을 이어서 풀을 만들고
    왼쪽 모서리부터 한바퀴 돌리면서 pool의 숫자들을 배정
first와 last를 0, len(list)-1 부터:
    helper돌린 후
    first += 1
    last -= 1
    (first < last 동안 반복)

https://leetcode.com/problems/rotate-image/
'''


def rotate(matrix):

    if len(matrix) == 1: return matrix

    def helper(first, last):
        nonlocal matrix

        temp1 = matrix[first][first:last+1]
        temp2 = [matrix[i][last] for i in range(first, last+1)]
        temp3 = matrix[last][first:last+1]
        temp4 = [matrix[i][first] for i in range(first, last+1)]
        pool = temp4[::-1] + temp1 + temp2 + temp3[::-1]

        i, j = first, first
        idx = 0
        while j <= last:
            matrix[i][j] = pool[idx]
            idx += 1
            j += 1
        j -= 1
        while i <= last:
            matrix[i][j] = pool[idx]
            idx += 1
            i += 1
        i -= 1
        while j >= first:
            matrix[i][j] = pool[idx]
            idx += 1
            j -= 1
        j += 1
        while i >= first:
            matrix[i][j] = pool[idx]
            idx += 1
            i -= 1
        return

    first = 0
    last = len(matrix)-1
    while first < last:
        helper(first, last)
        first += 1
        last -= 1
    return matrix

# for test

t1 = [[1]]
t2 = [[1,2],[3,4]]
t3 = [[1,2,3],[4,5,6],[7,8,9]]
t4 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotate(t1))
print(rotate(t2))
print(rotate(t3))
print(rotate(t4))


# for insert mode