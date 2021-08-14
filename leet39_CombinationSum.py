'''


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
    '''
    각 자리수마다 최대치로 들어갈 수 있는 숫자를 구해서 ('//' 연산) range(n+1)
    graph를 만든다. (DFS를 돌아야 함)
    각각 path에 append 해주고
    끝자리에 오면 path와 candidates로 합을 확인해서 target과 일치한다면 path를 answer에 append    
    
    [2,3,6,7] 7
    '''
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
            #print('last func', path)
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
#print(check(sol1, t1, t1_target))
print(check(sol2, t2, t2_target))

print('case 2')
print(check(sol1, t2, t2_target))
print(check(sol2, t2, t2_target))