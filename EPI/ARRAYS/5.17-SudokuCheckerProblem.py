import collections 

board1 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: true

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: false

def isValidSudoku(board: str) -> bool:

    ROWS = collections.defaultdict(set)
    COLS = collections.defaultdict(set)
    SQUARES = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):

            if board[r][c] == ".":
                continue 

            if (board[r][c] in ROWS[r] or
                board[r][c] in COLS[c] or 
                board[r][c] in SQUARES[(r // 3, c // 3)]):

                return False 

            ROWS[r].add(board[r][c])
            COLS[c].add(board[r][c])
            SQUARES[(r // 3, c // 3)].add(board[r][c])

    return True

print(isValidSudoku(board1))    # True
print(isValidSudoku(board2))    # False