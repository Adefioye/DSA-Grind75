board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word1 = "ABCCED"
# Output: true
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word2 = "SEE"
#Output: true
board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word3 = "ABCB"
#Output: false

def wordSearch(board, word):

    NROWS = len(board)
    NCOLS = len(board[0])

    def dfs(row, col, pos):
        
        if pos == len(word):
            return True 
        
        if row < 0 or row >= NROWS or col < 0 or col >= NCOLS or board[row][col] != word[pos]:
            return False 
        
        temp = board[row][col]
        board[row][col] = None

        top = dfs(row - 1, col, pos + 1)
        down = dfs(row + 1, col, pos + 1)
        right = dfs(row, col + 1, pos + 1)
        left = dfs(row, col - 1, pos + 1)

        board[row][col] = temp 
        
        return top or down or right or left 
    

    for r in range(NROWS):
        for c in range(NCOLS):

            if board[r][c] == word[0] and dfs(r, c, 0):
                return True 
            
    return False


print(wordSearch(board1, word1))
print(wordSearch(board2, word2))
print(wordSearch(board3, word3))