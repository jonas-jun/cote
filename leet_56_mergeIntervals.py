'''
주어진 arr 내의 interval들을 통합해서(통합 가능한 것들은) return

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

PSEUDO
정렬(lambda x: x[0]) 기준
stack = [intervals[0]]
for interval in intervals[1:]:
    if stack[-1][1] >= interval[0]: 겹치는 부분이 있다면
        stack.pop()
        # 둘이 합치는 작업
        stack.append(합친 거)
    else:
        stack.append(interval)

https://leetcode.com/problems/merge-intervals
'''

from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    
    def helper(inter1, inter2):
        return [min(inter1[0], inter2[0]), max(inter1[1], inter2[1])]
    
    stack = [intervals[0]]
    for interval in intervals[1:]:
        if stack[-1][1] >= interval[0]:
            stack.append(helper(stack.pop(), interval)) # 끝에거 빼서 합쳐주고 다시 append
        else: stack.append(interval)
    
    return stack

# for test
t1 = [[1,3],[2,6],[8,10],[15,18]]
t2 = [[0,0],[1,4]]
print(merge(t1))
print(merge(t2))