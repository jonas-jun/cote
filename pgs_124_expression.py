'''
124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

124 나라에는 자연수만 존재합니다.
124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

10진법	124 나라	10진법	124 나라
1	1	6	14
2	2	7	21
3	4	8	22
4	11	9	24
5	12	10	41
자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

제한사항
n은 500,000,000이하의 자연수 입니다.

https://programmers.co.kr/learn/courses/30/lessons/12899
'''

# use divmod !!!

def sol1(n):
    vocab = {1:1, 2:2, 3:4}
    vocab_remain = {0:4, 1:1, 2:2}

    if n <= 3:
        return str(vocab[n])
    
    a,b = n//3, n%3
    if b == 0:
        a -= 1
    return sol1(a) + str(vocab_remain[b])

def sol2(n):
    'divmod 사용, vocab 통합'
    vocab = {1:1, 2:2, 3:4}
    
    if n <= 3:
        return str(vocab[n])
    a,b = divmod(n, 3)
    if b == 0:
        a -= 1
        b = 3
    return sol2(a) + str(vocab[b])

t1 = 10
t2 = 42 # 1114
t3 = 21 # 144

from time_check import check

print(check(sol1, t1))
print(check(sol2, t1))
print(check(sol1, t2))
print(check(sol2, t2))
print(check(sol1, t3))
print(check(sol2, t3))