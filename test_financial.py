'''
주어진 두 시간의 사이 시간들 중 숫자 2개 이하로 표기되는 시간의 개수는?
주어진 두 시간은 같은 날로 가정한다.
'''


from datetime import datetime, timedelta

def solution(t1:str, t2:str) -> int:
    t1, t2 = datetime.strptime(t1, '%H:%M:%S'), datetime.strptime(t2, '%H:%M:%S')
    ans = 0
    while t1 <= t2:
        if len(set(datetime.strftime(t1, '%H%M%S'))) <= 2: ans += 1
        t1 += timedelta(seconds=1)
    return ans


# for test
from time_check import check

t1_s = '15:15:00'
t1_e = '15:15:11'

t2_s = '22:22:22'
t2_e = '22:22:24'

t3_s = '00:01:11'
t3_e = '23:55:57'

print(check(solution, t1_s, t1_e))
print(check(solution, t2_s, t2_e))
print(check(solution, t3_s, t3_e))