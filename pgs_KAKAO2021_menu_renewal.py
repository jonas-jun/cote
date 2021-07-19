'''
레스토랑을 운영하던 스카피는 코로나19로 인한 불경기를 극복하고자 메뉴를 새로 구성하려고 고민하고 있습니다.
기존에는 단품으로만 제공하던 메뉴를 조합해서 코스요리 형태로 재구성해서 새로운 메뉴를 제공하기로 결정했습니다.
어떤 단품메뉴들을 조합해서 코스요리 메뉴로 구성하면 좋을 지 고민하던 "스카피"는 이전에 각 손님들이 주문할 때 가장 많이 함께 주문한 단품메뉴들을 코스요리 메뉴로 구성하기로 했습니다.
단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.

예를 들어, 손님 6명이 주문한 단품메뉴들의 조합이 다음과 같다면,
(각 손님은 단품메뉴를 2개 이상 주문해야 하며, 각 단품메뉴는 A ~ Z의 알파벳 대문자로 표기합니다.)

손님 번호	주문한 단품메뉴 조합
1번 손님	A, B, C, F, G
2번 손님	A, C
3번 손님	C, D, E
4번 손님	A, C, D, E
5번 손님	B, C, F, G
6번 손님	A, C, D, E, H
가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

코스 종류	메뉴 구성	설명
요리 2개 코스	A, C	1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
요리 3개 코스	C, D, E	3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
요리 4개 코스	B, C, F, G	1번, 5번 손님으로부터 총 2번 주문됐습니다.
요리 4개 코스	A, C, D, E	4번, 6번 손님으로부터 총 2번 주문됐습니다.

각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, "스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때,
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.

[제한사항]
정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

PSEUDO
from itertools import combinations
from collections import defaultdict

combi_dict = defaultdict(lambda: dict())
orders = list(map(sorted, orders))

for nums in course: # 각 메뉴 개수마다
    for o in orders: # 각 주문 마다 메뉴 개수만큼 combination을 뽑아내고
        combis = list(map(lambda x: ''.join(x), combinations(o, nums))))
        for c in combis:
            if c not in combi_dict[nums]: combi_dict[nums][c] = 1 # 각 메뉴수 별로 조합 count dictionary 추가 (2개면, 2개 메뉴 조합들을 카운트)
            else: combi_dict[nums][c] += 1
ans = list()
for num in combi_dict:
    sort = sorted(combi_dict[num].items(), reverse=True)
    max_cnt = sort[0][-1]
    if max_cnt == 1:
        continue
    for menu, cnt in sort:
        if cnt == max_cnt: ans.append(menu)
        else break 
'''

from itertools import combinations
from collections import defaultdict, Counter

def sol(orders, course):
    orders = list(map(sorted, orders))
    combi_dict = defaultdict(lambda: dict())
    for nums in course:
        for o in orders:
            combis = list(map(lambda x: ''.join(x), combinations(o, nums)))
            for c in combis:
                if c not in combi_dict[nums]: combi_dict[nums][c] = 1
                else: combi_dict[nums][c] += 1

    ans = list()
    for num in combi_dict:
        sort = sorted(combi_dict[num].items(), key=lambda x: x[1], reverse=True)
        max_cnt = sort[0][-1]
        if max_cnt == 1:
            continue
        for menu, cnt in sort:
            if cnt == max_cnt: ans.append(menu)
            else: break
    
    return sorted(ans)

def sol_counter(orders, course):
    orders = list(map(sorted, orders))
    combi_dict = defaultdict(lambda: list())
    for nums in course:
        temp = list()
        for o in orders:
            combis = list(map(lambda x: ''.join(x), combinations(o, nums)))
            temp += combis
            combi_dict[nums] = Counter(temp).most_common()
    ans = list()
    for num in combi_dict:
        if combi_dict[num]:
            max_cnt = combi_dict[num][0][-1]
            if max_cnt == 1:
                continue
            for menu, cnt in combi_dict[num]:
                if cnt == max_cnt: ans.append(menu)
                else: break
    
    return sorted(ans)

# test
t1_orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
t1_course = [2,3,4]

t2_orders = ["XYZ", "XWY", "WXA"]
t2_course = [2, 3, 4]

from time_check import check
print('case 1')
print(check(sol, t1_orders, t1_course))
print(check(sol_counter, t1_orders, t1_course))

print('case 2')
print(check(sol, t2_orders, t2_course))
print(check(sol_counter, t2_orders, t2_course))

# for insert mode