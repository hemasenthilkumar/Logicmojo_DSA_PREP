"""
Can move up, down, left, right
end goal - able to reach (n-1, n-1)
starting position = 0,0

Up = diff row, same column (-1, 0)
Down = diff row, same column (1, 0)
left = same row, col decrease (0,-1)
right = same row, col increase (0, 1)

TC: 4^n^2
SC: n^2

Safe method:
- boundary
- cell value is 1
- tracking visited matrix
"""

rowMoves = [-1,1,0,0]
colMoves = [0,0,-1,1]
direction = ['U', 'D', 'L', 'R']

def isSafe(row, col, n, board, visited):
    if row >= 0 and col >=0 and row < n and col < n and (row, col) not in visited and board[row][col] == 1:
        return True 
    return False

def traverse(row, col, board, n, visited, path, result):

    if row == n-1 and col == n-1:
        result.append("".join(path))
        return 
    
    nextRow, nextCol = 0,0
    for i in range(4):
        nextRow = row + rowMoves[i]
        nextCol = col + colMoves[i]
        if isSafe(nextRow, nextCol, n, board, visited):
            visited.add((nextRow, nextCol))
            path.append(direction[i])
            
            traverse(nextRow, nextCol, board, n, visited, path, result)

            path.pop()
            visited.remove((nextRow, nextCol))

def solveRatMaze(board, n):
    visited = set()
    result = []
    visited.add((0,0))
    traverse(0,0, board, n,  visited, [], result)
    if bool(result):
        print(f"Reached: {result}")
    else:
        print("No solution!")



if __name__ == "__main__":
    n = 3
    maze = [
      [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]
    ]
    solveRatMaze(maze, n)
    n = 4
    maze = [
      [1, 1, 0, 0],
      [1, 1, 0, 1],
      [0, 1, 1, 1],
      [1, 1, 1, 1]
    ]
    solveRatMaze(maze, n)
