'''
N*M크기의 직사각형이 있다. 각 칸은 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형의 넓이를 찾는 프로그램을 작성하시오.

PSEUDO
ans = 1, 답을 1로 두고
길이 2,3,4,5 -> 작은 변의 길이까지 loop:
길이가 length인 정사각형 체크해서 네 꼭지점 숫자가 같은게 있으면 ans를 대체하고 break (바로 다음 크기로 넘어가도 됨)

https://www.acmicpc.net/problem/1051
'''

from typing import List

def solution(sq: List[List[int]]) -> int:
    # 가로 m, 세로 n
    m, n = len(sq[0]), len(sq)
    ans = 1
    for length in range(2, min(m,n)+1):
        for i in range((n-length+1)):
            for j in range((m-length)+1):
                if sq[i][j] == sq[i+length-1][j] == sq[i][j+length-1] == sq[i+length-1][j+length-1]:
                    ans = length
                    break
            if sq[i][j] == sq[i+length-1][j] == sq[i][j+length-1] == sq[i+length-1][j+length-1]:
                break
    return ans**2

# for test
test =\
[[4,2,1,0,1],
[2,2,1,0,0],
[2,2,1,0,1]]

print(solution(test))