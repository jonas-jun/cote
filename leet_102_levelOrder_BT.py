from typing import List


'''
주어진 Binary Tree의 level oreder traversal

sol
recursive하고, level별로 결과를 뽑아내려면 dict를 사용! defaultdict(lambda: list())

https://leetcode.com/problems/binary-tree-level-order-traversal
'''

from collections import defaultdict
def levelOrder(root) -> List:
    if not root: return list()
    rst = defaultdict(lambda: list())
    def helper(start, level):
        nonlocal rst
        rst[level].append(start.val)
        if start.left: helper(start.left, level+1)
        if start.right: helper(start.right, level+1)
    helper(root, 0)
    return rst.values()

from Project4.BST_Helper import create_linked_bst
t1 = [3,9,20,None,None,15,7]
print(levelOrder(create_linked_bst(t1)))