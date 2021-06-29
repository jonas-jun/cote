'''
0, 1, 1, 2, 3, 5, 8, ...
n = 0 이면 0
n = 3 이면 2
'''

import sys
input_ = int(sys.stdin.readline())

def piv(n):
    if n <= 1: return n
    return piv(n-1) + piv(n-2)

print(piv(input_))



# for insert mode