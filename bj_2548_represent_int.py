'''
대표 자연수는 주어진 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의 합을 최소로 하는 자연수이다.
대표 자연수가 두 개 이상일 경우 그 중 제일 작은 것을 출력한다.

1. counter 만들기
2. 중간값 찾기
- n//2
- 최소의 key부터 counter 돌면서 n//2보다 크거나 같아지면 바로 return

https://www.acmicpc.net/problem/2548
'''

def sol(arr, n):
    counter = dict()
    for val in arr:
        if val in counter: counter[val]+=1
        else: counter[val]=1
    
    keys = sorted(list(counter.keys()))
    cum = 0
    for key in keys:
        cum += counter[key]
        if cum >= n//2: return key

# for test
t1 = [4,3,2,2,9,10]
t2 = [100]

print(sol(t1, len(t1)))
print(sol(t2, len(t2)))

# for insert mode