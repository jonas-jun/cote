'''
substring 중 애너그램 쌍의 개수
abba: [a,a], [ab,ba], [b,b], [abb, bba] -> 4

sol1
가능한 길이 loop:
    그 길이 가능한 substring 케이스들을 모두 counter 만들기
    counter loop(이중루프) 돌면서 같은 쌍의 개수 세기

sol2
가능한 길이 loop:
    그 길이 substring 두 쌍 찾는 loop (이중루프):
        두 개의 substring을 뽑으면 둘 다 counter를 만들어서 check anagram

sol2는 이중루프 돌면서 그 안에서 모두 다시 counter를 만들어주기 때문에 복잡도 증가

https://www.hackerrank.com/challenges/sherlock-and-anagrams
'''
def build_counter(s):
    rst = dict()
    for char in s:
        if char in rst: rst[char]+=1
        else: rst[char]=1
    return rst

def check_ana(s1, s2):
    return build_counter(s1) == build_counter(s2)

def sol1(s):
    ans = 0
    for length in range(1, len(s)):
        counters = list()
        for i in range(len(s)-length+1):
            counters.append(build_counter(s[i:i+length]))
        temp = 0
        for i in range(len(counters)-1):
            for j in range(i+1, len(counters)):
                if counters[i]==counters[j]:
                    temp += 1
        ans += temp
    return ans

def sol2(s):
    ans = 0
    for length in range(1, len(s)):
        for i in range(len(s)-length):
            for j in range(i+1, len(s)-length+1):
                if check_ana(s[i:i+length], s[j:j+length]):
                    ans += 1
    return ans

# for test
t1 = 'abdsdfasdddfifailuhkqq'
t2 = 'kkkk'

from time_check import check
print('case 1')
print(check(sol1, t1))
print(check(sol2, t1))
print('case 2')
print(check(sol1, t2))
print(check(sol2, t2))