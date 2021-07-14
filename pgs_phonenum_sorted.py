'''
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

입출력 예제
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false

PSEUDO
sol_1
길이가 짧은 순으로 sorting
for i in range(len()-1):
    for j in range(i+1, len()):
        sort[j]가 sort[i]로 시작하면 return False (startswith)
return True

sol_2
sorted 함수의 특성을 이용
sorted(phone_book) ['116190', '1162', '119', '1193', '152', '342']
루프를 한번 돌면서 바로 뒤에 숫자와 비교만 해주면 됨
'''

def sol_1(p_book):
    sort = list()
    for num in p_book:
        sort.append((num, len(num)))
    sort = sorted(sort, key=lambda x: x[1])

    for i in range(len(sort)-1):
        s = sort[i][0]
        for j in range(i+1, len(sort)):
            if sort[j][0].startswith(s):
                return False
    return True

def sol_2(p_book):
    sort = sorted(p_book)
    for i in range(len(p_book)-1):
        if sort[i+1].startswith(sort[i]):
            return False
    return True

# for test
t1 = ['119', '97674223', '1195524421']
t2 = ['123', '456', '789']
t3 = ['119', '1162', '1193', '342', '152', '116190']
t4 = ['acef', 'b', 'zi', 'jonas', 'john', 'jz']

from time_check import check
print('test 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print('test 2')
print(check(sol_1, t2))
print(check(sol_2, t2))
print('test 3')
print(check(sol_1, t3))
print(check(sol_2, t3))
print('test 4')
print(check(sol_1, t4))
print(check(sol_2, t4))

# for insert mode