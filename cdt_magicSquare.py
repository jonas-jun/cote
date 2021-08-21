'''
문제설명
3*3 사각형 숫자들이 주어졌을 때
사각형의 가로세로 각 라인 [0,1,2] [3,4,5] [6,7,8] [0,3,6], [1,4,7], [2,5,8]의 합이 모두 같아지도록
최소한의 액션만 (액션은 한 지점을 +1 해주는 것) 취했을 때의 결과 사각형은?

아래 velog 글 보면 예시와 설명이 나와 있음
https://velog.io/@jonas-jun/Codility-almostmagic
'''

def solution(A):
    list_idx = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8]]
    list_sum = list()
    for idxs in list_idx:
        list_sum.append(sum([A[idx] for idx in idxs]))
    target = max(list_sum) # 만들어야 하는 숫자, 숫자를 줄일 순 없으니 가장 큰 수에 맞춰야 한다.
    list_target = [target-sum_ for sum_ in list_sum] # target 값까지 얼마나 부족한지?
    if sum(list_target)==0: return A # 이미 다 차 있다면 바로 return
    
    idxs = [idx for idx in range(6) if list_target[idx]] # 채워야 할 줄들만 뽑아내기 위한 작업
    list_idx = [list_idx[idx] for idx in idxs]
    list_target = [list_target[idx] for idx in idxs]

    def helper():
        nonlocal list_idx, list_target
        for i in range(len(list_idx)-1):
            for j in range(i+1, len(list_idx)):
                # i, j의 채워야할 값들이 남아있고, 둘의 공통 부분이 있다면
                if list_target[i] and list_target[j] and (set(list_idx[i]) & set(list_idx[j])):
                    add_idx = list(set(list_idx[i]) & set(list_idx[j]))[0] # 추가해야 할 index
                    val = min(list_target[i], list_target[j]) # 최대 몇 까지 추가할 수 있는지
                    A[add_idx] += val
                    list_target[i]-=val
                    list_target[j]-=val
                    if sum(list_target)==0: return # 한번 작업하고 다 됐는지 확인
        helper()
    helper()
    return A

# for test
t = [0,2,3,4,1,1,1,3,1]
print(solution(t))

