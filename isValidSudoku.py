def isValidSudoku(board: list[list[str]]) -> bool:
    # fon = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # flag = True
    for i in board:
        # l = len(i)
        cnt = 0
        for j in i:
            if j == '.':
                cnt += 1
        if len(list(set(i))) + cnt - 1 != 9:
            return False
    for i in range(9):
        lis = []
        for j in range(9):
            cnt = 0
            # print(board[j][i])
            lis.append(board[j][i])
            
            # l = len(lis)
            if board[j][i] == '.':
                cnt += 1   
        if len(list(set(lis))) + cnt - 1 != 9:
            return False
        print(lis)           
    return True  
    
    
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))