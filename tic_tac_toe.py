"""This module works quickly with arrays."""
import numpy as np


def print_info():
    """The function prints instruction how to play."""
    print('The first player moves with <X>, '
          'the second - with <O>. To make move enter the cell number:')
    print('|-----|-----|-----|')
    for i in range(3):
        print('| ', 3 * i, ' | ', 3 * i + 1, ' | ', 3 * i + 2, ' |')
        print('|-----|-----|-----|')


class Field:
    """The class implements game field:
    checks whether someone won, prints current field, etc."""
    def __init__(self):
        self.field = np.array([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
        self.state = -1
        # -1 play
        #  0 field is filled, nobody win
        #  1 player 1 is the winner
        #  2 player 2 is the winner

    def is_cell_empty(self, cell_number):
        """The function checks whether
        the cell is empty so player can make move to the cell."""
        return self.field[cell_number] == ' '

    def is_field_filled(self):
        """The function checks whether all cells are occupied."""
        mask = np.where(self.field == ' ')
        return len(self.field[mask]) == 0

    def is_winner(self, winner_symbol):
        """The function checks whether
        the player has filled 3 consecutive cells."""
        winner_array = np.array([winner_symbol, winner_symbol, winner_symbol])
        is_winner_diag_0 = np.all(self.field[0:9:4] == winner_array)  # 0,4,8
        is_winner_diag_1 = np.all(self.field[2:7:2] == winner_array)  # 2,4,6
        is_winner_diag = is_winner_diag_0 or is_winner_diag_1

        is_winner_row = np.array([False, False, False])
        is_winner_column = np.array([False, False, False])
        for i in range(3):
            is_winner_row[i] = np.all(self.field[i:i + 7:3] == winner_array)
            is_winner_column[i] = \
                np.all(self.field[3 * i:3 * i + 3:1] == winner_array)
        is_winner_row = np.any(is_winner_row)
        is_winner_column = np.any(is_winner_column)

        return is_winner_diag or is_winner_row or is_winner_column

    def update_game_state(self):
        """The function updates game status according to state of the field."""
        if self.is_field_filled():
            self.state = 0
        if self.is_winner('X'):
            self.state = 1
        if self.is_winner('O'):
            self.state = 2

    def get_game_state(self):
        """The function returns game status."""
        return self.state

    def occupy_cell(self, cell_number, occupier):
        """The function implements occupying the cell by the player."""
        if occupier == 1:
            self.field[cell_number] = 'X'
        elif occupier == 2:
            self.field[cell_number] = 'O'

    def print(self):
        """The function prints current field."""
        print('|-----|-----|-----|')
        for i in range(3):
            print('| ', self.field[3 * i], ' | ', self.field[3 * i + 1],
                  ' | ', self.field[3 * i + 2], ' |')
            print('|-----|-----|-----|')


class TicTacToe:
    """The class implements game logic:
    make moves in the field and print current field."""
    def __init__(self):
        self.field = Field()

    def make_move(self, cell_number, occupier):
        """The function checks whether
        player can move into the cell and implements move."""
        try:
            cell = int(cell_number)
        except ValueError:
            print('You entered a string. Please, '
                  'enter the cell number in range [0, 8]:')
            return False
        if 0 <= cell < 9:
            if self.field.is_cell_empty(cell):
                self.field.occupy_cell(cell, occupier)
                self.field.update_game_state()
                return True
            print('This cell is already occupied. Please, choose another cell')
        else:
            print('Please, enter the cell number in range [0, 8]:')
        return False

    def get_game_state(self):
        """The function returns game status."""
        return self.field.get_game_state()

    def print_field(self):
        """The function prints current field."""
        self.field.print()
