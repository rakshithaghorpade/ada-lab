global N 
N = 5
def printSolution(board): 
    for i in range(N): 
        for j in range(N): 
            print (board[i][j], end = " ") 
        print() 
def isSafe(board, row, col): 
    for i in range(row): 
        if board[i][col] == 1: 
            return False
    for i, j in zip(range(row, -1, -1),  
                    range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    for i, j in zip(range(row, -1, -1),  
                    range(col, N, 1)): 
        if board[i][j] == 1: 
            return False
    return True
  
def solveNQUtil(board, row): 
    if row >= N: 
        return True
    for i in range(N): 
        if isSafe(board, row, i): 
            board[row][i] = 1 
            if solveNQUtil(board, row + 1) == True: 
                return True
            board[row][i] = 0
    return False
def solveNQ(): 
    board = [ [0, 0, 0, 0,0], 
              [0, 0, 0, 0,0], 
              [0, 0, 0, 0,0], 
              [0, 0, 0, 0,0],
              [0, 0, 0, 0,0]] 
  
    if solveNQUtil(board, 0) == False: 
        print ("Solution does not exist") 
        return False
  
    printSolution(board) 
    return True
solveNQ() 
  
