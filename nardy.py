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

    if __name__ == '__main__':
        board = Board()
        print('White & Black dices: ', end='')
        board.start_game()
        board.rollTheDice()
        while True:
            state = board.makeTurn()
            if state == 0:
                exit()
