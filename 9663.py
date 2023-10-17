#백트래킹 
#기억상으로 2차원배열 안써도된걸로지만 ,, 

def is_promising(board, row, col, n):
# row -> col |

    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in 



