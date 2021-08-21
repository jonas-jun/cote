'''
주어진 list 값들로 permutation을 만들 때, 오름차순 정렬 상 다음 permutation 값을 return
123 -> 132
52341 -> 52413

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Solution
끝에서부터 loop
앞숫자와 동일 또는 증가하는 구간에서는 그냥 continue
만약 감소하는 구간이라면,
뒷 숫자들 중 감소된 숫자보다는 크면서 가장 작은 숫자를 찾아내서 i-1과 자리 바꿈
그리고 i: 끝까지 sorting(inplace, quick or insertion)
한번 작업이 이뤄지면 바로 return
작업이 안 이뤄졌다면, (위에서 끝까지 루프가 다 돌았다면) 오름차순 정렬 (가장 작은 수) 또는 숫자 뒤집기

https://leetcode.com/problems/next-permutation/
'''

def nextPermutation(nums):
    i = len(nums)-1
    while i > 0:
        if nums[i-1]>=nums[i]:
            i-=1
            continue
        min_val = nums[i]
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[i-1] < nums[j] and min_val > nums[j]:
                min_idx = j
                min_val = nums[j]
        nums[i-1], nums[min_idx] = nums[min_idx], nums[i-1]
        
        # i:len(nums)-1까지를 sort (quick or insertion)
        for idx_i in range(i, len(nums)):
            min_idx = idx_i
            min_val = nums[idx_i]
            for j in range(idx_i+1, len(nums)):
                if nums[j] < min_val:
                    min_idx = j
                    min_val = nums[j]
            nums[idx_i], nums[min_idx] = nums[min_idx], nums[idx_i]
        return
    nums.sort() # 위에서 아무 일도 일어나지 않았다면 뒤집어주기
    return

# for test
t1 = [1,2,3]
nextPermutation(t1)
print(t1)

t2 = [3,2,1]
nextPermutation(t2)
print(t2)

t3 = [1,1,5]
nextPermutation(t3)
print(t3)