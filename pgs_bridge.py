'''
트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다.
다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다.
단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다.
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
0	[]	[]	[7,4,5,6]
1~2	[]	[7]	[4,5,6]
3	[7]	[4]	[5,6]
4	[7]	[4,5]	[6]
5	[7,4]	[5]	[6]
6~7	[7,4,5]	[6]	[]
8	[7,4,5,6]	[]	[]
따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight,
트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3#

PSEUDO
bdg 상태를 [0]*bridge_length로 표현
while truck_weights:
    time += 1
    bdg.pop()
    if sum(bdg) + truck_weights[0]이 <= weight:
        bdg.appendleft(truck_weights.popleft())
    else:
        bdg.appendleft(0)
마지막 트럭이 막 올라간 상태로 끝나기 때문에 time + bridge_length를 return
--> 한 개의 케이스에서 시간 초과. 아마 popleft()를 자주 써서?

[sol_1]
다리 방향을 [7, 0] -> [0, 7] -> [4, 0] 이런식으로 왼쪽 -> 오른쪽 형태가 아니라 반대로 바꿔서
[0, 7] -> [7, 0] -> [0, 4] 처럼 오른쪽에서 왼쪽으로 건너가는 형태로 바꿔봄 (sol_1)
deque를 쓸 필요 없고 list에서 pop() 작업만 필요하기 때문!
--> 그러나 마찬가지로 시간초과, sum() method가 O(n)으로 이뤄지기 때문!!!

[sol_2]
sum 작업을 줄이기 위해 sum_bdg를 만들고 0이 아닌 값을 추가/제거 할 때마다 반영되게 하였음
--> 통과
'''

def sol_1(bridge_length, weight, truck_weights):
    time = 0
    t_id = 0
    bdg = [0]*bridge_length
    while t_id < len(truck_weights):
        time += 1
        bdg = bdg[1:]
        if sum(bdg) + truck_weights[t_id] <= weight:
            bdg.append(truck_weights[t_id])
            t_id += 1
        else:
            bdg.append(0)
    return time + bridge_length

def sol_2(bridge_length, weight, truck_weights):
    time = 0
    t_id = 0
    bdg = [0]*bridge_length
    sum_bdg = 0
    while t_id < len(truck_weights): 
        time += 1
        sum_bdg -= bdg[0]
        bdg = bdg[1:] 
        if sum_bdg + truck_weights[t_id] <= weight:
            bdg.append(truck_weights[t_id]) 
            sum_bdg += truck_weights[t_id]
            t_id += 1 
        else:
            bdg.append(0)
    return time + bridge_length

# test
length = 2
weight = 10
t_weights = [7,4,5,6]

from time_check import check
print(check(sol_1, length, weight, t_weights))
print(check(sol_2, length, weight, t_weights))

# for insert mode