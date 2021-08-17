'''
distinct한 수들로 이뤄진 배열과 target: int이 주어질 때 배열 내에서 두 수를 골라 합이 target이 되는 쌍의 개수
5 12 7 10 9 1 2 3 11,  13 이면 답은 3
Sol1: 정렬 후 two pointer (기본)
Sol2: loop을 돌면서 타겟에서 숫자를 뺀 나머지를 set에 넣어준다. 만약 우선 그 숫자가 set에 있는지 확인해서 있으면 ans += 1, 없으면 set에 넣어주기
https://www.acmicpc.net/problem/3273
'''

def sol1(arr, target):
    left, right = 0, len(arr)-1
    ans = 0
    arr.sort()
    while left < right:
        sum_ = arr[left] + arr[right]
        if sum_ == target:
            ans += 1
            left += 1
            right -= 1
        elif sum_ > target:
            right -= 1
        else:
            left += 1
    return ans

def sol2(arr, target):
    check = set()
    ans = 0
    for val in arr:
        if val in check:
            ans += 1
        else:
            check.add(target-val)
    return ans

# for test
t1 = [5, 12, 7, 10, 9, 1, 2, 3, 11, 4, 15, 19, 13, 33, 6, 8]
from time_check import check
print(sorted(t1))
print(check(sol1, t1, 15))
print(check(sol2, t1, 15))