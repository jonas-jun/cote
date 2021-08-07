'''
'여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.

쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다. '
이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.

레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다. 

()(((()())(())()))(())  17
(((()(()()))(())()))(()())  24

PSEUDO
sol_1
laser의 위치와 bar들의 위치(시작, 끝)를 담아놓고 각 bar에 담긴 laser의 수를 활용해 잘라진 개수를 구함
for i in range(len(s)):
    if s[i] == '(': stack.append(idx)
    else:
        if s[i-1] == '(': 레이저의 위치, stack.pop()
        else: bar.append([stack.pop(), idx]) # bar의 위치
각 bar에 대해 그 안의 레이저가 몇개인지 세서 +1을 해주면 됨

sol_2
다시 bar를 loop 돌지 않고 처음 string을 돌면서 답 계산하기
laser라면 그때 열려있는 bar들은 모두 잘리는 것, ans += len(stack)
bar가 닫히는 부분이라면 ans += 1

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