'''
예를 들어 집합 A = {1, 2, 3}, 집합 B = {2, 3, 4}라고 할 때, 교집합 A ∩ B = {2, 3}, 합집합 A ∪ B = {1, 2, 3, 4}이 되므로, 집합 A, B 사이의 자카드 유사도 J(A, B) = 2/4 = 0.5가 된다.
집합 A와 집합 B가 모두 공집합일 경우에는 나눗셈이 정의되지 않으니 따로 J(A, B) = 1로 정의한다.

자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장할 수 있다. 다중집합 A는 원소 "1"을 3개 가지고 있고, 다중집합 B는 원소 "1"을 5개 가지고 있다고 하자.
이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다. 다중집합 A = {1, 1, 2, 2, 3}, 다중집합 B = {1, 2, 2, 4, 5}라고 하면,
교집합 A ∩ B = {1, 2, 2}, 합집합 A ∪ B = {1, 1, 2, 2, 3, 4, 5}가 되므로, 자카드 유사도 J(A, B) = 3/7, 약 0.42가 된다.

이를 이용하여 문자열 사이의 유사도를 계산하는데 이용할 수 있다. 문자열 "FRANCE"와 "FRENCH"가 주어졌을 때, 이를 두 글자씩 끊어서 다중집합을 만들 수 있다.
각각 {FR, RA, AN, NC, CE}, {FR, RE, EN, NC, CH}가 되며, 교집합은 {FR, NC}, 합집합은 {FR, RA, AN, NC, CE, RE, EN, CH}가 되므로, 두 문자열 사이의 자카드 유사도 J("FRANCE", "FRENCH") = 2/8 = 0.25가 된다.

https://programmers.co.kr/learn/courses/30/lessons/17677
'''

import re
def solution(str1, str2):
    def get_list(s):
        s = s.lower()
        return [s[i:i+2] for i in range(len(s)-1) if not re.search('[^a-z]', s[i:i+2])] # val -> for -> if
    list1, list2 = get_list(str1), get_list(str2)

    if (not list1) and (not list2):
        return 65536
    if (not list1) or (not list2):
        return 0

    # counter
    def get_counter(L):
        vocab = dict()
        for s in L:
            if s not in vocab:
                vocab[s] = 1
            else:
                vocab[s] += 1
        return vocab
    counter1, counter2 = get_counter(list1), get_counter(list2)

    # count
    n_i, n_u = 0, 0
    unique = set(list1+list2) # unique, only one
    for s in unique:
        if s in counter1 and s in counter2:
            n_i += min(counter1[s], counter2[s])
            n_u += max(counter1[s], counter2[s])
        elif s in counter1:
            n_u += counter1[s]
        else:
            n_u += counter2[s]

    return int((n_i / n_u) * 65536)

# test
t1_s1 = 'FRANCE+'
t1_s2 = 'french'

t2_s1 = 'handshake'
t2_s2 = 'shake hands'

t3_s1 = 'E=M*C^2'
t3_s2 = 'e=m*c^2'

from time_check import check

print(check(solution, t1_s1, t1_s2))
print(check(solution, t2_s1, t2_s2))
print(check(solution, t3_s1, t3_s2))

# for insert mode