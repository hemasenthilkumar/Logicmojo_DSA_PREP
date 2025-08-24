


def isSafe(row, col, n, board):
    tempRow, tempCol = row,col
    # left
    tempCol = col
    while tempCol >= 0:
        if board[row][tempCol] == 'Q':
            return False
        tempCol -= 1
    # upper diagonal
    tempRow = row 
    tempCol = col 
    while tempRow >=0 and tempCol >=0 :
        if board[tempRow][tempCol] == 'Q':
            return False
        tempRow -= 1 
        tempCol -= 1
    # lower diagonal
    tempRow = row 
    tempCol = col 
    while tempRow < n and tempCol >=0:
        if board[tempRow][tempCol] == 'Q':
            return False
        tempRow += 1 
        tempCol -= 1
    return True

def findAllPath(col, n, board):
    if col == n:
        for row in board:
            print(" ".join(row))
        print()
        return

    for row in range(n):
        if isSafe(row, col, n, board):
            board[row][col] = 'Q'
            findAllPath(col+1, n, board)
            board[row][col] = '.'

def solveNQueen(n):
    board = [['.'] * n for _ in range(n)]
    findAllPath(0,n,board)

if __name__ == "__main__":
    solveNQueen(4)