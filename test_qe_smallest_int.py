'''
자연수(1~) 중 주어진 list에 없는 최소의 수를 구하기
time O(n)

t1 = [3,4,2,8,13] -> 1
t2 = [101,102,103] -> 1
t3 = [4,3,2,6,1,9] -> 5
t4 = [3,2,1,4] -> 5 worst case
'''

from typing import List


def sol(arr: List) -> int:
    # if not arr: # []의 경우에도 dict에 아무것도 없고, range(1, 2)로 돌아가기 때문에 return 가능
    #     return 1
    vocab = dict()
    for i in arr:
        vocab[i] = True
    
    for i in range(1, len(arr)+2): # len(arr)+1 까지만 뒤져보면 되고, 최악의 경우 len(arr)+1 값을 return하면 되는 이유 생각해보
        if i in vocab:
            pass
        else:
            return i

# test
t1 = [3,4,2,8,13] 
t2 = [101,102,103]
t3 = [4,3,2,6,1,9]
t4 = [3,2,1,4]

from time_check import check
print(check(sol, t1))
print(check(sol, t2))
print(check(sol, t3))
print(check(sol, t4))
print(check(sol, []))

# for insert mode