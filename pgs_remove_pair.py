'''
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다. 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다. 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.
이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. 문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면
b aa baa → bb aa → aa →

PSEUDO
i = 0
s = '0' + s
while i<len(s)-1:
    if s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        i -= 1 # i = -1 이 되는 것을 방지하기 위해 시작 부분에서 s = '0'+s
        continue
    i += 1
len(s)가 1이면 return 1
    
https://programmers.co.kr/learn/courses/30/lessons/12973

'''

def solution1(s):
    if len(s) == 1: return 0

    i = 1
    s = '0' + s # 0baabaa
    while i < len(s)-1:
        if s[i] == s[i+1]: # i == 2
            s = s[:i] + s[i+2:]
            i -= 1
            continue
        i += 1
    return 1 if len(s)==1 else 0

def solution2(s):
    if len(s) == 1: return 0
    list_s = [0] + list(s)
    i = 1
    while i < len(list_s)-1:
        if list_s[i] == list_s[i+1]:
            del list_s[i]
            del list_s[i]
            i -= 1
            continue
        i += 1
    return 1 if len(list_s)==1 else 0

def solution3(s):
    if len(s) == 1: return 0
    stack = list()
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
    return 1 if not stack else 0

# for test
from time_check import check

test1 = 'baabaa'
test2 = 'kokaksldkfjaksldkfjkaaadgbb'
test3 = 'oaaaaaaaaaaakkdkddjkdlddldldlglghhjjjkjklkjkedieiqpeplakslldfffffdsssj'

print('case 1')
print(check(solution1, test1))
print(check(solution2, test1))
print(check(solution3, test1))

print('case 2')
print(check(solution1, test2))
print(check(solution2, test2))
print(check(solution3, test2))

print('case 3')
print(check(solution1, test3))
print(check(solution2, test3))
print(check(solution3, test3))


# for insert mode