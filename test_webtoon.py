'''
양쪽에서 같은 문자가 나오면 자르기, 최대한 문자열을 잘게 자르기
input = 'abcde'
output = ['abcde']

input = '12abxyzab12'
output = ['12', 'ab', 'xyz', 'ab', '12]

input = 'zzzzz'
output = ['z', 'z', 'z', 'z', 'z']

실제 문제와 조금 다를 수 있음
'''

'''
1. left, right= 0, len(s)-1 // left_ans, right_ans = deque()
2. [:left+1] == [right:]가 같은가?
3. 같으면 left_ans.append, right_ans.appendleft 추가 후 s[left+1:right]에 대해 다시 적용 (recursion)
4. 다르면 left += 1, right -= 1, left<right에서 계속 진행
5. 아무것도 없이 while left<right 가 끝나면 양끝에서 같은 문자열 없이 중간까지 왔다는 뜻이므로 ans_left에 그대로 append
6. 마지막에 ans_left와 ans_right를 이어서 return
'''

from typing import List
from collections import deque

def sol(s: str) -> List[str]:
    ans_left, ans_right = deque(), deque()

    def helper(str_, ans_left, ans_right):
        left, right = 0, len(str_)-1
        while left < right:
            str_left, str_right = str_[:left+1], str_[right:]
            if str_left == str_right:
                ans_left.append(str_left)
                ans_right.appendleft(str_right)
                helper(str_[left+1:right], ans_left, ans_right)
                return # 여기서 끝내주는 게 중요!
            else:
                left += 1
                right -= 1
        ans_left.append(str_)
        return
    
    helper(s, ans_left, ans_right)
    return list(ans_left + ans_right)

# test
t1 = 'abcde'
t2 = '12abxyzab12'
t3 = 'zzzzz'

from time_check import check
print(check(sol, t1))
print(check(sol, t2))
print(check(sol, t3))


# for insert mode