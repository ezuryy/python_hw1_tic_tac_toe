"""The module implements unit tests."""
import unittest
from tic_tac_toe import TicTacToe


class MyTestCase(unittest.TestCase):
    """The class implements tests of the game."""
    def test_moves_sequence(self, game=TicTacToe(),
                            moves_sequence=None, final_state=-1):
        """The function tests the sequence of moves."""
        if moves_sequence is None:
            return
        for idx, move in enumerate(moves_sequence):
            player = int(idx % 2) + 1
            self.assertEqual(game.get_game_state(), -1)
            game.make_move(move, player)
        self.assertEqual(game.get_game_state(), final_state)

    def test_nobody_win(self):
        """The function tests the case where field is filled and nobody won."""
        game = TicTacToe()
        moves_sequence = [0, 1, 2, 3, 5, 4, 6, 8, 7]
        final_state = 0
        self.test_moves_sequence(game, moves_sequence, final_state)

    def test_diagonals(self):
        """The function tests the case where player won using diagonals."""
        # 1 player is winner, main diagonal
        winner_1 = 1
        game_1 = TicTacToe()
        moves_sequence_1 = [0, 1, 4, 2, 8]
        self.test_moves_sequence(game_1, moves_sequence_1, winner_1)

        # 1 player is winner, side diagonal
        game_2 = TicTacToe()
        moves_sequence_2 = [2, 0, 4, 1, 6]
        self.test_moves_sequence(game_2, moves_sequence_2, winner_1)

        # 2 player is winner, main diagonal
        winner_2 = 2
        game_3 = TicTacToe()
        moves_sequence_3 = [2, 0, 1, 4, 3, 8]
        self.test_moves_sequence(game_3, moves_sequence_3, winner_2)

        # 2 player is winner, side diagonal
        game_4 = TicTacToe()
        moves_sequence_4 = [0, 2, 1, 4, 3, 6]
        self.test_moves_sequence(game_4, moves_sequence_4, winner_2)

    def test_rows(self):
        """The function tests the case where player won using rows."""
        moves_sequence_winner_1 = [[0, 3, 1, 4, 2],
                                   [3, 0, 4, 1, 5],
                                   [6, 0, 7, 1, 8]]
        for moves_sequence in moves_sequence_winner_1:
            game = TicTacToe()
            self.test_moves_sequence(game, moves_sequence, 1)

        moves_sequence_winner_2 = [[3, 0, 4, 1, 8, 2],
                                   [0, 3, 1, 4, 8, 5],
                                   [0, 6, 1, 7, 5, 8]]
        for moves_sequence in moves_sequence_winner_2:
            game = TicTacToe()
            self.test_moves_sequence(game, moves_sequence, 2)

    def test_columns(self):
        """The function tests the case where player won using columns."""
        moves_sequence_winner_1 = [[0, 1, 3, 4, 6],
                                   [1, 0, 4, 3, 7],
                                   [2, 0, 5, 3, 8]]
        for moves_sequence in moves_sequence_winner_1:
            game = TicTacToe()
            self.test_moves_sequence(game, moves_sequence, 1)

        moves_sequence_winner_1 = [[2, 0, 1, 3, 4, 6],
                                   [2, 1, 0, 4, 3, 7],
                                   [1, 2, 0, 5, 3, 8]]
        for moves_sequence in moves_sequence_winner_1:
            game = TicTacToe()
            self.test_moves_sequence(game, moves_sequence, 2)

    def test_input(self):
        """The function tests incorrect input."""
        game = TicTacToe()
        result = game.make_move('0', 1)
        self.assertEqual(result, True)
        result = game.make_move('0', 2)  # Ячейка занята
        self.assertEqual(result, False)
        result = game.make_move('0abc', 2)  # Ввод строки
        self.assertEqual(result, False)
        result = game.make_move('-1', 2)  # Отрицательные значения
        self.assertEqual(result, False)
        result = game.make_move(-1, 2)
        self.assertEqual(result, False)
        result = game.make_move('9', 2)  # Значения больше 8
        self.assertEqual(result, False)
        result = game.make_move(9, 2)  # Значения больше 8
        self.assertEqual(result, False)
        game_state = game.get_game_state()
        self.assertEqual(game_state, -1)

        for i in range(9):
            game = TicTacToe()
            result = game.make_move(i, 1)
            self.assertEqual(result, True)
            game_state = game.get_game_state()
            self.assertEqual(game_state, -1)


if __name__ == '__main__':
    unittest.main()
