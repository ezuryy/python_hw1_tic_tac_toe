"""The module implements unit tests."""
import unittest
from tic_tac_toe import TicTacToe


class MyTestCase(unittest.TestCase):
    """The class implements tests of the game."""
    def test_nobody_win(self):
        """The function tests the case where field is filled and nobody won."""
        game = TicTacToe()
        game.make_move(0, 1)
        game.make_move(1, 2)
        game.make_move(2, 1)
        game.make_move(3, 2)
        game.make_move(5, 1)
        game.make_move(4, 2)
        game.make_move(6, 1)
        game.make_move(8, 2)
        game.make_move(7, 1)
        game_state = game.get_game_state()
        self.assertEqual(game_state, 0)

    def test_diagonals(self):
        """The function tests the case where player won using diagonals."""
        game_1 = TicTacToe()
        game_1.make_move(0, 1)
        game_1.make_move(1, 2)
        game_1.make_move(4, 1)
        game_1.make_move(2, 2)
        game_1.make_move(8, 1)
        game_state = game_1.get_game_state()
        self.assertEqual(game_state, 1)

        game_2 = TicTacToe()
        game_2.make_move(0, 1)
        game_2.make_move(2, 2)
        game_2.make_move(1, 1)
        game_2.make_move(4, 2)
        game_2.make_move(3, 1)
        game_2.make_move(6, 2)
        game_state = game_2.get_game_state()
        self.assertEqual(game_state, 2)

    def test_rows(self):
        """The function tests the case where player won using rows."""
        game = TicTacToe()
        game.make_move(0, 1)
        game.make_move(3, 2)
        game.make_move(1, 1)
        game.make_move(4, 2)
        game.make_move(2, 1)
        game_state = game.get_game_state()
        self.assertEqual(game_state, 1)

    def test_columns(self):
        """The function tests the case where player won using columns."""
        game = TicTacToe()
        game.make_move(0, 1)
        game.make_move(2, 2)
        game.make_move(1, 1)
        game.make_move(5, 2)
        game.make_move(3, 1)
        game.make_move(8, 2)
        game_state = game.get_game_state()
        self.assertEqual(game_state, 2)

    def test_input(self):
        """The function tests incorrect input."""
        game = TicTacToe()
        result = game.make_move('0', 1)
        self.assertEqual(result, True)
        result = game.make_move('0abc', 2)
        self.assertEqual(result, False)
        result = game.make_move('0', 2)
        self.assertEqual(result, False)
        result = game.make_move('-1', 2)
        self.assertEqual(result, False)
        result = game.make_move('9', 2)
        self.assertEqual(result, False)

        game_state = game.get_game_state()
        self.assertEqual(game_state, -1)


if __name__ == '__main__':
    unittest.main()
