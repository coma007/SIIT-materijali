class Board:
    """
    Klasa koja implementira strukturu table.
    """

    def __init__(self, rows=20, cols=20):
        self.rows = rows  # broj redova
        self.cols = cols  # broj kolona
        # ---------------
        # . = empty
        # w = wall
        # r = robot
        # g = robot's goal
        # ----------------
        self.elems = [
            '.',
            'w',
            'r',
            'g',
            'b',
            'y'
            ]
        self.data = [['.'] * cols for _ in range(rows)]
        self.text = [[''] * cols for _ in range(rows)]
        self.teleport = False

    def load_from_file(self, file_path):
        """
        Ucitavanje table iz fajla.
        :param file_path: putanja fajla.
        """
        board_f = open(file_path, 'r')
        row = board_f.readline().strip('\n')
        self.data = []
        while row != '':
            self.data.append(list(row))
            row = board_f.readline().strip('\n')
        board_f.close()

    def save_to_file(self, file_path):
        """
        Snimanje table u fajl.
        :param file_path: putanja fajla.
        """
        if file_path:
            f = open(file_path, 'w')
            for row in range(self.rows):
                f.write(''.join(self.data[row]) + '\n')
            f.close()

    def switch_cell(self, row, col):
        """
        Izmena sadrzaja celije table.
        :param row: red celije.
        :param col: kolona celije.
        """
        if row < len(self.data) and col < len(self.data[0]):
            idx = self.elems.index(self.data[row][col])
            idx += 1
            idx %= len(self.elems)
            self.data[row][col] = self.elems[idx]

    def clear(self):
        """
        Ciscenje sadrzaja cele table.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                self.data[row][col] = '.'
                self.text[row][col] = ''

    def find_position(self, element):
        """
        Pronalazenje specificnog elementa unutar table.
        :param element: kod elementa.
        :returns: tuple(int, int)
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if self.data[row][col] == element:
                    return row, col
        return None, None
    
    def find_all_positions(self, element):
        """
        Pronalazenje svih pojava specificnog elementa unutar table.
        :param element: kod elementa.
        :returns: list(tuple(int, int))
        """
        positions = []
        for row in range(self.rows):
            for col in range(self.cols):
                if self.data[row][col] == element:
                    positions.append((row, col))
        return positions

    def move_player_keyboard(self, direction):
        position = self.find_position('r')
        new_position = position

        if self.teleport:
            self.teleport = False
            teleport_position = self.find_position('y')
            if (teleport_position[0] != None):
                self.data[position[0]][position[1]] = '.'
                self.data[teleport_position[0]][teleport_position[1]] = 'r'
                return position[0], position[1], teleport_position[0], teleport_position[1]
        if all([p is not None for p in position]):
            d_row, d_col = Board.get_direction_keyboard(direction)
            new_row = position[0] + d_row
            new_col = position[1] + d_col
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.data[new_row][new_col] != 'w':
                self.data[position[0]][position[1]] = '.'
                new_position = new_row, new_col
                if self.data[new_position[0]][new_position[1]] == 'y':
                    self.teleport = True
                self.data[new_position[0]][new_position[1]] = 'r'
        
                
        return position[0], position[1], new_position[0], new_position[1]

    @staticmethod
    def get_direction_keyboard(direction):
        if direction == 'left':
            return 0, -1
        elif direction == 'right':
            return 0, 1
        elif direction == 'up':
            return -1, 0
        elif direction == 'down':
            return 1, 0
        else:
            return 0, 0
