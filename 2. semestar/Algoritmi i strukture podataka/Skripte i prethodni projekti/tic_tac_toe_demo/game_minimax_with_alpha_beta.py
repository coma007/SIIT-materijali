from state import State
import time


class Game(object):

    __slots__ = ['_current_state', '_player_turn']

    def __init__(self):
        self._current_state = None
        self._player_turn = 'X'
        self.initialize_game()

    def initialize_game(self):
        self._current_state = State()
        self._player_turn = 'X'

    # Player 'O' is max, in this case AI
    def max(self, alpha, beta):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result, winner = self._current_state.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result:
            if winner == 'X':
                return -1, 0, 0
            elif winner == "O":
                return 1, 0, 0
            else:
                return 0, 0, 0

        # game is not over yet
        # we continue looking for an empty field and exploring all the options
        for i in range(0, 3):
            for j in range(0, 3):
                if self._current_state.get_value(i, j) == '-':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self._current_state.set_value(i, j, 'O')
                    (m, min_i, min_j) = self.min(alpha, beta)
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self._current_state.set_value(i, j, '-')

                if maxv >= beta:
                    return maxv, px, py

                if maxv > alpha:
                    alpha = maxv

        return maxv, px, py

    # Player 'X' is min, in this case human
    def min(self, alpha, beta):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result, winner = self._current_state.is_end()

        if result:
            if winner == 'X':
                return -1, 0, 0
            elif winner == 'O':
                return 1, 0, 0
            else:
                return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self._current_state.get_value(i, j) == '-':
                    self._current_state.set_value(i, j, 'X')
                    (m, max_i, max_j) = self.max(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self._current_state.set_value(i, j, '-')

                if minv <= alpha:
                    return minv, qx, qy

                if minv < beta:
                    beta = minv

        return minv, qx, qy

    def play(self):
        while True:
            print(self._current_state)
            result, winner = self._current_state.is_end()

            # Printing the appropriate message if the game has ended
            if result:
                if winner == 'X':
                    print('The winner is X!')
                elif winner == 'O':
                    print('The winner is O!')
                else:
                    print("It's a tie!")

                self.initialize_game()
                return

            # If it's player's turn
            if self._player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    if self._current_state.is_move_valid(px, py, 'X'):
                        self._current_state.set_value(px, py, 'X')
                        self._player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py) = self.max(-2, 2)
                self._current_state.set_value(px, py, 'O')
                self._player_turn = 'X'
