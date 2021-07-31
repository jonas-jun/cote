'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

[10, 20, 15, 25, 10, 20] -> 75
20 + 25 + 10 + 20

PSEUDO: DP
DP는 그 idx까지의 max값
dp[idx] = max((dp[idx-3] + nums[idx-1] + nums[idx]), (dp[idx-2] + nums[idx])):
바로 전 계단을 밟는 경우엔 전전 계단을 밟으면 안됨. 따라서 3개 전 계단으르 발았다 치고 + 전 계단 + idx 계단
전전 계단을 밟는 경우엔 바로 넘어옴. 전단 계단 + idx 계단

https://www.acmicpc.net/problem/2579
'''

def sol(nums):
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return sum(nums)
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = dp[0] + nums[1]
    dp[2] = max(dp[0]+nums[2], nums[1]+nums[2]) # [10, 30, 35]

    for idx in range(3, len(nums)):
        dp[idx] = max((dp[idx-3]+nums[idx-1]+nums[idx]), (dp[idx-2]+nums[idx]))
    return dp[-1]

t1 = [10,20,15,25,10,20]
print(sol(t1))