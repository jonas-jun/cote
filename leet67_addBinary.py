'''
이진수의 합

solution 1,2: 이진수 상태에서 각 자리수를 더하고 2가 넘어가면 1을 올려주면서 나머지를 현재 자리수에 넣어줌
solution 3: 이진수를 십진수로 바꾼 후 덧셈하고 다시 이진수로 (val을 2로 계속 나눠가는 과정을 한번 이해해보기!!)

https://leetcode.com/problems/add-binary
'''

def sol_1(a: str, b: str) -> str:
    a, b = a[::-1], b[::-1]
    a_i, b_i = 0, 0
    ans = str()
    up = 0

    while a_i < len(a) and b_i < len(b):
        temp = int(a[a_i]) + int(b[b_i]) + up
        up = 0
        if temp >= 2:
            up += 1
            temp -= 2
        ans += str(temp)
        a_i += 1
        b_i += 1

    while a_i < len(a):
        temp = int(a[a_i]) + up
        up = 0
        if temp >= 2:
            up += 1
            temp -= 2
        ans += str(temp)
        a_i += 1

    while b_i < len(b):
        temp = int(b[b_i]) + up
        up = 0
        if temp >= 2:
            up += 1
            temp -= 2
        ans += str(temp)
        b_i += 1

    if up: ans += '1'
    return ans[::-1]

from itertools import zip_longest
def sol_2(a:str, b:str) -> str:
    a, b = a[::-1], b[::-1]
    ans = str()
    up = 0
    for val1, val2 in zip_longest(a,b, fillvalue='0'):
        up, present = divmod((int(val1) + int(val2) + up), 2)
        ans += str(present)
    if up: ans += '1'
    return ans[::-1]

def sol_3(a:str, b:str) -> str:
    def to_ten(s: str):
        ans = 0
        n = 0
        for char in s[::-1]:
            ans += int(char) * (2**n)
            n += 1
        return ans

    def to_binary(val: int) -> str:
        if val == 0: return '0'
        ans = str()
        while val != 0:
            val, v2 = divmod(val, 2)
            ans += str(v2)
        return ans[::-1]

    int_a, int_b = to_ten(a), to_ten(b)    
    return to_binary(int_a+int_b)


# for test
from time_check import check
ta, tb = '10111101', '110101000110'

print(check(sol_1, ta, tb))
print(check(sol_2, ta, tb))
print(check(sol_3, ta, tb))