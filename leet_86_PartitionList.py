'''
LL에서 주어진 x보다 작은 값들을 앞쪽에, 크거나 같은 값들을 뒤쪽에 배치
순서는 원래 순서 그대로 사용해야 함

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Input: head = [1,2], x = 3
Output: [1,2]

Solution
smaller, larger = ListNode(0) 만들어두고
loop 돌면서 smaller와 larger에 붙임.
smaller와 larger의 head를 두번째로 바꿔주고
smaller는 끝을 larger_head로 연결
larger는 끝을 None으로 바꿔줌
return smaller_head

https://leetcode.com/problems/partition-list
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional, List
def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:

    head_smaller = ListNode(val=0)
    head_larger = ListNode(val=0)
    smaller = head_smaller
    larger = head_larger
    
    if not head: return head
    while head:
        if head.val < x:
            smaller.next = head
            smaller = smaller.next
            head = head.next
        else:
            larger.next = head
            larger = larger.next
            head = head.next
    
    head_smaller = head_smaller.next
    head_larger = head_larger.next
    
    smaller.next = head_larger
    larger.next = None
    
    return head_smaller if head_smaller else head_larger
    
def list_to_LL(arr: List) -> ListNode:
    head = ListNode(arr[0])
    cur = head
    for val in arr[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def LL_to_list(head: ListNode) -> List:
    rst = list()
    while head:
        rst.append(head.val)
        head = head.next
    return rst

print(LL_to_list(partition(list_to_LL([1,4,3,2,5,2]), 3)))

