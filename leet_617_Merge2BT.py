'''
두 개의 tree merge

Solution
Recursive하게
한쪽만 존재하면 그쪽 값을 return
양쪽 모두 존재하면 새로 node를 만들어서 두 val 합한 것을 val에 할당해주고
left와 right를 재귀적으로 생성해서 붙여주면 된다.

https://leetcode.com/problems/merge-two-binary-trees/submissions
'''

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1: return root2
        if not root2: return root1
        root = TreeNode(0)
        root.val = root1.val + root2.val
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root