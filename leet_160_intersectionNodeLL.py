'''
두 LL head가 주어졌을 때, intersection Node가 존재하면 그걸 return, 없으면 return None

sol
stack 이용
한칸씩 움직이면서 stack에 존재하는 node가 나오면 return node
아니면 stack에 넣고 다음 칸으로 이동
'''

def getIntersectionNode(headA, headB):
    curA, curB = headA, headB
    stack = set()
    while curA or curB:
        if curA:
            if curA in stack: return curA
            stack.add(curA)
            curA = curA.next
        if curB:
            if curB in stack: return curB
            stack.add(curB)
            curB = curB.next