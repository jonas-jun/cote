'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

PSEUDO
basic DFS
end comdition: leaf(not have any child)

check point! -> do not affect temp_sum outside of definition (nonlocal!!)

https://leetcode.com/problems/path-sum/
'''

def hasPathSum(root, targetSum):
    if not root: return False
    ans = False

    def dfs_helper(root, temp_sum):
        nonlocal ans, targetSum
        temp_sum += root.val
        if not root.left and not root.right:
            if temp_sum == targetSum:
                ans = True
            return
        
        togo = [node for node in [root.left, root.right] if node]
        for node in togo:
            #cur_sum = temp_sum
            dfs_helper(node, temp_sum) # checkpoint!!!
    dfs_helper(root, 0)
    return ans

# for test
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree1 = TreeNode(5, left=TreeNode(4, left=TreeNode(11, left=TreeNode(7), right=TreeNode(2))), right=TreeNode(8, left=TreeNode(13),
    right=TreeNode(4, right=TreeNode(1))))

print(hasPathSum(tree1, 22))

# for insert mode