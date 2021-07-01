'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

https://leetcode.com/problems/longest-palindromic-substring/
'''

def longestPalindrome(s: str) -> str:
    length = len(s)
    max_len = 1
    palin = None

    for i in range(2, len(s)+1):
        if (s[:i] == s[i-1::-1]):
            if (len(s[:i]) > max_len):
                palin = s[:i]
                max_len = len(s[:i])

    for i in range(1,len(s)-1):
        for j in range(i+1+max_len, len(s)+1):
            if (s[i:j] == s[j-1:i-1:-1]):
                if (len(s[i:j]) > max_len):
                    palin = s[i:j]
                    max_len = len(s[i:j])

    if not palin:
        return s[0]
    return palin

t1 = 'babad'
t2 = 'cbbd'
t3 = 'a'
t4 = 'ac'

print(longestPalindrome(t1))
print(longestPalindrome(t2))
print(longestPalindrome(t3))
print(longestPalindrome(t4))

# faster algorithm
# first, check right side same digits
# next, check both side
# O(n^2-c)
def longestPalindrome_(s: str) -> str:
    res=""
    size=0
    center = 0
    n=len(s)
    while center<n:
        left = center-1
        right= center+1
        while right<n and s[right]==s[center]:
            right+=1
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        if right-left-1>size:
            size=right-left-1
            res = s[left+1:right]
        center+=1
    return res

print(longestPalindrome_(t1))
print(longestPalindrome_(t2))
print(longestPalindrome_(t3))
print(longestPalindrome_(t4))


# for insert mode