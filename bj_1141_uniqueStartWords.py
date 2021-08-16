'''
접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다.
예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다.
반면에, {hello, hell}, {giant, gig, g}는 접두사 X 집합이 아니다.
단어가 N개 주어질 때, 이 단어의 부분 집합 중 접두사X 집합이면서 크기가 가장 큰 것을 출력

예제 입력 1 
6
hello
hi
h
run
rerun
running

예제 출력 1 
4

PSEUDO
길이로 정렬 (짧은 순)
ans = list()
addto=True
짧은 문자열부터 뒤로 loop을 돌면서 startswith에 걸리면 addto=False, break
다 돌고 addto: ans.append()
위 과정을 전체 list에서 할 게 아니라 같은 char로 시작하는 단어들 안에서만 진행하면 됨

https://www.acmicpc.net/problem/1141
'''

from typing import List
from collections import defaultdict

def solution(words: List) -> List:
    ans = list()
    words.sort(key=lambda x: len(x))
    words_dict = defaultdict(lambda: list())
    for word in words:
        words_dict[word[0]].append(word)
    
    def check(wo_list):
        nonlocal ans
        for idx in range(len(wo_list)): # 맨 끝 단어까지
            addto = True
            for j in range(idx+1, len(wo_list)):
                if wo_list[j].startswith(wo_list[idx]):
                    addto = False
                    break
            if addto: ans.append(wo_list[idx])
    
    for key in list(words_dict.keys()):
        check(words_dict[key])
    
    return len(ans)

# for test
test = ['hello', 'hi', 'h', 'run', 'rerun', 'running']
test2 = ['hello', 'goodbye', 'giant', 'hi']
print(solution(test))
print(solution(test2))