'''
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때,
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

https://programmers.co.kr/learn/courses/30/lessons/42584

PSEUDO
i가 주어졌을 때 i 뒤쪽으로 직접 비교. 더 작은 값이 보이면 loop는 break

prices += [0] #[1,2,3,2,3,0]
ans = [0]*len(prices)
for i in range(len(prices)-1) # 0,1,2,3,4
    for j in range(i+1, len(prices)) # 1,2,3,4,5
        if prices[j] < prices[i]:
            ans[i] = j-i, break
            이때 j가 맨끝, 0까지 왔다면 j-i-1
'''

def solution(prices):
    answer = [0] * len(prices)
    prices += [0]
    for i in range(len(prices)-1): # 0,1,2,3,4
        for j in range(i+1, len(prices)): # 1,2,3,4,5
            if prices[j]<prices[i]:
                if j == len(prices)-1:
                    answer[i] = j-i-1
                else:
                    answer[i] = j-i
                break
    return answer

t1 = [1,2,3,2,3]
print(solution(t1))

# for insert mode