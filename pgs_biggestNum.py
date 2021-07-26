'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

입출력 예
numbers	return
[6, 10, 2]	"6210"
[3, 30, 34, 5, 9]	"9534330"

PSEUDO (sol_3) -> 꼭 체크할 것. 
str으로 바꾼 후
각 str*3을 대상으로 sort (reverse=True)

PSEUDO (sol_2)
str으로 바꾼 후
모두 세자리수로 맞춰주고 (자리수 함께 기록)
sort (reverse=True)
[:자리수] 까지만 ans에 더해서 출력

** 303과 30의 경우 30330이 나와야 하는데
sol_3에서는 303303303 303030 이므로 303 -> 30 순으로 출력
반면 sol_2에서는 (303, 3자리수), (303, 2자리수)로 sorting이 되지 않음. 따라서 30303으로 출력될 가능성이 50%..
353과 35의 경우엔 또 반대여서 일관된 규칙으로 처리하기 힘듦...

https://programmers.co.kr/learn/courses/30/lessons/42746
'''

from itertools import permutations
def sol_1(numbers):
    if len(numbers)==1: return str(numbers[0])

    pool = list(permutations(numbers))

    def make_int(tuple1):
        return int(''.join(map(str, tuple1)))
    
    nums = list(map(make_int, pool))
    ans = 0
    for num in nums:
        ans = max(ans, num)
    return str(ans)

def sol_2(numbers):
    if len(numbers)==1: return str(numbers[0])
    numbers = list(map(str, numbers)) # O(n)
    numbers = [(num, len(num)) for num in numbers] # O(n)
    new_nums = list()
    ths = 0 # 1000?
    zero = 0 # num of zeros
    for num, length in numbers: # O(n)
        if num == '0':
            zero += 1
            continue
        if length==1:
            new_nums.append((num*3, length))
        elif length==2:
            new_nums.append((num+num[0], length))
        elif length==4:
            ths += 1
        else:
            new_nums.append((num, length))
    #print(new_nums)
    new_nums.sort(key=lambda x: (x[0][0], x[0][1], x[0][2]), reverse=True) # O(nlogn)
    
    ans = str()
    for num, length in new_nums:
        ans += num[:length] # O(n)

    return str(int(ans + '1000'*ths + '0'*zero))

def sol_3(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# for test
t1 = [6,10,2]
t2 = [3,30,303,34,5,9]
t3 = [8, 83, 840, 832, 491, 75, 779, 7, 42, 45, 4, 6, 1000, 103, 1, 889, 881]
from time_check import check
print('case 1')
print(check(sol_1, t1))
print(check(sol_2, t1))
print(check(sol_3, t1))
print('case 2')
print(check(sol_1, t2))
print(check(sol_2, t2))
print(check(sol_3, t2))
print('case 3')
#print(check(sol_1, t3))
print(check(sol_2, t3))
print(check(sol_3, t3))

# for insert mode