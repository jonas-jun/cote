'''

https://www.acmicpc.net/problem/10799
'''

def sol_1(s:str) -> int:
    idx_stack = list()
    bar = list()
    laser = [0 for _ in range(len(s))]

    for idx in range(len(s)):
        if s[idx] == '(': idx_stack.append(idx)
        else:
            if s[idx-1] == '(':
                laser[idx] = 1
                idx_stack.pop()
            else:
                bar.append([idx_stack.pop(), idx])
    
    ans = 0
    for b in bar:
        ans += (sum(laser[b[0]:b[1]]) + 1)
    return ans

def sol_2(s:str) -> int:
    stack = list()
    ans = 0
    for idx in range(len(s)):
        if s[idx] == '(': stack.append(idx)
        else:
            stack.pop()
            if s[idx-1] == '(': ans += len(stack)
            else: ans += 1
    return ans

# for test

t1 = '()(((()())(())()))(())'
t2 = '(((()(()()))(())()))(()())'

from time_check import check
print('case 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('case 2')
print(check(sol_1, t2))
print(check(sol_2, t2))