'''
1. 합이 max가 되는 subarray
2. 곱이 max가 되는 subarray

Kadene's 알고리즘
nums[i] 까지의 최대/최소 값 등의 계산 값 기준으로
nums[i+1] 까지의 최대/최소 값을 계산할 수 있다.
num[i+1]이 맨 끝에 포함되는 subarray 중
'''

def sol_1(nums):
    global_max = nums[0]
    local_max = nums[0]

    for idx in range(1, len(nums)):
        local_max = max(local_max+nums[idx], nums[idx])
        global_max = max(global_max, local_max)
    return global_max

def sol_2(nums):
    cur_max, cur_min, g_max = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= 0:
            cur_max, cur_min = max(cur_max*nums[i], nums[i]), min(cur_min*nums[i], nums[i])
        else:
            cur_max, cur_min = max(cur_min*nums[i], nums[i]), min(cur_max*nums[i], nums[i])
        g_max = max(g_max, cur_max)
    return g_max

print('Question 1. maxSum')
t1 = [-2,1,-3,4,-1,2,1,-5,4]
t2 = [5,4,-1,7,8]
print(sol_1(t1))
print(sol_1(t2))
print('Question 2. maxProduct')
t3 = [2,3,-2,4]
t4 = [-2,0,-1]
print(sol_2(t3))
print(sol_2(t4))