'''
alternating coin arr를 만들 때까지 필요한 최소 변경 수? (flip 뒤집는 횟수?)
[1,1,0,1]은 [0,1,0,1]로 1번 뒤집으면 된다.

[0,1,0,1,...] 경우와 [1,0,1,0,...] 경우를 만드는 flip 수를 확인하고 둘 중 작은 값을 return
'''

from typing import List

def minFlip_1(arr: List):
    # [0,1,...]
    start_zero = 0
    for idx in range(0, len(arr), 2):
        if arr[idx] != 0: start_zero += 1
    for idx in range(1, len(arr), 2):
        if arr[idx] != 1: start_zero += 1

    # [1,0,...]
    start_one = 0
    for idx in range(0, len(arr), 2):
        if arr[idx] != 1: start_one += 1
    for idx in range(1, len(arr), 2):
        if arr[idx] != 0: start_one += 1

    return min(start_zero, start_one)

def minFlip_2(arr: List):
    s0 = sum([n == i%2 for i, n in enumerate(arr)])
    s1 = sum([n == (i+1)%2 for i, n in enumerate(arr)])
    return min(s0, s1)

t1 = [1,1,0,1,1]
t2 = [0]

print('case 1')
print(minFlip_1(t1))
print(minFlip_2(t1))

print('case 2')
print(minFlip_1(t2))
print(minFlip_2(t2))