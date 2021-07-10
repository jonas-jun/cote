'''
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
 {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z']}

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

https://leetcode.com/problems/letter-combinations-of-a-phone-number/

PSEUDO
"combination = old_combi * new one"

make combination of lists [a,b,c], [d,e] -> [ad, bd, cd, ae, be, ce]
make_comib(make_combi(vocab[a], vocab[b]), vocab[c])...

[ad, bd, cd, ae, be, cd], [h, i] -> [adh, bdh, cdh, aeh, ...] length 12
'''

from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return None
    vocab = {
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h','i'],
    '5': ['j','k','l'],
    '6': ['m','n','o'],
    '7': ['p','q','r','s'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z']}

    def combi_lists(list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1        
        res = list()
        for i in range(len(list1)):
            for j in range(len(list2)):
                res.append(list1[i]+list2[j])
        return res

    ans = list()
    for char in digits:
        ans = combi_lists(ans, vocab[char])
    return ans

# test
t1 = '23'
t2 = ''
t3 = '2'

print(letterCombinations(t1))
print(letterCombinations(t2))
print(letterCombinations(t3))

# for insert mode