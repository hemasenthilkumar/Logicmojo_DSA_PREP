"""
Path which the knight will take to visit all places exactly once

Possible moves from a point for knight = 8
(x,y)
(-2,1)
(-2,-1)
(-1,2)
(-1,2)
(2,1)
(2,-1)
(1,-2)
(1,2)

TC: O(8^n^2)
SC: O(n^2)

"""
rowMoves = [2,2,-2,-2,-1,-1,1,1]
colMoves = [1,-1,1,-1,2,-2,2,-2]


def isSafe(x, y, n, board):
    if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
        return True
    return False

def traverse(board, move, x, y, n):
    nextX, nextY = 0,0
    # Terminating condition
    if move == n*n:
        return True
    for i in range(8):
        nextX = x + rowMoves[i]
        nextY = y + colMoves[i]
        if isSafe(nextX, nextY, n, board):
            board[nextX][nextY] = move
            if traverse(board, move+1, nextX, nextY, n):
                return True 
            board[nextX][nextY] = -1
    return False
        

def knight_tour(n):
    board = [[-1] * n for _ in range(n)]
    board[0][0] = 0 # can check for all starting values from the board
    if traverse(board, 1, 0, 0, n):
        print(board)
    else:
        print("No solution exists!")

if __name__ == "__main__":
    knight_tour(5)
    knight_tour(4)