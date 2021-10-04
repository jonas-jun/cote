'''
두 개의 tree root이 주어졌을 때, 두 tree가 same tree인지 판단해라.

sol
recursive하게 푸는데
- 둘 다 None이면 True
- 한쪽이 없으면 False
- 둘다 있는 경우에는?
    - 값이 같고. sametree(left), sametree(right) 모두 True이면 True
- 위 해당되지 않는 경우엔 False

https://leetcode.com/problems/same-tree
'''

def isSameTree(p, q):
    if not p and not q: return True
    if not p or not q: return False # 둘 중에 하나만 없는 경우
    # 모두 있는 경우
    if (p.val == q.val) and (isSameTree(p.left, q.left)) and (isSameTree(p.right and q.right)): return True
    return False