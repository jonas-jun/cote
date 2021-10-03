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


'''
zigzag order level traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
'''

def zigzagLevelOrder(root) -> List[List[int]]:
    if not root: return list()
    rst = list()
    rst.append([root.val])
    q = list()
    q.append([root])
    reverse = True # 둘째줄은 reverse
    while q:
        level = list()
        for node in q.pop():
            if not node: continue
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        if not any(level): return rst
        q.append(level)
        if reverse:
            rst.append([n.val for n in level][::-1])
        else:
            rst.append([n.val for n in level])
        reverse = not reverse