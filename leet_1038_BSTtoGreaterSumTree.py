'''
GreaterSumTree: original key plus tue sum of all keys greater than the original key in BST
더 큰 수들의 합 + 본인

solution
BST를 inorder traversal로 node들을 모은다 (val의 정렬이 된 상태)
- 오른쪽->본인->왼쪽 순으로 돌리면 reverse하게 모인다.
가장 큰 쪽, 오른쪽부터 각각 val를 바꿔주면 된다.

https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree
'''

def bstToGst(root):
    # in-order traversal
    nodes = list()
    def in_order_rvs(start):
        nonlocal nodes
        if not start: return
        in_order_rvs(start.right)
        nodes.append(start)
        in_order_rvs(start.left)
    in_order_rvs(root)

    # change vals to cum_vals
    cum = 0
    for idx in range(len(nodes)):
        cum += nodes[idx].val
        nodes[idx].val = cum
    return root

# for test
from Project4.BST_Helper import create_linked_bst
test = create_linked_bst([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])
print(bstToGst(test))