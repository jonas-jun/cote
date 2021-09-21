'''
LL에서 주어진 두 index(left, right) 사이의 노드들을 reverse하여 LL의 head return

ex1
1,2,3,4,5,  left=2, right=4
1,4,3,2,5

sol.
Sentinel이라는 노드를 만들어서 앞에 붙여줘서 1번 부터 바뀌어야 할 상황 대응
left-1부터 right까지 stack에 담아두고
next_one = right.next
before_one = stack.popleft()
그 다음 stack의 것들을 뒤에서부터 next_one에 줄줄이 연결
마지막으로 sentinel.next를 return

https://leetcode.com/problems/reverse-linked-list-ii/
'''

from typing import Optional
from Project2.linked_list_helper import create_linked_list, print_linked_list
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if left == right: return head
    if not head.next: return head
    sentinel = ListNode(val=None, next=head)
    cur = sentinel
    idx = 0
    check = False
    stack = deque()
    while cur:
        if idx==left-1:
            check=True
        if check:
            stack.append(cur)
        if idx==right:
            next_one = cur.next
            break
        cur = cur.next
        idx += 1
    
    before_one = stack.popleft()
    cur = before_one
    while stack:
        cur.next = stack.pop()
        cur = cur.next
    cur.next = next_one
    return sentinel.next

t1 = [1,2,3,4,5,6,1,3,5]
print_linked_list(reverseBetween(create_linked_list(t1), 2, 5), list())
