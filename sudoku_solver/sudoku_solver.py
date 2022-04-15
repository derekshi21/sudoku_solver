board = [
        [3,9,-1,-1,5,-1,-1,-1,-1],
        [-1,-1,-1,2,-1,-1,-1,-1,5],
        [-1,-1,-1,7, 1, 9,-1,8,-1],

        [-1,5,-1,-1,6,8,-1,-1,-1],
        [2,-1,6,-1,-1,3,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1,-1,-1, 4],

        [5,-1,-1,-1,-1,-1,-1,-1,-1],
        [6,7,-1,1,-1,5,-1,4,-1],
        [1,-1,9,-1,-1,-1,2,-1,-1]
]

def find_next_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == -1:
                return i, j
    return False

def valid_guess(bo, num, pos):
    row_vals = bo[pos[0]]
    if num in row_vals:
        return False
    
    col_vals = [bo[i][pos[1]] for i in range(len(bo))]
    if num in col_vals:
        return False

    square_row = (pos[0] // 3) * 3
    square_col = (pos[1] // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if bo[i][j] == num and bo[i][j] != pos:
                return False
    
    return True

def solve(bo):
    find = find_next_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid_guess(bo, num, (row, col)):
            bo[row][col] = num

            if solve(bo):
                return True
        
        bo[row][col] = -1
    
    return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

if __name__ == "__main__":
    print("Original board: ")
    print_board(board)
    print("")
    solve(board)
    print("New board: ")
    print_board(board)
