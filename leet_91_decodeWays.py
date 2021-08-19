'''
a: 1, b: 2 ... z: 26 디코딩된다.
aajf -> 1 1 10 6: 11106
kjf -> 11 10 6: 11106 같을 수 있다.
하지만 11 1 06 은 불가하다. 0이나 06 같은 건 없다.
숫자로 이뤄진 str이 주어졌으르 때 디코딩 가능한 방법의 수는?

ex1. '226'
(2 26), (22, 6), (2, 2, 6) 3개

Solution
다이나믹프로그래밍 사용
우선 앞자리가 0이면 return 0, 한지리 문자라면 return 1
dp = [1, 0, 0, 0, ...] -> i자리까지의 디코딩 가능한 수

s[i]가 0이면:
    s[i-1]이 0이거나 s[i-1]이 >2이면: 디코딩할 방법이 없음. return 0
    아니라면: dp[i] = dp[i-2] (i-2까지 디코딩을 하고 '10', '20' 등 한가지만 가능)

s[i]가 0이 아니면:
    s[i-1:i+1] > 26이면: i-1까지 인코딩된 방법에 s[i]를 붙여주는 수밖에 없음. dp[i] = dp[i-1]
    아니라면: i-1까지 인코딩 + s[i] 또는 i-2까지 인코딩 + s[i-1:i+1] 두 가지 가능. dp[i] = dp[i-1]+dp[i-2]

return dp[-1]

https://leetcode.com/problems/decode-ways
'''

def numDecodings(s: str) -> int:
    if s[0] == '0': return 0
    if len(s) == 1: return 1
    
    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    dp[-1] = 1
    '2101'
    for i in range(1, len(s)):
        if s[i] == '0':
            if int(s[i-1])>2 or s[i-1]=='0': return 0
            else: dp[i] = dp[i-2]
        else: # 0이 아니라면
            if s[i-1] == '0':
                dp[i] = dp[i-1]
                continue
            if int(s[i-1:i+1]) <= 26: dp[i] = dp[i-1] + dp[i-2] # dp[-1]==1이기 때문에 i=1에서도 가능
            else: dp[i] = dp[i-1]
    return dp[-1]


# for test
s1 = '02'
s2 = '2264'
s3 = '2101'
print(numDecodings(s1))
print(numDecodings(s2))
print(numDecodings(s3))