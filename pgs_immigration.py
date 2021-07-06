'''
문제 설명
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.
입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
심사관은 1명 이상 100,000명 이하입니다.
입출력 예
n	times	return
6	[7, 10]	28
입출력 예 설명
가장 첫 두 사람은 바로 심사를 받으러 갑니다.

7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

Sol1은 O(n * len(times))로 문제의 상황을 그대로 구현한 것
Sol2는 중간값을 하나 잡은 후 범위를 좁혀나가면서 탐색 O(C*len(times)) 수준에서 가능, 엄밀하게는 C = log(highest-lowest)

https://programmers.co.kr/learn/courses/30/lessons/43238?language=python3#
'''

def sol1(n, times):
    remains = [0 for _ in range(len(times))]
    done = 0
    while done < n:
        temp = [remains[j] + times[j] for j in range(len(times))] # finish time
        go_idx = temp.index(min(temp))
        remains[go_idx] += times[go_idx]
        done += 1
    return max(remains)

def sol2(n, times):
    times = sorted(times)
    start, end = times[0] * n / len(times), times[-1] * n / len(times)    

    def helper(low, high):
        if low == high:
            return low
        mid = (low+high)//2
        done = 0
        for time in times:
            done += mid // time
            if done >= n:
                break
        if done >= n:
            return helper(low, mid) # not include mid
        else:
            return helper(mid+1, high)
    
    return helper(start, end)

# test
t1_n = 6
t1_times = [7, 10]

t2_n = 150
t2_times = [5, 4, 3, 9, 11, 10, 22, 15]

from time_check import check
print('>> test1')
print(check(sol1, t1_n, t1_times))
print(check(sol2, t1_n, t1_times))
print('>> test2')
print(check(sol1, t2_n, t2_times))
print(check(sol2, t2_n, t2_times))

# for insert mode