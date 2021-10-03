'''
subtree의 합 중 가장 빈도가 높은 합을 return
같은 최대빈도의 합이 여러 개일 경우 순서 상관이 함께 list로 return
- 왼쪽 subtree의 합
- 오른쪽 subtree의 합
- 전체 root까지 포함한 tree

https://leetcode.com/problems/most-frequent-subtree-sum
'''
from collections import defaultdict
def findFrequentTreeSum(root):
    counter = defaultdict(lambda:0)
    def helper(subroot):
        nonlocal counter
        if not subroot.left and not subroot.right:
            counter[subroot.val]+=1
            return subroot.val
        sum_left, sum_right = 0,0
        if subroot.left:
            sum_left = helper(subroot.left)
        if subroot.right:
            sum_right = helper(subroot.right)
        total = subroot.val + sum_left + sum_right
        counter[total]+=1
        return total
    helper(root)
    max_val = max(counter.values())
    return [key for key in counter if counter[key]==max_val]

# for test
from Project4.BST_Helper import create_linked_bst
t1 = [5,2,-5]
t2 = [236, 104, 701, None, 227, None, 911]
print(findFrequentTreeSum(create_linked_bst(t1)))
print(findFrequentTreeSum(create_linked_bst(t2)))