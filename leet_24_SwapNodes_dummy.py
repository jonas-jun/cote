'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Input: head = [1,2,3,4]
Output: [2,1,4,3]

PSEUDO
use dummy(head node) not to use if code

start = Node(0) # dummy
cur = start
start.next = head

while cur.next and cur.next.next:
    one = cur.next
    two = cur.next.next
    cur.next = two 0 -> 2
    one.next = two.next 1 -> 3
    two.next = one 2 -> 1
    cur = one 0 -> 2 -> 1 -> 3, cur: 1

return start.next
'''

def swapPairs(head):
    if not head:
        return head
    if not head.next:
        return head
    
    start = ListNode(0)
    start.next = head
    cur = start

    while cur.next and cur.next.next:
        one = cur.next
        two = one.next
        cur.next = two
        one.next = two.next
        two.next = one
        cur = one
    
    return start.next

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

t1 = arr_to_linked([1,2,3,4])
t2 = arr_to_linked([1,2,3,4,5])
print(linked_to_arr(swapPairs(t1)))
print(linked_to_arr(swapPairs(t2)))

# for insert mode