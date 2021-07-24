'''
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → L(n - 1) → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → L(n - 1) → L2 → L(n - 2) → …

정의 그대로 i번째와 len(LL)-i번째가 이어지도록 해야 쉽다..!

PSEUDO 1
prev를 달아서 규칙대로 이동

PSEUDO 2
임시 list에 node들을 첫 순서대로 넣어두고 i번째 뒤에 len(LL)-i번째를 연결

https://leetcode.com/problems/reorder-list
'''
# for test
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# solution
def sol_1(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    cur = head
    # make prev
    while cur.next:
        cur.next.prev = cur
        cur = cur.next

    right = cur
    left = head
    while left != right and left.next != right:
        left_temp = left.next
        right_temp = right.prev
        right_temp.next = right.next
        if right.next: right.next.prev = right_temp
        left.next = right
        right.prev = left
        right.next = left_temp
        left_temp.prev = right

        left = left_temp
        right = right_temp
        
    return head

def sol_2(head):
    if head.next:
        a = list()
        current = head
        # list에 node들을 다 담아두기
        while current:
            a.append(current)
            current = current.next
        
        val = len(a) // 2 # 2

        k = 0
        i = 1

        while head and k < val: # 1 < 2
            current = head.next # 
            head.next = a[len(a)-i] # 맨 끝 노드
            head = head.next # 4
            head.next = current # 4->2
            head = head.next
            k += 1
            i += 1 # i = 2
        head.next = None
    return a[0]

# for test
t1 = [1,2,3,4]
t1_head = arr_to_linked(t1)
t2 = [1,2,3,4,5]
t2_head = arr_to_linked(t2)

from time_check import check
print(check(sol_1, t1_head))
print(check(sol_2, t1_head))

t1 = [1,2,3,4]
t1_head = arr_to_linked(t1)
t2 = [1,2,3,4,5]
t2_head = arr_to_linked(t2)
print(check(sol_1, t2_head))
print(check(sol_2, t2_head))

# for insert mode