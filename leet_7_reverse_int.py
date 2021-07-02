'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

https://leetcode.com/problems/reverse-integer/
'''

def reverse(num: int) -> int:
    valid_range = range(-(2**31), (2**31))
    if num < 0:
        minus = True
        num = -1 * num
    else:
        minus = False
    
    num = int(str(num)[::-1])
    if minus:
        num = -1 * num
    return num if num in valid_range else 0

# test
t1 = 123
t2 = -123
t3 = 120
t4 = 0

print(reverse(t1))
print(reverse(t2))
print(reverse(t3))
print(reverse(t4))

# for insert mode