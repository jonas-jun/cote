'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

PSEUDO sol2
구분자를 ''.join(sorted(str_))으로 list를 만들고
unique한 구분자들을 key로 dict를 만들어두고
idx를 len(strs)까지 돌면서 ans_dict[구분자[i]].append(strs[i])

https://leetcode.com/problems/group-anagrams
'''

def sol1(strs):

    def make_count(str_):
        ans = dict()
        for char in str_:
            if char in ans:
                ans[char] += 1
            else: ans[char] = 1
        return ans

    def check_ana(str1, str2):
        return make_count(str1)==make_count(str2)

    vocab = dict()
    for str_ in strs:
        check = False
        for key in vocab:
            if check_ana(str_, key):
                vocab[key].append(str_)
                check = True
                break
        if not check:
            vocab[str_] = [str_]
    return [vocab[key] for key in vocab]

def sol2(strs):
    keys = [''.join(sorted(str_)) for str_ in strs] # nklogk (k: 가장 큰 str의 길이)
    ans_dict = dict()
    for key in set(keys):
        ans_dict[key] = list()
    for i in range(len(keys)): # O(n)
        ans_dict[keys[i]].append(strs[i])
    return [ans_dict[key] for key in ans_dict]

# for test
from time_check import check

t1 = ["eat","tea","tan","ate","nat","bat"]
t2 = [""]
t3 = ['a']

print(check(sol1, t1))
print(check(sol2, t1))
print(check(sol1, t2))
print(check(sol2, t2))
print(check(sol1, t3))
print(check(sol2, t3))

# for insert mode