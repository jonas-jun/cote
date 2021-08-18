'''
비슷한 단어 쌍의 수 구하기
단어 abca와 zbxz는 비슷하다. 그 이유는 a를 z로 바꾸고, b는 그대로 b, c를 x로 바꾸면, abca가 zbxz가된다.
단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 구하는 프로그램을 작성하시오.

Solution
- 알파벳이 아니라 숫자로 바꿔서 비교해보자 'aabca'와 'kkfpk'는 모두 11231이 될 수 있다.
- 같은 문자들이 2개 4개가 있다면 2C2 + 4C2가 한쌍을 고르는 방법이다.
- 또는 for i in range(len(words)-1):
    for j in range(i+1, len(words)): 로 돌면서 같으면 ans += 1 해주는 방법도 있다.
'''

from typing import List
def solution(words: List) -> int:
    
    def change(word: str) -> str:
        dic = dict()
        val = 0
        ans = str()
        for char in word:
            if char in dic:
                ans += dic[char]
            else:
                val+=1
                dic[char] = str(val)
                ans += str(val)
        return ans

    def fac2(val):
        return (val * (val-1)) / 2
    
    words = list(map(change, words))

    vocab = dict()
    for word in words:
        if word in vocab: vocab[word]+=1
        else: vocab[word]=1
    return sum([fac2(vocab[key]) for key in list(vocab.keys())])
    
    # ans = 0
    # for i in range(len(words)-1):
    #     for j in range(i+1, len(words)):
    #         if words[i]==words[j]:
    #             ans += 1
    # return ans

# for test
test = ['aa', 'ab', 'bb', 'cc', 'cd']
print(solution(test))