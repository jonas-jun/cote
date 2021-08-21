'''
A는 물고기의 크기
B의 0은 downstream, 1이 upstream
upstream은 오른쪽으로 거슬러 가는 물고기인데
오른편에서 왼쪽으로 오는 물고기 만나면 둘중 하나는 먹히게 됨
살아 남은 물고기 수는?

A = [4,3,2,1,5]
B = [0,1,0,0,0]
1번 물고기 (크기 3)가 거슬러 가면서 2,3을 먹고 4번에게 먹힘 -> 0번과 4번 남음

Solution
오른쪽에서부터 loop
stack = list()
B[i]==0: stack.append(A[i])
B[i]==1:
    stack에서 A[i]보다 작은 것들을 줄줄이 먹힘 kill += 1
    stack이 남아 있으면 A[i]가 먹혔다는 뜻이므로 kill += 1
    stack이 남아있지 않으면 A[i]가 끝까지 다 먹었다는 뜻이므로 kill 추가할 필요 없음
return len(A)-kill
'''

def solution(A,B):
    if sum(B)==0: return len(A)
    stack = list()
    kill = 0
    for i in range(len(A)-1, -1, -1):
        if B[i]==0:
            stack.append(A[i])
            continue
        if not stack:
            continue
        while stack[-1] < A[i]:
            stack.pop()
            kill += 1
            if not stack: break
        if stack: kill += 1
    return len(A)-kill

# for test
A = [4,3,2,1,5]
B = [0,1,0,0,0]
print(solution(A, B))