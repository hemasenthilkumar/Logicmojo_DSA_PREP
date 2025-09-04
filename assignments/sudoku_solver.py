"""
Sudoku Solver
- Guaranteed that it has only 1 valid solution

"""

ROWS = 9
COLS = 9

def is_number_valid(board, r,c, num) -> bool:
    # check if we can place the num in board[r][c]
    # check rows if the same number is there
    for i in range(9):
        if board[r][i] == num:
            return False
    # check columns if same number is there
    for i in range(9):
        if board[i][c] == num:
            return False
    # check block if same number is there
    row_start = ( r // 3 ) * 3 
    col_start = (c // 3) * 3 
    for i in range(row_start, row_start+3):
        for j in range(col_start, col_start+3):
            if board[i][j] == num:
                return False 
    # need help
    return True


def solve_sudoku(board):
    # backtracking solution
    # For each position we will try 9 items so TC: 9^81 (branching ^ board-size)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == '.':
                for i in range(1,10):
                    if is_number_valid(board, r, c, str(i)):
                        board[r][c] = str(i) 
                        if solve_sudoku(board):
                            return True
                        board[r][c] = '.'
                return False
    return True
   

if __name__  == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    solve_sudoku(board)
    print(board)