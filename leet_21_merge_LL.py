'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

https://leetcode.com/problems/merge-two-sorted-lists

PSEUDO
make dummy
cur, cur_l1, cur_l2
while cur_l1 and cur_l2:
    compare, and cur.next = smaller
    cur = smaller
    cur_l1 = smaller.next (if cur_l1 is smaller) 
while cur_l1:
while cur_l2:
return dummy.next
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    cur = dummy
    l1_cur, l2_cur = l1, l2
    while l1_cur and l2_cur:
        if l1_cur.val >= l2_cur.val:
            cur.next = l2_cur
            cur = l2_cur
            l2_cur = l2_cur.next
        else:
            cur.next = l1_cur
            cur = l1_cur
            l1_cur = l1_cur.next
    while l1_cur:
        cur.next = l1_cur
        cur = l1_cur
        l1_cur = l1_cur.next
    while l2_cur:
        cur.next = l2_cur
        cur = l2_cur
        l2_cur = l2_cur.next
    return dummy.next
            
# for test
from collections import deque     
def arr_to_linked(list_):
    root = ListNode(list_[0])
    if len(list_) == 1:
        return root
    cur = root
    queue = deque(list_[1:])
    while queue:
        cur.next = ListNode(queue.popleft())
        cur.next.prev = cur
        cur = cur.next
    return root

def linked_to_arr(root):
    cur = root
    ans = list()
    while cur.next:
        ans.append(cur.val)
        cur = cur.next
    ans.append(cur.val)
    return ans

t1_1 = arr_to_linked([1,2,4])
t1_2 = arr_to_linked([1,3,4])
print(linked_to_arr(mergeTwoLists(t1_1, t1_2)))

# for insert mode