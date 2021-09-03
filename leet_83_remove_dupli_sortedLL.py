'''
오름차순 정렬된 Linked List에서 중복된 밸류를 갖고 있는 노드들을 제거
연속해서 중복된 노드들을 처리할 때 어떻게 해야하는지. 아래 코드로 기억

https://leetcode.com/problems/remove-duplicates-from-sorted-list
'''

def deleteDuplicates(self, head):
    #if not head or not head.next: return head
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            temp = cur.next.next
            cur.next = temp # 뒤로 넘어가지 않고 한번 더 다음 거 체크하는 게 포인트
        else: cur = cur.next
    return head