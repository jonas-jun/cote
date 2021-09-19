'''
n이 주어지면, 1-n 까지의 노드로 만들 수 있는 unique BST의 개수를 구해라.

Solution
Dynamic Programing
3이 주어진다고 하면 1,2,3이 root node가 될 수 있음
각각의 경우에 대해 왼쪽 오른쪽 subtree의 종류를 구할 수 있음 (왼쪽 오른쪽 모두 연속하는 n으로 만들 수 있는 BST의 수가 됨)

https://leetcode.com/problems/unique-binary-search-trees
'''

memo = [False for _ in range(20)] # 1<=n<=19
memo[0] = 1
memo[1] = 1
memo[2] = 2

def numTrees(n: int) -> int:
    global memo
    if memo[n]: return memo[n]
    
    for i in range(3, n+1):
        cum = 0
        for j in range(1, i+1): cum += (memo[j-1] * memo[i-j])
        memo[i] = cum
    
    return memo[n]

print(numTrees(5))
print(numTrees(18))