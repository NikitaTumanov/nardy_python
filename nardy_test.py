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