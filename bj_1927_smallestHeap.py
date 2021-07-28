'''
널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

heapq.heappush(list, val): list에 val을 insert하고 최소값을 list[0]에 둔다
heapq.heappop(list): list에서 최소값==list[0]을 pop하고 다시 최소값이 맨 앞에 오게끔 정렬한다.
최소값이 0번에 오지만 2,3번째 최소값이 [1] [2]로 오지는 않는다.

예제 입력 1 
9
0
12345678
1
2
0
0
0
0
32
예제 출력 1 
0
1
2
12345678
0

https://www.acmicpc.net/problem/1927
'''

import heapq
from typing import List

def sol(list1: List):
    queue = list()
    for val in list1:
        if val == 0:
            if queue: print(heapq.heappop(queue))
            else: print(0)
        else:
            heapq.heappush(queue, val)

# for test
t1 = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
sol(t1)

# not use heap
def insert(val, queue):
    queue.appendleft(val)
    for i in range(len(queue)-1):
        if queue[i] > queue[i+1]:
            queue[i], queue[i+1] = queue[i+1], queue[i]
    return queue