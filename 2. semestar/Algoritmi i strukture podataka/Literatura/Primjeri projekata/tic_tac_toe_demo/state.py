class State(object):

    def __init__(self):
        self._board = []
        for i in range(0, 3):
            self._board.append(3*['-'])

    def get_value(self, i, j):
        return self._board[i][j]

    def set_value(self, i, j, value):
        self._board[i][j] = value

    def is_move_valid(self, i, j, value):
        value = value.upper()
        if value not in "XO":
            return False

        if self._board[i][j] is not '-':
            return False

        return True

    def is_end(self):

        # Vertical win
        for i in range(0, 3):
            if self._board[0][i] == self._board[1][i] and \
                    self._board[1][i] == self._board[2][i] and \
                    self._board[2][i] != '-':
                return True, self._board[0][i]

        # Horizontal win
        for row in self._board:
            if row == ['X', 'X', 'X']:
                return True, 'X'
            elif row == ['O', 'O', 'O']:
                return True, 'O'

        # Diagonal win 1
        if self._board[0][0] == self._board[1][1] and \
                self._board[1][1] == self._board[2][2] and \
                self._board[2][2] != '-':
            return True, self._board[1][1]

        # Diagonal win 2
        if self._board[0][2] == self._board[1][1] and \
                self._board[1][1] == self._board[2][0] and \
                self._board[2][0] != '-':
            return True, self._board[1][1]

        for i in range(0, 3):
            for j in range(0, 3):
                if self._board[i][j] == '-':
                    return False, None

        return True, None

    def __str__(self):
        ret = "\n\n-------------\n"
        for i in range(0, 3):
            ret += "|"
            for j in range(0, 3):
                if self._board[i][j] is '-':
                    ret += "   |"
                else:
                    ret += " %s |" % self._board[i][j]
            ret += "\n-------------\n"
        return ret
