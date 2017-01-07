class Reversi():
    def __init__(self, moves):
        self.moves = moves
        self.turn = 0
        self.board = ['.']*8
        self.players = ['*', 'O']

    def play(self):
        for move in self.moves:
            self.board[move] = self.players[self.turn]
            self.board_update()
            self.turn = (self.turn+1)%2
        return ''.join(self.board)

    def board_update(self):
        # go = True
        # while go:
        #     go = False
        #     for i in xrange(1, 7):
        #         if (self.board[i-1]==self.board[i+1]) and (self.board[i-1]!=self.board[i]) and (self.board[i-1]!='.') and (self.board[i]!='.'):
        #             self.board[i] = self.players[self.turn]
        #             go = True

        # for i in xrange(0, 6):
        #     if self.board[i]!='.':
        #         piece = self.board[i]
        #         to_turn = []
        #
        #         for item in self.board[i+1:]:
        #             if (item==piece) or (item=='.'):
        #                 break
        #             to_turn.append()

        # I could get it to work with the above...but try a regex.


def reversi_row(row):
    reversi = Reversi(row)
    return reversi.play()

if __name__=="__main__":
# '*OO*...*' should equal '****...*'

    print reversi_row([7, 6, 5])
