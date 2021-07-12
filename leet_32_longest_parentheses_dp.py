'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

https://leetcode.com/problems/longest-valid-parentheses

PSEUDO 1
isValid: s이 유효한 괄호인지?
for i in (0, len(s)-1):
    for j in (i+1, len(s), 2): # 2개 단위로
        if isValid(s[i:j+1]):
            max_len = max(max_len, j+1-i) # 길이 업데이트
return max_len

PSEUDO 2 DP
dp = [0]*length

)이 나왔을 때 바로 앞이 (면 -> dp[i] = 2 (길이 2짜리 valid)
)이 나왔을 때 바로 앞이 )면 -> dp[i-1]이 0이 아니라면 (=바로 앞까지 유효한 괄호들이 있었다면)
    i-dp[i-1]-1 위취가 괄호 열리는 곳인지 확인해야 함 (= 바로 앞 유효한 괄호 보다 한칸 더 앞에서 열리고 한칸 뒤에서 닫히는지)
    그렇다면 dp[i-1] + 2를 해줘야 함. (+ dp[i-dp[i-1]-2]) 그 앞에서도 유효한 괄호들로 진행 중이었다면 이어서 더해줘야 함
return max(dp)
'''

def sol_1(s):
    'is valid'
    def isValid(str_):
        open_ = 0
        for char in str_:
            if char == '(':
                open_ += 1
            else:
                if not open_:
                    return False
                open_ -= 1
        return open_ == 0
    
    max_len = 0
    for i in range(len(s)-1):
        for j in range(i+1, len(s), 2):
            if isValid(s[i:j+1]):
                max_len = max(max_len, j+1-i)
    return max_len

def sol_2(s):
    'dynamic promgramming'
    n = len(s)
    if n <= 1:
        return 0

    dp = [0]*n # [0,0,0,0,0]

    for i in range(1, n):
        if s[i] == ')':
            if s[i-1] == '(':
                dp[i] = dp[i-2] + 2 # + '()'
            else: # '))
                before = dp[i-1]
                if before and (i -before-1 >= 0) and s[i-before-1] == '(': # before == 0 인 경우에는 s[i-before-1]=='('가 성립하지 못함. 
                    dp[i] = dp[i-1] + 2 + dp[i-before-2] # i-before-2 == -1이 되면 0 값이 되기 때문에 상관 없음
    return max(dp)

# for test
t1 = '(()'
t2 = ')()())'
t3 = ''
t4 = '((())))()'

from time_check import check
print('sample 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('sample 2')
print(check(sol_1, t2))
print(check(sol_2, t2))
print('sample 3')
print(check(sol_1, t3))
print(check(sol_2, t3))
print('sample 4')
print(check(sol_1, t4))
print(check(sol_2, t4))

# for insert mode