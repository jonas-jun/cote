'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

https://leetcode.com/problems/remove-nth-node-from-end-of-list

PSEUDO 1.
get arr from LL
pop arr[-n]
make arr to LL

PSEUDO 2.
make all nodes have .prev and go to Last node
get Nth node from Last
cur.prev.next = cur.next

roughly, O(3n) vs O(1/2*n)
'''
# for test
from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def sol1(head: ListNode, n: int):
    if not head.next:
        return None
    arr = linked_to_arr(head)
    arr.pop(-n)
    return arr_to_linked(arr)

def sol2(head: ListNode, n: int):
    def make_prev(root):
        root.prev = None
        cur = root
        while cur.next:
            cur.next.prev = cur
            cur = cur.next
        return cur
    
    if not head.next:
        return None
    cur = make_prev(head)
    for i in range(n-1):
        cur = cur.prev
    if cur.prev:    cur.prev.next = cur.next
    else:   return cur.next
    return head

# for test
test1 = [1,2,3,4,5,9,8,7,6,5,12,13,1]
test1 = arr_to_linked(test1)
test2 = [1,2]
test2 = arr_to_linked(test2)
test3 = [1]
test3 = arr_to_linked(test3)

from time_check import check
print('case 1')
print(check(sol1, test1, 3))
print(check(sol2, test1, 3))
print(linked_to_arr(sol2(test1, 3)))
print('case 2')
print(check(sol1, test2, 2))
print(check(sol2, test2, 2))
print(linked_to_arr(sol2(test2, 2)))
print('case 3')
print(check(sol1, test3, 1))
print(check(sol2, test3, 1))
print(linked_to_arr(sol2(test3, 1)))

# for insert mode