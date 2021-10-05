'''
BST내에서 target을 찾아서 삭제하기
- target을 찾은 후 우측 subtree중 가장 작은 값으로 val을 바꿔주고 우측 트리에 대해 다시 substitute 노드를 지워주는 delete tree 함수를 재귀적으로 수행

https://leetcode.com/problems/delete-node-in-a-bst/submissions
'''
def get_smallest(self, subroot):
        if not subroot.left: return subroot
        return self.get_smallest(subroot.left)
        
def deleteNode(self, root, key: int):
    
    if not root: return root
    
    if root.val == key:
        if root.left and root.right:
            sub = get_smallest(root.right)
            root.val = sub.val
            root.right = deleteNode(root.right, sub.val)
            return root
        
        if not root.left and not root.right:
            return None
        if not root.left: return root.right
        if not root.right: return root.left
    
    elif root.val > key:
        root.left = deleteNode(root.left, key)
    else:
        root.right = deleteNode(root.right, key)
        
    return root