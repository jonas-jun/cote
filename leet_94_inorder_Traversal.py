'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Input: root = [1,null,2,3]
Output: [1,3,2]

https://leetcode.com/problems/binary-tree-inorder-traversal

# inorder / preorder / postorder
1. 'in' order -> get root val in middle. root.left -> root -> root.right
2. 'pre' order -> get root val first. root -> root.left -> root.right
3. 'post' order -> get root val last. root.left -> root.right -> root

PSEUDO
dfs(root.left)
ans.append(root)
dfs(root.right)
'''
from typing import List

def inorderTraversal(root):
    ans = list()
    def dfs_helper(start, ans):
        if not start:
            return
        dfs_helper(start.left, ans)
        ans.append(start.val)
        dfs_helper(start.right, ans)
    dfs_helper(root, ans)
    return ans

def preorder(root):
    ans = list()
    def preorder_helper(start, ans):
        if not start:
            return
        ans.append(start.val)
        preorder_helper(start.left, ans)
        preorder_helper(start.right, ans)
    preorder_helper(root, ans)
    return ans

def postorderTraversal(root) -> List[int]:
        
    ans = list()
    
    def helper(start):
        nonlocal ans
        if not start: return
        # 아래 부분을 넣어주면 마지막에 양 자식이 없는 leaf는 바로 return이 돼서 좀 더 빠르게 끝남
        if not start.left and not start.right:
            ans.append(start.val)
            return
        
        helper(start.left)
        helper(start.right)
        ans.append(start.val)
        
    helper(root)
    return ans

# for test
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(val=1, right=TreeNode(2))
root.right.left = TreeNode(3)

print(inorderTraversal(root))
print(preorder(root))
print(postorderTraversal(root))

# for insert mode
