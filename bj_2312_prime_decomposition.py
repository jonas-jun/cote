'''
소인수분해하기
소수를 구할 필요가 없다...
밑에서부터 가능할 때까지 나눠가다 보면 자연스럽게 소수로만 나눠지게 된다.
sqrt(n)까지만 돌리고 마지막에 n만 확인해주는 것도 포인트. n이 소수라면 sqrt(n) 까지 해도 나눠지지 않기 때문

https://www.acmicpc.net/problem/2312
'''

def solution(n):
    ans = list()
    for num in range(2, int(n**(1/2))+1):
        count = 0
        while n % num == 0:
            n /= num
            count += 1
        if count:
            ans.append((num, count))
        if n == 1: break
    if n != 1: ans.append((int(n),1))
    return ans

# for test
print(solution(32))
print(solution(91))
print(solution(24))