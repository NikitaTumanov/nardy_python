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

    def move_chess(self, From, To):
        if not self._IsPossibleToMove(From, To):
            print('ERROR: Can`t move')
            time.sleep(1)
            return 2
        if From == 0 or From == 12:
            if self.outNumLeft <= 0:
                print('\t Can`t out!!!')
                time.sleep(2)
                return
            else:
                self.outNumLeft -= 1
        self.chess_arr[From][1] -= 1
        self.chess_arr[To][1] += 1
        self.chess_arr[To][0] = self.chess_arr[From][0]
        self.dice.remove((To - From) % 24)

    def makeTurn(self):
        self.print()
        print('\n Dice:', self.dice, 'Turn: {}'.format(self.turn))
        inp = input('\n  Enter from & to chess position: ').split()
        if len(inp) != 2:
            print('Error Input!')
            time.sleep(1)
            return 'Error Input!'
        try:
            From, To = map(lambda a: (int(a) - 1) % 24, inp)
        except:
            print('Error Input!')
            time.sleep(3)
            return 2
        self.move_chess(From, To)
        while not len(self.dice):
            self.rollTheDice()
            self._ChangePlayer()

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

    def print(self):
        print('  12 11 10 9  8  7     6  5  4  3  2  1 ')
        print(' ' + '-v-' * 6 + '   ' + '-v-' * 6)
        t_color = ''
        t_num = ''
        for pos in range(11, -1, -1):
            t_color, t_num = self._MakeStr(pos, t_color, t_num)
        b_color = ''
        b_num = ''
        for pos in range(12, 24, 1):
            b_color, b_num = self._MakeStr(pos, b_color, b_num)
        print('\n', t_color, '\n', t_num, '\n' * 5, b_num, '\n', b_color, '\n')
        print(' ' + '-^-' * 6 + '   ' + '-^-' * 6)
        print('  13 14 15 16 17 18    19 20 21 22 23 24 ')

    def _IsPossibleToMove(self, From, To):
        from_color, from_num = self.chess_arr[From]
        to_color, to_num = self.chess_arr[To]
        c1 = True
        c2 = (from_color == to_color) or to_num == 0
        c3 = from_num != 0
        c4 = len(self.dice)
        c5 = (from_color == '◉' and self.turn == 'White') or (from_color == '○' and self.turn == 'Black')
        return c1 and c2 and c3 and c4 and c5

    def _MakeStr(self, pos, color, num):
        c, n = self.chess_arr[pos]
        if n > 1:
            color += '{:^3}'.format(str(c))
            num += '{:^3}'.format(str(n))
        elif n == 1:
            color += '{:^3}'.format(str(c))
            num += '   '
        else:
            color += '   '
            num += '   '
        if pos == 6 or pos == 17:
            color += '   '
            num += '   '
        return (color, num)

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
