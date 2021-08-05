'''
An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].

PSEUDO
1자리수: [0, 1]
2자리수: [11, 10] -> [3, 2] -> [0,1,3,2]
3자리수: [110, 111, 101, 100] -> [0,1,3,2] + [6, 7, 5, 4] (뒤집은 후 + 2**2)
4자리수: [1100, 1101, 1111, 1110, 1010, 1011, 1001, 1000] -> [0,1,3,2,6,7,5,4] + [12, 13, 15, 14, 10, 11, 9, 8]
5자리수: [11000, 11001, 11011, ...]
dp[n] = dp[n-1] + [val + 2**(n-1) for val in dp[n-1][::-1]] 점화식==DP로 풀 수 있음

sol_2
bitwise operators: a ^ (a >> 2)를 하나씩 늘려가면 됨..

https://leetcode.com/problems/gray-code/
'''
from typing import List

def sol_1(n:int) -> List[int]:
    dp = dict()
    dp[1] = [0,1]
    dp[2] = [0,1,3,2]

    def get_list(val:int):
        nonlocal dp
        if val in dp: return dp[val]
        ans = get_list(val-1) + [v + (2**(val-1)) for v in get_list(val-1)[::-1]]
        dp[val] = ans
        return ans
    return get_list(n)

def sol_2(n:int) -> List[int]:
    ans = list()
    idx = 0
    while idx <= 2**n -1:
        ans.append(idx ^ (idx >> 1))
        idx += 1
    return ans

# for test
from time_check import check
print(' >> case 1: 4')
print(check(sol_1, 4))
print(check(sol_2, 4))
print(' >> case 2: 10')
print(check(sol_1, 10))
print(check(sol_2, 10))

# for insert mode