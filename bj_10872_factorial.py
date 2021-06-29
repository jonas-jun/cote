'''
input: int N
output: N!
'''

n = int(input())

def facto(i):
    if i == 0:
        return 1
    ans = 1
    for j in range(1, i+1):
        ans *= j
    return ans

print(facto(n))

def facto_recurse(i):
    if i == 0:
        return 1
    return i * facto_recurse(i-1)

print(facto_recurse(n))