'''
Unique한 숫자로 이뤄진 candidates에서 샘플링 with replacement를 해서 target을 만들 수 있는 모든 경우를 리턴

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

PSEUDO
각 candidates의 숫자들이 등장할 수 있는 개수 중 있는 가장 큰 값을 구하고
그 범위 안에서 모든 경우들을 탐색한다.
solution 1
범위를 max_n 이하의 수로 구하는데, max_n은 candidates 중 가장 작은 숫자가 가질 수 있는 최대 개수로 정했다. 시간이 매우 오래 걸림
solution 2
각 candidates 숫자 마다 가질 수 있는 최대 값들을 별도로 정의해준 후 DFS를 돌려 가면서 탐색했다 + 백트래킹으로 target을 우선 넘어갈 경우 탐색을 종료했다.

https://leetcode.com/problems/combination-sum
'''

from typing import List
from itertools import product
def sol1(candidates: List[int], target: int):
    max_n = target // min(candidates)
    pool = list(product(range(max_n+1), repeat=len(candidates)))
    def check(arr):
        nonlocal candidates, target
        cum = 0
        for i in range(len(candidates)):
            cum += (arr[i]*candidates[i])
        return cum == target
    
    temp = [arr for arr in pool if check(arr)]
    ans = list()
    for arr in temp:
        t = list()
        for idx in range(len(arr)):
            t += ([candidates[idx]] * arr[idx])
        ans.append(t)
    return ans

def sol2(candidates, target):

    ans = list()
    candidates.sort(reverse=True) # 장치 1
    max_n = [target//i for i in candidates]

    def transform(path):
        nonlocal candidates
        rst = list()
        for i in range(len(path)):
            rst += [candidates[i]] * path[i]
        return rst

    def dfs_helper(path, idx, val):
        nonlocal candidates, max_n, ans, target
        trans = transform(path)
        sum_trans = sum(trans)
        if sum_trans > target: return # 장치 2
        path.append(val)
        sum_trans += (candidates[idx]*val) # 장치 3
        trans += [candidates[idx]] * val
        if len(path) == len(candidates):
            if sum_trans == target:
                ans.append(trans)
            return
        togo = list(range(max_n[idx+1]+1)) 
        for loc in togo:
            dfs_helper(path[:], idx+1, loc) # 포인트 1

    for val in range(max_n[0]+1):
        dfs_helper(list(), 0, val)
    
    return ans

# for test
from time_check import check
t1 = [48,22,49,24,26,47,33,40,37,39,31,46,36,43,45,34,28,20,29,25,41,32,23]
t1_target = 69
t2 = [2,3,6,7]
t2_target = 7

print('case 1')
#print(check(sol1, t1, t1_target)) # don't run... needs very very long time
print(check(sol2, t2, t2_target))

print('case 2')
print(check(sol1, t2, t2_target))
print(check(sol2, t2, t2_target))