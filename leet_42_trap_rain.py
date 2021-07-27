'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
height를 그리고 중간에 물이 고일 수 있는 면접을 구해라.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Input: height = [4,2,0,3,2,5]
Output: 9

PSEUDO
양끝 투 포인터 사용
left<right 동안 왼/오 중 작은쪽에서 한칸씩 이동하면서 아래 작업 수행
height[left+1] < left_max: (더 낮아진다면)
    left_temp += left_max-height[left+1]
else: (더 커지거나 같다면, temp 정산)
    ans += left_temp
    left_temp = 0
    left_max = height[left+1]
left += 1
(right에서도 마찬가지로 수행)

마지막에 한쪽에서 이동해서 만나게 되면
ans + left_temp + right_temp 모두 더해줘서 정산

*아마 temp가 필요 없이 바로 ans에 더해줘도 괜찮을 것 같음
*양쪽에서 동시에 한칸씩 이동한다면 둘의 max값들이 다르기 때문에 가운데에서 복잡해질 수 있음. (문제 풀기 어려움) 한칸씩만!!
'''

from typing import List

def trap(height: List[int]) -> int:
    if len(height) <= 2: return 0

    left_idx = 0
    right_idx = len(height)-1
    ans = 0
    left_temp, right_temp = 0, 0
    left_max, right_max = height[0], height[-1]

    while left_idx < right_idx:
        if left_max <= right_max:
            if height[left_idx+1] < left_max:
                left_temp += (left_max - height[left_idx+1])
            else:
                ans += left_temp
                left_temp = 0
                left_max = height[left_idx+1]
            left_idx += 1
        else:
            if height[right_idx-1] < right_max:
                right_temp += (right_max - height[right_idx-1])
            else:
                ans += right_temp
                right_temp = 0
                right_max = height[right_idx-1]
            right_idx -= 1
    return ans + left_temp + right_temp

# for test
t1 = [0,1,0,2,1,0,1,3,2,1,2,1]
t2 = [4,2,0,3,2,5]

print(trap(t1))
print(trap(t2))

# for insert mode