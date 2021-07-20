'''
숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.
이렇게 게임을 진행할 경우,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, …
순으로 숫자를 말하면 된다.

한편 코딩 동아리 일원들은 컴퓨터를 다루는 사람답게 이진수로 이 게임을 진행하기도 하는데, 이 경우에는
0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, …
순으로 숫자를 말하면 된다.

이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로 게임을 진행해보기로 했다.
숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해, 자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

입력 형식
진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.

2 ≦ n ≦ 16
0 ＜ t ≦ 1000
2 ≦ m ≦ 100
1 ≦ p ≦ m
출력 형식
튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 단, 10~15는 각각 대문자 A~F로 출력한다.

입출력 예제
n	t	m	p	result
2	4	2	1	"0111"
16	16	2	1	"02468ACE11111111"
16	16	2	2	"13579BDF01234567"

PSEUDO
object_num = 숫자는 p + (t-1) * m 개 구해야 함
그 중에 range(p, len(s), m)의 idx들을 뽑아내면 됨

16진수 16개 숫자, 2명, 1번째 순서-> 31개 숫자만 구하면 됨

각 자리수의 숫자를 차례대로 append 해주는데, cnt가 object_num 까지만 채워지면 끝.
k = 1 (자리수)
ans_pool = [0]
cnt = 1
while cnt <= object_num:
    temp = list(product(range(n), repeat=k))[n**(k-1):] # [(1), (2),...(15), (1,0), (1,1)]
    for s in temp:
        ans_pool += s
        cnt += k
        if cnt >= object_num: break     

https://programmers.co.kr/learn/courses/30/lessons/17687
'''

from itertools import product

def solution(n, t, m, p):
    
    target_num = p + ((t-1) * m)

    cnt = 1
    answer = [0]
    k = 1 # 자리수

    while cnt < target_num:
        pool = list(product(range(n), repeat=k))[n**(k-1):]
        for sample in pool:
            cnt += k
            answer += sample
            if cnt >= target_num:
                break
        k += 1
    
    ans = str()
    vocab = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    for idx in range(p-1, target_num, m):
        if answer[idx] < 10:
            ans += str(answer[idx])
        else:
            ans += vocab[answer[idx]]

    return ans

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))

# for insert mode