'''
3x3의 표에 영문자가 하나씩 있으며, 이 영문자들을 사용해서 최대한 많은 영단어를 만드는 것이 목표
단어는 최소 4글자 이상이어야 하며, 한 글자당 최대 1번만 사용할 수 있다. 따라서 10글자 이상의 단어는 만들 수 없다.
또한, 표의 정중앙에 있는 글자는 반드시 사용해야 한다.
단어들을 모두 담고 있는 사전과 퍼즐판에 배치할 9개의 문자가 주어졌을 때, 문제를 푸는 프로그램을 작성
puzzle 단어들은 배치를 마음대로 할 수 있음

dictionary = [APPLE,BANANA,BANE,BRILLIANT,LINT,PALE,PROBLEM,TILL,TRILL]
puzzles = [LARBITNLI, LEPAPBNNA, LEPAPBNAM]

https://www.acmicpc.net/problem/1148

Solution
사전과 puzzle 문자 9개 한세트가 주어졌을 때,
사전에서 puzzle로 만들 수 있는 단어들만 우선 추출 (counter 활용)
puzzle 문자 중 하나씩 가운데에 놓는다 생각하고, 가능한 단어들의 개수 파악
최대, 최소 뽑아서 return 
'''

def build_counter(s:str):
    rst = dict()
    for char in s:
        if char in rst: rst[char]+=1
        else: rst[char]=1
    return rst

def solution(words, tgt):

    possible = list()
    ans = dict()
    tgt = build_counter(tgt)
   
    # 가능한 단어만 뽑아보기
    for word in words:
        p = True
        word = build_counter(word)
        for char in word:
            if char not in tgt or word[char]>tgt[char]:
                p = False
                break
        if not p: continue
        possible.append(word)

    # puzzle 문자 하나씩 가운데로 보냈을 때, 가능한 단어들 찾기 
    for char in tgt:
        temp = 0
        for word in possible:
            if char not in word: # 중간 문자는 꼭 포함해야 하므로.
                continue
            temp += 1
        ans[char] = temp

    ans = ans.items()
    max_ = max(ans, key=lambda x:x[1])[1]
    min_ = min(ans, key=lambda x:x[1])[1]
    max_char, min_char = list(), list()
    for pair in ans:
        if pair[1]==max_: max_char.append(pair[0])
        if pair[1]==min_: min_char.append(pair[0])
    
    return [''.join(sorted(min_char)), str(min_), ''.join(sorted(max_char)), str(max_)]

dictionary = ['APPLE','BANANA','BANE','BRILLIANT','LINT','PALE','PROBLEM','TILL','TRILL']
puzzles = ['LARBITNLI', 'LEPAPBNNA', 'LEPAPBNAM']

for puzzle in puzzles:
    print(' '.join(solution(dictionary, puzzle)))