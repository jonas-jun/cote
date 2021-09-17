"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode
def P3(head: ListNode) -> ListNode: 

    if head is None:
        return None
    if head.next is None:
        return head
    
    # Find the number of nodes
    cnt = 0
    curr = head
    midNode = head
    while curr != None:
        curr = curr.next        
        cnt += 1

    #Divide into left and right
    mid = cnt // 2    
    left= head
    
    curr = head
    cnt = 0
    while cnt < mid-1:
        curr = curr.next
        cnt += 1
    right = curr.next
    curr.next = None 
    
    ##### Write your Code Here #####

    return head
    ##### End of your code #####


