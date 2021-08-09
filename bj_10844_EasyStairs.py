'''
45656이란 수를 보자. 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)
첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

"Memoization"
n*10의 2dim list를 생성
dp[n-1]은 n자리 수의 계단 개수 [0,1,2,3,4,5,6,7,8,9] -> 첫자리의 숫자
dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
j == 0 이거나 j == 9 일때는 dp[i-1][j+1]이나 dp[i-1][j-1] 만 그대로 계승함
계산할 때 n=3으로 먼저 고정해두고 j를 0~9까지 돌려야 함(이중루프 순서)

https://www.acmicpc.net/problem/10844
'''

def stairs(n: int):
    dp = [[0 for _ in range(10)] for _ in range(n)]
    dp[0] = [1 for _ in range(10)] # n=1
     
    for i in range(1, n):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    return sum(dp[n-1][1:])

print(stairs(int(input())) % 1000000000)