'''
Given the head of a linked list, return the list after sorting it in ascending order.
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

Merge Sort와 유사한 방식을 활용하여 정렬

전체 길이 파악
mid_idx를 기준으로 나눔
merge 함수 구현
recursive 하게 끝에서부터 merge

https://leetcode.com/problems/sort-list
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
        
    if not head or not head.next: return head
    
    cur = head
    length = 0
    while cur:
        length += 1
        cur = cur.next
    mid_idx = length//2
    
    # split two    
    cur = head
    i = 0
    while i < mid_idx-1:
        i += 1
        cur = cur.next
    left = head
    right = cur.next
    cur.next = None

    def merge(head1, head2):
        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next
        cur = head
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                cur = cur.next
                head1 = head1.next
            else:
                cur.next = head2
                cur = cur.next
                head2 = head2.next
        if head1: cur.next = head1
        if head2: cur.next = head2
        return head

    return merge(sortList(left), sortList(right))