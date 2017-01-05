def flip(last_move, board):
    if move>=2:
        if (board[move-1]==chars[(turn+1)%2]) and (board[move-2]==chars[turn]):
            board[move-1]=chars[turn]
    if move<=5:
        if (board[move+1]==chars[(turn+1)%2]) and (board[move+2]==chars[turn]):
            board[move+1]=chars[turn]


def reversi_row(moves):
    board = ['.']*8
    chars = ['*', 'O']
    turn = 0

    for move in moves:
        board[move] = chars[turn]

        last_move = move
        while flip(last_move, board):
            new_move = flip(last_move, board)
            board[new_move, board)] = chars[turn]
            last_move =new_move
            print board




        turn = (turn+1)%2

    return board



if __name__=="__main__":
    print reversi_row([7, 6, 5])
