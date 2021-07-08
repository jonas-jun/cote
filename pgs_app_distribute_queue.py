'''
문제 설명
프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

입출력 예
progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
입출력 예 설명
입출력 예 #1
첫 번째 기능은 93% 완료되어 있고 하루에 1%씩 작업이 가능하므로 7일간 작업 후 배포가 가능합니다.
두 번째 기능은 30%가 완료되어 있고 하루에 30%씩 작업이 가능하므로 3일간 작업 후 배포가 가능합니다. 하지만 이전 첫 번째 기능이 아직 완성된 상태가 아니기 때문에 첫 번째 기능이 배포되는 7일째 배포됩니다.
세 번째 기능은 55%가 완료되어 있고 하루에 5%씩 작업이 가능하므로 9일간 작업 후 배포가 가능합니다.

따라서 7일째에 2개의 기능, 9일째에 1개의 기능이 배포됩니다.

Pseudo Code
1. 남은 기간을 리스트로 만든다. divmod 몫을 추가하는데 나머지가 0이라면 몫에 1이 아니라면 몫에 1을 더해줘야 한다. (100%가 넘어가야 최종 배포 가능)
2. max_val을 0으로 놓고 max_val보다 큰 idx를 체크한다. 이게 배포하는 날짜가 됨
3. idx 리스트 마지막에 len(progresses)를 붙여준다. 배포일에 배포하게 되는 개수를 count할 수 있도록
4. idx 리스트의 i+1 - i 값들을 정답에 넣어준다.

https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
'''

def solution(progresses, speeds): # O(2n + C) 정도
    # make remain list
    remains = list()
    for i in range(len(speeds)):
        a,b = divmod(100-progresses[i], speeds[i])
        if b != 0: a += 1
        remains.append(a)
    
    # make date list
    max_val = 0
    date_list = list()
    for i in range(len(speeds)):
        if remains[i] > max_val:
            date_list.append(i)
            max_val = remains[i]
    date_list += [len(speeds)]
    
    return [date_list[i+1]-date_list[i] for i in range(len(date_list)-1)]

from collections import deque
def solution_1(progresses, speeds): # O(2n) 정도
    remains = list()
    for i in range(len(speeds)):
        a,b = divmod(100-progresses[i], speeds[i])
        if b != 0: a += 1
        remains.append(a)
        
    ans = list()
    remains = deque(remains)
    max_val = remains.popleft()
    cnt = 1
    
    while remains:
        val = remains.popleft()
        if val > max_val:
            ans.append(cnt)
            max_val = val
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    return ans

# test
t1_prog = [93, 30, 55]
t1_speeds = [1,30,5]
t2_prog = [95,90,99,99,80,99]
t2_speeds = [1,1,1,1,1,1]

from time_check import check
print(check(solution, t1_prog, t1_speeds))
print(check(solution, t2_prog, t2_speeds))
print(check(solution_1, t1_prog, t1_speeds))
print(check(solution_1, t2_prog, t2_speeds))

# for insert mode