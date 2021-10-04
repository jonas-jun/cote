'''
완전 대칭 tree

https://leetcode.com/problems/invert-binary-tree
'''

def invertTree(root):
    def helper(subroot):
        if not subroot: subroot
        subroot.left, subroot.right = helper(subroot.right), helper(subroot.left) # 동시에 바꿔줘야 둘다 걸릴 수 있음
        return subroot
    root = helper(root)
    return root

def invertTree(root): # 내 식대로
    def helper(subroot):
        if not subroot: return
        subroot.left, subroot.right = subroot.right, subroot.left # 이게 핵심이네
        helper(subroot.left)
        helper(subroot.right)    
    helper(root)
    return root