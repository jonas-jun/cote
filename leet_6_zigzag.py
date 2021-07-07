'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

nRows = 3
P   A   H   N
A P L S I I G
Y   I   R

https://leetcode.com/problems/zigzag-conversion/

Solution>
중요한 수 k: nRow + (nRow-2)
idx_list = list()

0 + n*k 나열
1, k-1 + n*k 나열
2, k-2
3, k-3
4 + n*k 나열

k 정의
range(0, len(s), k)
j range(1, nRow-1)에 대해서:
    range(j, len(s), k)
    range(k-j, len(s), k)
    합쳐서 sorted
range(nRow-1, len(s), k)

이것들을 각각 더해주고

ans=str()
마지막에 for문 돌려서 s[i]들을 차례로 붙여서 return
'''

def solution(s, numRows):
    if numRows==1 or len(s)<=numRows:
        return s
    
    key_val = numRows + (numRows-2)

    # check index
    idx_list = list()
    # first line
    idx_list += list(range(0, len(s), key_val))
    # middle lines
    for j in range(1, numRows-1):
        idx_list += sorted(list(range(j, len(s), key_val)) + list(range(key_val-j, len(s), key_val)))
    # last line
    idx_list += list(range(numRows-1, len(s), key_val))

    # get answer
    ans = str()
    for i in idx_list:
        ans += s[i]
    
    return ans

t1 = 'PAYPALISHIRING'

from time_check import check

print(check(solution, t1, 3))
print(check(solution, t1, 4))
print(check(solution, 'AB', 1))

# for insert mode