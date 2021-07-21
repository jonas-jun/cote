'''
원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수), 이는 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있습니다.

{{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로

{{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
{{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
{{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.

특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.

[입출력 예]
s	result
"{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
"{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
"{{20,111},{111}}"	[111, 20]
"{{123}}"	[123]
"{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]

PSEUDO
string을 받아서 [[2], [2,1], [2,1,3], [2,1,3,4]] 형태로 만들기 (re.findall)
길이가 짧은 순서대로 sorted, key=len

ans = dict() # dict를 사용하는 이유는 O(1)로 in 사용하기 위해서
for set1 in sort:
    for num in set1:
        if int(num) not in ans: ans[int(num)] = True
        else: pass
return list(ans.keys())

https://programmers.co.kr/learn/courses/30/lessons/64065
'''

import re
def solution(s):
    split_list = s.split('},')
    lists = list()
    lists.append(re.findall('[0-9]+', split_list[0]))
    lists.append(re.findall('[0-9]+', split_list[-1]))
    for str_ in split_list[1:-1]:
        lists.append(re.findall('[0-9]+', str_))
    
    sort = sorted(lists, key=lambda x: len(x))
    ans = dict()
    for set1 in sort:
        for num in set1:
            if num in ans:
                continue 
            ans[int(num)] = True
    return list(ans.keys())

# for insert mode