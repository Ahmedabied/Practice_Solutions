
def next_move(posr, posc, dimx, dimy, board):
    i, j = min(((i, j) for i, row in enumerate(board) if 'd' in row for j, c in enumerate(row) if c == 'd'), key=lambda x: abs(posr - x[0]) + abs(posc - x[1]))
    print("LEFT" if j < posc else "RIGHT" if j > posc else "UP" if i < posr else "DOWN" if i > posr else "CLEAN")
pos = [int(i) for i in input().strip().split()]
dim = [int(i) for i in input().strip().split()]
board = [[j for j in input().strip()] for i in range(dim[0])]
next_move(pos[0], pos[1], dim[0], dim[1], board)