'''
[4,5,6,7,0,1,2] 이런식으로 중간에 한번 잘린 ASC 행렬(rotated sorted array)이 있을 때,
O(logn)으로 target을 찾는 문제, 없으면 -1

Solution
max_idx를 찾아내고 (logn)
array[0]과 target을 비교하면 arr의 어느 부분에 target이 있어야 할지 알 수 있음
그리고 그 부분에 bs를 돌려서 target 찾기

https://leetcode.com/problems/search-in-rotated-sorted-array
'''

def search(nums, target):
    # find max idx
    def get_max(s,e):
        nonlocal nums
        if e-s==1:
            if nums[s]<nums[e]: return e
            else: return s
        mid_idx = (s+e)//2
        if s == mid_idx: return s
        if nums[s] > nums[mid_idx]:
            return get_max(s, mid_idx-1)
        else:
            return get_max(mid_idx, e)

    max_i = get_max(0, len(nums)-1)
    if nums[max_i]==target: return max_i
    
    if max_i == len(nums)-1: # max_idx가 맨 끝이라면 -> 전체가 asc array
        s,e = 0, len(nums)-2 # 끝에서 두번째 index

    # target이 있을만한 범위를 구함. 그 범위 안에서는 ASC array
    else:
        if target == nums[0]: return 0
        if target > nums[0]:
           s,e = 1, max_i-1
        else:
            s,e = max_i+1, len(nums)-1
    if target < nums[s] or nums[e] < target: return -1 # 범위 안에 존재하지 않으면 -1

    def bs(s,e):
        nonlocal nums, target
        if s>e: return -1
        if s==e:
            if nums[s]==target: return s
            else: return -1
        mid_idx = (s+e)//2
        if nums[mid_idx]==target: return mid_idx
        if nums[mid_idx]>target:
            return bs(s,mid_idx-1)
        else:
            return bs(mid_idx+1,e)
    
    return bs(s,e)

# for test
t1 = [4,5,6,7,0,1,2]
print(search(t1, 0))
print(search(t1, 3))
print(search([1], 0))