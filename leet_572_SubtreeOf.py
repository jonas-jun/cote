'''
Subtree of Another tree
한 트리가 다른 한쪽의 서브트리가 될 수 있는지 판단?

Sol
check subtree: subtree인지 확인하는 함수
traverse: 돌면서 val가 같은 노드는 만나면 거기서부터 check sub tree

https://leetcode.com/problems/subtree-of-another-tree
'''

def isSubtree(root, subRoot) -> bool:
        
    def checkSubTree(proot, qroot):
        if not proot and not qroot:
            return True
        if not proot or not qroot:
            return False
        
        if proot.val != qroot.val:
            return False
        return checkSubTree(proot.left, qroot.left) and checkSubTree(proot.right, qroot.right)
    
    
    def traverse(root):
        if not root:
            return False
        ret = False
        if root.val == subRoot.val:
            ret = checkSubTree(root, subRoot) or checkSubTree(root.left, subRoot) or checkSubTree(root.right, subRoot)
        return ret or traverse(root.left) or traverse(root.right)
    
    return traverse(root)


def isSubtree(root, subroot):
    if not root: return False
    def compare(root, subroot):
        if not root and not subroot: return True
        if not root or not subroot: return False
        return root.val==subroot.val and compare(root.left, subroot.left) and compare(root.right, subroot.right)
    return compare(root, subroot) or isSubtree(root.left, subroot) or isSubtree(root.right, subroot)