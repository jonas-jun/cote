'''
정수 1과 3이 주어지고, 이 둘을 통틀어 5번까지 마음대로 사용하여 그 합을 구하여 1,2,3,…을 만드는 놀이다.
서로 번갈아서 상대방의 수보다 1이 큰 수를 만들어야 한다. 단, 1과 3을 통틀어 최대 5번 사용한다. 이런 식으로 진행하면 13까지는 만들 수 있지만 14를 만들지 못하게 되므로 짝순이가 졌다.
숫자들과 사용 최대 회수가 주어질 때, 누가 어느 수에서 이기는지를 판별하는 프로그램을 작성하는 것이 문제다.

sol1: product (itertools)
3가지 숫자와 최대개수 4가 주어진다면, 가능한 경우의 수 (0,0,1), (2,1,1) 등을 모두 뽑고, 0<sum(pair)<=4 인 경우만 filter
가능한 경우들을 돌면서 memo를 True로 지워주고
1부터 추가하면서 False가 발견되면 return

sol2: DFS
0부터 시작해서 3,5 를 각각 더해가면서 이동.
cum 들을 memo에서 True로 바꿔줌

sol3: DP
dp[i]는 숫자 i번 골랐을 때 가능한 합들
dp[i+1]은 dp[i]에 각각의 nums를 더해줬을 때 나오는 수들
dp에 기록하면서 memo도 동시에
set()으로 중복을 피하면 됨

https://www.acmicpc.net/problem/1679
'''


from itertools import product
def sol1(nums, max_num):
    length = len(nums)
    pool = range(max_num+1)
    pool = list(filter(lambda x: 0<sum(x)<=max_num, list(product(pool, repeat=length))))
    
    memo = [False for _ in range((nums[-1]*max_num) + 1)]
    for pair in pool:
        cum = 0
        for i in range(len(pair)):
            cum += pair[i] * nums[i]
        memo[cum] = True
    
    for num in range(1, len(memo)):
        if not memo[num]: break
    
    who = 'holsoon' if num % 2 == 0 else 'jjaksoon'
    return '{} win at {}'.format(who, num)

def sol2(nums, max_num):
    memo = [False for _ in range((nums[-1]*max_num) + 1)]

    def dfs_helper(cum, length):
        nonlocal nums, max_num, memo
        memo[cum] = True
        if length == max_num: return

        for num in nums:
            dfs_helper(cum + num, length+1)
    
    dfs_helper(0, 0)
    for num in range(1, len(memo)):
        if not memo[num]: break

    who = 'holsoon' if num % 2 == 0 else 'jjaksoon'
    return '{} win at {}'.format(who, num)

def sol3(nums, max_num):
    memo = [False for _ in range((nums[-1]*max_num) + 1)]
    for num in nums:
        memo[num] = True

    dp = [set() for _ in range(max_num+1)]
    dp[1] = set(nums)
    
    for i in range(2, len(dp)):
        before = dp[i-1]
        for b in before:
            for num in nums:
                memo[b+num] = True
                dp[i].add(b+num)

    for num in range(1, len(memo)):
        if not memo[num]: break
    
    who = 'holsoon' if num % 2 == 0 else 'jjaksoon'
    return '{} win at {}'.format(who, num)


from time_check import check
t1 = [1,3]
t1_max = 5
t2 = [1,2,4,6,8]
t2_max = 10

print('case 1')
print(check(sol1, t1, t1_max))
print(check(sol2, t1, t1_max))
print(check(sol3, t1, t1_max))

print('case 2')
print(check(sol1, t2, t2_max))
print(check(sol2, t2, t2_max))
print(check(sol3, t2, t2_max))