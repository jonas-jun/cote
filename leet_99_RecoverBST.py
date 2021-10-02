'''
BST 순서에 맞지 않도록 한쌍(2개) 노드가 swap 되어 있는데, 원래 순서대로 바꿔줘라

Sol
정렬 순서 그대로 arr에 담을 수 있게 inorder traversal을 한 후
왼쪽 첫번째 잘못된 순서, 오른쪽 첫번째 잘못된 순서 노드들의 val을 교환

https://leetcode.com/problems/recover-binary-search-tree
'''

def recoverTree(root) -> None:
    arr = list()
    def inorder_trav(subroot):
        nonlocal arr
        if not subroot: return
        inorder_trav(subroot.left)
        arr.append(subroot)
        inorder_trav(subroot.right)
    inorder_trav(root)
    left, right = None, None
    for i in range(len(arr)-1):
        if arr[i].val > arr[i+1].val:
            left = arr[i]
            break
    for i in range(len(arr)-1, 0, -1):
        if arr[i].val < arr[i-1].val:
            right = arr[i]
            break
    left.val, right.val = right.val, left.val

from Project4.BST_Helper import create_linked_bst

t1 = create_linked_bst([1,3,None,None,2])
recoverTree(t1)
print(t1.val)