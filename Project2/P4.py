"""
Singly Linked List를 받아서 순서를 뒤집는 함수 만들어라
4,2,1,3 --> 3,1,2,4
"""
from linked_list_helper import ListNode, create_linked_list, print_linked_list
def P4(head: ListNode) -> ListNode: 
    ##### Write your Code Here #####        
    '''
    1. node들을 stack에 append를 해주고
    2. tail을 할당해두고
    3. pop()을 해가면서 next로 연결
    4. 마지막 노드는 None으로 연결
    ''' 
    if not head: return head
    stack = list()
    while head:
        stack.append(head)
        head = head.next
    head = stack.pop()
    cur = head
    while stack:
        cur.next = stack.pop()
        cur = cur.next
    cur.next = None
    return head
    ##### End of your code #####

t1 = create_linked_list([4,2,1,3])
print_linked_list(P4(t1), list())