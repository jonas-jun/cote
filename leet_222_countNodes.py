'''
tree의 node 개수 세기

https://leetcode.com/problems/count-complete-tree-nodes
'''

def countNodes(root):
    cnt = 0
    def helper(subroot):
        nonlocal cnt
        if not subroot: return
        cnt += 1
        if subroot.left: helper(subroot.left)
        if subroot.right: helper(subroot.right)
    helper(root)
    return cnt