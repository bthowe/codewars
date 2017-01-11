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
            self.board_update()
            self.turn = (self.turn+1)%2
        return ''.join(self.board)

    def board_update(self):
        t1 = self.turn
        t2 = (self.turn+1)%2
        for i in xrange(2):
            regex = re.escape(self.players[t1]) + r'[' + re.escape(self.players[t2]) + r']+' + re.escape(self.players[t1])
            results = True
            while results:
                results = re.findall(regex, ''.join(self.board))
                board_string = ''.join(self.board)
                if results:
                    self.board = [i for i in ''.join(self.board).replace(results[0], results[0][0]*len(results[0]))]
            t1 = t2
            t2 = (t2+1)%2


def reversi_row(row):
    reversi = Reversi(row)
    return reversi.play()



if __name__=="__main__":
    # rev = Reversi([0,1,7,3,2])
    # print rev.play()
    # #not sure about this sequence

    print reversi_row([0,1,2,3,4,5,6,7])
