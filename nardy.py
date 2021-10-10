import time
from random import randint


class Board(object):
    def __init__(self):
        self.chess_arr = [['', 0] for i in range(24)]
        self.chess_arr[0] = ['◉', 15]
        self.chess_arr[12] = ['○', 15]
        self.turn = None
        self.outNumLeft = 0
        self.dice = []

    def start_game(self):
        self.rollTheDice()
        while self.dice[0] == self.dice[1]:
            self.rollTheDice()
        if self.dice[0] > self.dice[1]:
            self.turn = 'White'
        else:
            self.turn = 'Black'
        print('\n Dice:', self.dice, 'Start: {}'.format(self.turn))

    def rollTheDice(self):
        self.dice = []
        self.dice.append(randint(1, 6))
        self.dice.append(randint(1, 6))
        self.outNumLeft = 1
        if self.dice[0] == self.dice[1]:
            self.dice.append(self.dice[0])
            self.dice.append(self.dice[0])
            self.outNumLeft = 2
        return [self.dice]

    def _ChangePlayer(self):
        self.turn = 'White' if self.turn == 'Black' else 'Black'

    if __name__ == '__main__':
        board = Board()
        print('White & Black dices: ', end='')
        board.start_game()
        board.rollTheDice()
        while True:
            state = board.makeTurn()
            if state == 0:
                exit()
