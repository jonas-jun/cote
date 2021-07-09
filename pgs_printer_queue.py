'''
일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다.
이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.
예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

입출력 예
priorities	location	return
[2, 1, 3, 2]	2	1
[1, 1, 9, 1, 1, 1]	0	5

https://programmers.co.kr/learn/courses/30/lessons/42587

PSEUDO
idx, priorities, sorted를 deque로 만들기
count 0
while prior: 또는 while True:
    val = prior.popleft() prior 가장 앞 숫자가
    i = idx.popleft()
    if sort[0] 가장 큰 숫자와 같으면:
        count+=1
        if idx가 location과 같으면:
            return count
        sort.popleft() 방금 뽑았던 가장 큰 숫자 제거
    else:
        idx.append(i)
        prior.append(val) idx와 value를 다시 맨 뒤에 붙여주기

Solution3 is the best!
'''
from collections import deque
def solution(priorities, location):
    prior = deque(priorities)
    idx = deque(range(len(priorities)))
    sort = deque(sorted(priorities, reverse=True))
    cnt = 0
    
    while prior:
        val = prior.popleft()
        i = idx.popleft()
        if val == sort[0]:
            cnt += 1
            if i == location:
                return cnt
            sort.popleft()
        else:
            idx.append(i)
            prior.append(val)

# test
t1 = [2,1,3,2]
t1_loc = 2
t2 = [1,1,9,1,1,1]
t2_loc = 0

from time_check import check
print('solution 1')
print(check(solution, t1, t1_loc))
print(check(solution, t2, t2_loc))

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

print('solution 2')
print(check(solution2, t1, t1_loc))
print(check(solution2, t2, t2_loc))

def solution3(priorities, location):
    sort = deque(sorted(priorities, reverse=True))
    priorities = deque([(idx, val) for idx, val in enumerate(priorities)]) # [(0, 2), (1, 1), ...]
    cnt = 0
    while priorities:
        cur = priorities.popleft()
        if cur[1] == sort[0]:
            cnt += 1
            if cur[0] == location:
                return cnt
            sort.popleft()
        else:
            priorities.append(cur)

print('solution 3')
print(check(solution3, t1, t1_loc))
print(check(solution3, t2, t2_loc))

# for insert mode