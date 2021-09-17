#Helper functions: DO NOT MODIFY!!
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Create a linked list from a list, then return head node
def create_linked_list(l: list) -> ListNode:
    if len(l) == 0:
        return None
    
    start = ListNode(l[0])
    node = start
    
    for i in range(1, len(l)):
        node_new = ListNode(l[i])
        node.next = node_new
        node = node_new
    
    return start

#Print all values in the linked list
def print_linked_list(n: ListNode, l: list) -> None:
    if n is not None:
        l.append(n.val)
        print_linked_list(n.next, l)
    else:
        print(l)