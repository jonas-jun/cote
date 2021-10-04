'''
path의 합이 tragetSum과 같은 path들의 개수
path는 부모->자식 노드 방향으로만 진행됨

Solution
한점을 시작으로 pathSum을 구해서 cnt하는 함수 짜고
traverse 함수를 만들어서 위의 dfs_helper함수를 모든 node에서 시작하도록 해주면 된다.

https://leetcode.com/problems/path-sum-iii
'''

def pathSum(root, targetSum) -> int:
    
    if not root: return 0
    cnt = 0

    def dfs_helper(subroot, cum):
        nonlocal cnt, targetSum
        if not subroot: return
        cum += subroot.val
        if cum == targetSum: cnt += 1
        dfs_helper(subroot.left, cum)
        dfs_helper(subroot.right, cum)
    
    def traverse(start):
        dfs_helper(start, 0)
        if start.left: traverse(start.left)
        if start.right: traverse(start.right)
    
    traverse(root)
    return cnt
