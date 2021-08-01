'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

not necessarily solvable.
only validate filled cells. (not '.')

PSEUDO
for (i,j) in board:
    board[i][j] == target
    if target == '.': continue (don't check)
    check if there is any same value in row, column, square area -> return False
return True

https://leetcode.com/problems/valid-sudoku
'''

def isValidSudoku(board):
    i_dict, j_dict = dict(), dict()
    for idx in range(9):
        if idx in range(3):
            i_dict[idx] = range(3)
            j_dict[idx] = range(3)
        elif idx in range(3,6):
            i_dict[idx] = range(3,6)
            j_dict[idx] = range(3,6)
        else:
            i_dict[idx] = range(6,9)
            j_dict[idx] = range(6,9)
    
    for i in range(9):
        for j in range(9):
            target = board[i][j]
            if target == '.': continue
            for _ in range(9):
                if _ != i:
                    if board[_][j] == target: return False
                if _ != j:
                    if board[i][_] == target: return False
            
            for k in i_dict[i]:
                for l in j_dict[j]:
                    if k-i and l-j:
                        if board[k][l] == target: return False
    return True

# for test
t1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

t2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

from time_check import check

print(check(isValidSudoku, t1))
print(check(isValidSudoku, t2))