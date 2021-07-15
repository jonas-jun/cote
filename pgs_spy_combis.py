'''
스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

입출력 예
clothes	return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	3

입출력 예 설명
예제 #1
headgear에 해당하는 의상이 yellow_hat, green_turban이고 eyewear에 해당하는 의상이 blue_sunglasses이므로
아래와 같이 5개의 조합이 가능합니다.

1. yellow_hat
2. blue_sunglasses
3. green_turban
4. yellow_hat + blue_sunglasses
5. green_turban + blue_sunglasses

PSEUDO
sol_1 # failed test case 1
개수로 dict를 만든다.
key를 가지고 combination을 뽑는다. 3가지라면 3C1, 3C2, 3C3
각 콤비네이션 loop을 돌면서 vocab에서 해당되는 value를 곱해주고, 그걸 모두 더한다.

sol_2
hat = [X, A, B]
shirt = [X, C, D]
shoes = [X, E]
where X means not wearing
num(hat) * num(shirt) * num(shoes) -1 (none case)
'''

from itertools import combinations as cbs
def sol_1(clothes):
    # make dict
    vocab = dict()
    for name, cat in clothes:
        if cat not in vocab:
            vocab[cat] = 1
        else:
            vocab[cat] += 1

    # make combinations
    ans = 0
    for num in range(1, len(vocab)+1):
        for com in list(cbs(vocab, num)):
            temp = 1
            for c in com:
                temp *= vocab[c]
            ans += temp
    return ans

def sol_2(clothes):
    vocab = dict()
    for name, cat in clothes:
        if cat in vocab:
            vocab[cat] += 1
        else: vocab[cat] = 1
    ans = 1
    for i in vocab.values():
        ans *= (i+1)
    return ans-1

# for test
from time_check import check
t1 = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"],
      ["green_turban", "headgear"]]
t2 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
print('test 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('test 2')
print(check(sol_1, t1))
print(check(sol_2, t2))

# for insert mode