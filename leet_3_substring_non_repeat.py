'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = 'dvdf'
Output: 3 not 2, vdf

use list or use dictionary (in this case, list is better)
leetcode runtime
use dict: 1216ms & 14.3MB
use list: 84ms 14.2MB

https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

def sol_1(s: str) -> int:
    max_len = 0
    cur_len = 0
    i = 0
    vocab = dict()
    
    while i < len(s):
        cur = str(s[i])
        if cur not in vocab:
            vocab[cur] = i
            cur_len += 1
            max_len = max(cur_len, max_len)
            i += 1
        else:
            i = vocab[cur] + 1
            cur_len = 0
            vocab = dict()
    return max_len

def sol_2(s: str) -> int:
    max_len = 0
    visit = list()

    for i in range(len(s)):
        cur = str(s[i])
        if cur not in visit:
            visit.append(cur)
            max_len = max(max_len, len(visit))
        else:
            visit.append(cur)
            visit = visit[visit.index(cur)+1:]
    return max_len

from time_check import check

t1 = 'abcabcbb'
t2 = ''
t3 = 'dvdf'
t4 = 'kmmorxfk'

print(' >> use dictionary')
print(check(sol_1, t1))
print(check(sol_1, t2))
print(check(sol_1, t3))
print(check(sol_1, t4))

print(' >> use list')
print(check(sol_2, t1))
print(check(sol_2, t2))
print(check(sol_2, t3))
print(check(sol_2, t4))


# for insert mode