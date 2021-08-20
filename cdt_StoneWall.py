'''
H[i]는 i~i+1까지의 벽의 높이
주어진 벽을 직사각형으로 자를 때 최소 개수는?

H = [8,8,5,7,9,8,7,4,8]
return 7

그림을 그려서 이해해봐야 함...
좋은 문제
처음에는 각 최소값으로 잘라서 생각했었음 (time error)

solution
증가한다면? stack에 추가
감소한다면? 감소 높이(H[i])로 자르는 거라고 생각함.
위쪽 부분을 잘라내면서 사각형 발생 (다른 높이 개수만큼 다른 사각형이 발생!)
마지막에 스택에 남아있는 숫자 만큼의 사각형 (다른 높이) 추가해줘야 함

https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall
'''

def solution(H):
    ans = 0
    stack = [0]
    for val in H:
        if val == stack[-1]:
            continue
        if val > stack[-1]:
            stack.append(val)
        else:
            while stack[-1] > val:
                stack.pop()
                ans += 1
            if stack[-1] != val:
                stack.append(val)
    ans += (len(stack)-1)
    return ans

# for test
H = [8,8,5,7,9,8,7,4,8]
print(solution(H))