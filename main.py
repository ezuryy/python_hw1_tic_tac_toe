"""The module has game logic and console output."""
from tic_tac_toe import TicTacToe, print_info


def play(game):
    """The function for playing in console.
    It gets console input and do the main logic."""
    print_info()

    game_state = -1
    while game_state == -1:
        move_result = False
        while not move_result:
            cell_number_1 = input('Player 1: >>>>>>>>>>')
            move_result = game.make_move(cell_number_1, 1)
        game.print_field()

        game_state = game.get_game_state()
        if game_state != -1:
            break

        move_result = False
        while not move_result:
            cell_number_2 = input('Player 2: >>>>>>>>>>')
            move_result = game.make_move(cell_number_2, 2)
        game.print_field()

        game_state = game.get_game_state()
        if game_state != -1:
            break

    if game_state == 0:
        print('Game is over. No one won! :)')
    elif game_state == 1:
        print('Game is over. Player 1 won! :)')
    elif game_state == 2:
        print('Game is over. Player 2 won! :)')


if __name__ == '__main__':

    tic_tac_toe = TicTacToe()
    play(tic_tac_toe)
