'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
n쌍의 괄호를 사용해서 유효한 모든 괄호문자 만들기

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

PSEUDO 1
맨 앞, 맨 뒤에 (,) 을 각각 넣고 가운데 2n-2개 자리 중 n-1개를 뽑는 combinations '('가 들어갈 index를 구함
pool (가능한 모든 샘플)
pool의 모든 경우에 대해 isValid

PSEUDO 2
DFS를 돌리는데, path나 cum에 값을 할당해주면 돌면서 계속 바뀌기 때문에 직접 함수에 집어넣는 형태로
path += ')'
cum -= 1 해두고
dfs_helper(path, cum)을 넣으면 한번 리프까지 다녀온 후에 다음 탐색을 할 때 예전 path를 그대로 사용할 수 있도록

https://leetcode.com/problems/generate-parentheses/
'''

from itertools import combinations
def sol_1(n):
    idx_pool = list(combinations(list(range(1, (2*n)-1)), n-1))
    pool = [[')' for k in range(2*n)] for l in range(len(idx_pool))]
    for i in range(len(idx_pool)):
        pool[i][0] = '('
        for j in idx_pool[i]:
            pool[i][j] = '('

    def isValid(list1):
        cum = 0
        for char in list1:
            if char == '(':
                cum += 1
            else:
                cum -= 1
            if cum < 0: return False
        return list1
    
    return [''.join(list2) for list2 in pool if isValid(list2)]

def sol_2(n):
    ans = list()
    def dfs_helper(str1, cum):
        nonlocal ans, n
        if len(str1) == n*2:
            if cum == 0:
                ans.append(str1)
            return
        
        if cum == 0:
            dfs_helper(str1+'(', cum+1)
        elif cum == n:
            dfs_helper(str1+')', cum-1)
        else:
            dfs_helper(str1+'(', cum+1)
            dfs_helper(str1+')', cum-1)
    dfs_helper(str(), 0)
    return ans


# for test
from time_check import check

print('case n=3')
print(check(sol_1, 3))
print(check(sol_2, 3))

print('case n=8')
print(check(sol_1, 8))
print(check(sol_2, 8))

# for insert mode