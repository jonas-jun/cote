'''
diameter (트리 내에서 가장 긴 node 간의 거리) 을 구해라

solution
check함수: subroot 기준으로 왼쪽과 오른쪽 가장 긴 leaf까지의 거리를 찾아주고 (BFS, cnt) -> max_left+max_right
helper함수: 모든 node를 정점으로 check를 돌려줌 (recursive)

solution2를 한번 읽어보기!
solution1을 전체 recursive하게 짠 코드

https://leetcode.com/problems/diameter-of-binary-tree/submissions/
'''

from Project4.BST_Helper import create_linked_bst
from collections import deque
def diameterOfBT(root):

    def check(start):
        # left side
        if not start.left:
            max_left = 0
        else:
            queue = deque([(start.left, 1)]) # (node, cnt)
            max_left = 0
            while queue:
                node, cnt = queue.popleft()
                if not node.left and not node.right:
                    max_left = max(max_left, cnt)
                if node.left:
                    queue.append((node.left, cnt+1))
                if node.right:
                    queue.append((node.right, cnt+1))
        # right side
        if not start.right:
            max_right = 0
        else:
            queue = deque([(start.right, 1)]) # (node, cnt)
            max_right = 0
            while queue:
                node, cnt = queue.popleft()
                if not node.left and not node.right:
                    max_right = max(max_right, cnt)
                if node.left:
                    queue.append((node.left, cnt+1))
                if node.right:
                    queue.append((node.right, cnt+1))
        return max_left + max_right

    ans = 0
    def helper(start):
        nonlocal ans
        ans = max(ans, check(start))
        if start.left:
            helper(start.left)
        if start.right:
            helper(start.right)
    helper(root)
    return ans

def diameterOfBT2(root):
    rst = 0
    def children(subroot):
        nonlocal rst
        n_left, n_right = 0, 0
        if subroot.left:
            n_left = 1 + max(children(subroot.left))
        if subroot.right:
            n_right = 1 + max(children(subroot.right))
        rst = max(rst, n_left+n_right)
        return n_left, n_right
    children(root)
    return rst

t1 = create_linked_bst([1,2,3,4,5])
t2 = create_linked_bst([1,2])

print(diameterOfBT(t1))
print(diameterOfBT(t2))
print(diameterOfBT2(t1))
print(diameterOfBT2(t2))