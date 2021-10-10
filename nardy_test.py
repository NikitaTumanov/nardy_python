import unittest
import nardy


class Test(unittest.TestCase):
    def test_start(self):
        a = nardy.Board()
        a.start_game()
        for i in range(0, 24):
            if i != 0 and i != 12:
                assert a.chess_arr[i] == ['', 0]
            if i == 0:
                assert a.chess_arr[i] == ['◉', 15]
            if i == 12:
                assert a.chess_arr[i] == ['○', 15]

        if a.dice[0] > a.dice[1]:
            assert a.turn == 'White'
        else:
            assert a.turn == 'Black'

    def test_role(self):
        a = nardy.Board()
        a.rollTheDice()
        for i in a.dice:
            assert i in range(1, 7)
        assert a.dice == 2 or 4

    def test_move(self):
        a = nardy.Board()
        assert a.chess_arr[12] == ['○', 15]
        assert a.chess_arr[0] == ['◉', 15]

        a.move_chess(0, 10)
        assert a.chess_arr[0 + 10] == ['◉', 1] or a.turn == 'Black'
        assert a.chess_arr[0] == ['◉', 14] or a.turn == 'Black'

        a.chess_arr[0 + 10] = ['○', 1]
        a.move_chess(0, 0 + 10)
        assert a.chess_arr[12] == ['○', 15]
        assert a.chess_arr[0] == ['◉', 15]