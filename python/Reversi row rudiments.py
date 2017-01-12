import re
class Reversi():
    def __init__(self, moves):
        self.moves = moves
        self.turn = 0
        self.board = ['.']*8
        self.players = ['*', 'O']

    def play(self):
        for move in self.moves:
            self.board[move] = self.players[self.turn]
            self.board_update(move)
            self.turn = (self.turn+1)%2
            print self.board
        return ''.join(self.board)

    def board_update(self, move):
        regex = re.escape('x') + r'[' + re.escape(self.players[(self.turn+1)%2]) + r']+' + re.escape(self.players[self.turn])
        results = True

        for sign in [1, -1]:
            self.board[move] = 'x'
            results = re.findall(regex, ''.join(self.board[::sign]))
            board_string = ''.join(self.board)
            if results:
                self.board = [i for i in ''.join(self.board[::sign]).replace(results[0], self.players[self.turn]*len(results[0]))][::sign]
            else:
                self.board[move] = self.players[self.turn]

def reversi_row(row):
    reversi = Reversi(row)
    return reversi.play()



if __name__=="__main__":
    # rev = Reversi([0,1,7,3,2])
    # print rev.play()
    # #not sure about this sequence


    # print reversi_row([5, 1, 3, 4, 6])
    print reversi_row([3, 4])



# go = True
# while go:
#     go = False
#     for i in xrange(1, 7):
#         if (self.board[i-1]==self.board[i+1]) and (self.board[i-1]!=self.board[i]) and (self.board[i-1]!='.') and (self.board[i]!='.'):
#             self.board[i] = self.players[self.turn]
#             go = True

# t1 = self.turn
# t2 = (self.turn+1)%2
# for i in xrange(2):
#     regex = re.escape(self.players[t1]) + r'[' + re.escape(self.players[t2]) + r']+' + re.escape(self.players[t1])
#     results = True
#     while results:
#         results = re.findall(regex, ''.join(self.board))
#         board_string = ''.join(self.board)
#         if results:
#             self.board = [i for i in ''.join(self.board).replace(results[0], results[0][0]*len(results[0]))]
#     t1 = t2
#     t2 = (t2+1)%2
