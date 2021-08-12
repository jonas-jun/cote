'''
number: str에서 k개의 숫자를 제거했을 때 가장 큰 수를 return: str
number	k	return
"1924"	2	"94"
"1231234"	3	"3234"
"4177252841"	4	"775841"

PSEUDO
sol1
def helper():
    number 길이가 1이면 (k는 남아있다는 것이므로)
    k-=1, number = str() 처리

    앞에서부터 k+1개의 숫자에서 가장 큰 숫자를 기준으로 앞쪽 숫자들은 떼어냄
    k - (떼어낸 숫자의 개수)
    ans에 max숫자를 넣어주고, number는 그 뒤쪽부분으로 자름 number = number[idx+1:]
while k:
    helper()
sol2
stack을 쓴다.
감소하는 구간에서는 그냥 stack.append
증가하는 구간에서는 while문으로 새로운 값보다 작은 것들을 stack에서 제거, k-=1

https://programmers.co.kr/learn/courses/30/lessons/42883
'''

def sol(number, k):

    def helper():
        nonlocal number, k, ans
        if len(number) == 1:
            number = str()
            k-=1
            return
        idx = 1
        max_val = int(number[0]) # 4, 7
        max_idx = 0 # 0, 2

        while idx <= k: # 1 <= 4
            if int(number[idx]) > max_val:
                max_val = int(number[idx])
                max_idx = idx
            idx += 1
        ans += number[max_idx]
        number = number[max_idx+1:]
        k -= max_idx
    
    ans = str()
    while k:
        helper()
    return ans+number

def sol2(number, k):
    
    stack = list(number[0])
    idx = 1
    
    while idx < len(number):
        if number[idx] > stack[-1]: # 증가한다면
            while stack and (stack[-1] < number[idx]) and k:
                stack.pop()
                k -= 1
        stack.append(number[idx])
        idx += 1
        if not k: break

    if k: return number[:-k]
    return ''.join(stack) + number[idx:]


# for test
from time_check import check
print(check(sol, '1924', 2))
print(check(sol, '1231234', 3))
print(check(sol, '4177252841', 4))
print(check(sol, '91', 1))

print(check(sol2, '1924', 2))
print(check(sol2, '1231234', 3))
print(check(sol2, '4177252841', 4))
print(check(sol2, '91', 1))