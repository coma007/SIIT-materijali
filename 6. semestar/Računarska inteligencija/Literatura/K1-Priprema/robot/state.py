from abc import *


class State(object):
    """
    Apstraktna klasa koja opisuje stanje pretrage.
    """

    @abstractmethod
    def __init__(self, board, parent=None, position=None, goal_position=None, left_box=None, right_box=None, fire=None):
        """
        :param board: Board (tabla)
        :param parent: roditeljsko stanje
        :param position: pozicija stanja
        :param goal_position: pozicija krajnjeg stanja
        :return:
        """
        self.board = board
        self.parent = parent  # roditeljsko stanje

        self.left_box = left_box
        self.right_box = right_box
        if self.left_box == None or self.right_box == None:
            boxes = board.find_all_positions(self.get_checkpoint_code())
            self.left_box = boxes[0]
            self.right_box = boxes[1]

        self.fire = fire
        if self.fire == None:
            self.fire = tuple(board.find_position(self.get_fire_code()))

        if self.parent is None:  # ako nema roditeljsko stanje, onda je ovo inicijalno stanje
            self.position = board.find_position(
                self.get_agent_code())  # pronadji pocetnu poziciju
            self.goal_position = board.find_position(
                self.get_agent_goal_code())  # pronadji krajnju poziciju
        else:  # ako ima roditeljsko stanje, samo sacuvaj vrednosti parametara
            self.position = position
            self.goal_position = goal_position
        # povecaj dubinu/nivo pretrage
        self.depth = parent.depth + 1 if parent is not None else 1

    def get_next_states(self):
        # dobavi moguce (legalne) sledece pozicije iz trenutne pozicije
        new_positions = self.get_legal_positions()
        next_states = []
        # napravi listu mogucih sledecih stanja na osnovu mogucih sledecih pozicija
        for new_position in new_positions:
            next_state = self.__class__(
                self.board, self, new_position, self.goal_position, self.left_box, self.right_box, self.fire)
            next_states.append(next_state)
        return next_states

    @abstractmethod
    def get_agent_code(self):
        """
        Apstraktna metoda koja treba da vrati kod agenta na tabli.
        :return: str
        """
        pass

    @abstractmethod
    def get_agent_goal_code(self):
        """
        Apstraktna metoda koja treba da vrati kod agentovog cilja na tabli.
        :return: str
        """
        pass

    @abstractmethod
    def get_checkpoint_code(self):
        """
        Apstraktna metoda koja treba da vrati kod checkpoint-a na tabli.
        :return: str
        """
        pass

    @abstractmethod
    def get_teleport_code(self):
        """
        Apstraktna metoda koja treba da vrati kod teleporta-a na tabli.
        :return: str
        """
        pass

    @abstractmethod
    def get_fire_code(self):
        """
        Apstraktna metoda koja treba da vrati kod vatre-a na tabli.
        :return: str
        """
        pass

    @abstractmethod
    def get_legal_positions(self):
        """
        Apstraktna metoda koja treba da vrati moguce (legalne) sledece pozicije na osnovu trenutne pozicije.
        :return: list
        """
        pass

    @abstractmethod
    def is_final_state(self):
        """
        Apstraktna metoda koja treba da vrati da li je treuntno stanje zapravo zavrsno stanje.
        :return: bool
        """
        pass

    @abstractmethod
    def unique_hash(self):
        """
        Apstraktna metoda koja treba da vrati string koji je JEDINSTVEN za ovo stanje
        (u odnosu na ostala stanja).
        :return: str
        """
        pass

    @abstractmethod
    def get_cost_estimate(self):
        """
        Apstraktna metoda koja treba da vrati procenu cene
        (vrednost heuristicke funkcije - h(n)) za ovo stanje.
        Koristi se za vodjene pretrage.
        :return: float
        """
        pass

    @abstractmethod
    def get_current_cost(self):
        """
        Apstraktna metoda koja treba da vrati stvarnu trenutnu cenu za ovo stanje, odnosno g(n)
        Koristi se za vodjene pretrage.
        :return: float
        """
        pass


class RobotState(State):

    def __init__(self, board, parent=None, position=None, goal_position=None, left_box=None, right_box=None, fire=None):
        super(self.__class__, self).__init__(board, parent,
                                             position, goal_position, left_box, right_box, fire)

        # Akumuliranje cene u stanju
        if self.parent == None:
            self.cost = 0
        else:
            self.cost = self.parent.cost + 1  # dozvoljeno je menjati cene akcija
            if self.position == self.fire:
                self.cost += 100000

        # self.left_box - pozicija leve kutije
        if self.position == self.left_box and self.right_box == ():
            self.left_box = ()
        # self.right_box - pozicija desne kutije
        elif self.position == self.right_box:
            # print(self.right_box)
            self.right_box = ()
        # self.fire - pozicija vatre

    def get_agent_code(self):
        return 'r'

    def get_agent_goal_code(self):
        return 'g'

    def get_checkpoint_code(self):
        return 'b'

    def get_teleport_code(self):
        return 'y'

    def get_fire_code(self):
        return 'f'

    def get_legal_positions(self):
        # moguci smerovi kretanja robota (desno, levo, dole, gore)
        actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # dodatni smerovi kretanja kao sahoviski konj
        knight_actions = [(-1, -2), (-1, 2), (1, -2), (1, 2),
                          (-2, -1), (-2, 1), (2, -1), (2, 1)]

        row, col = self.position
        new_positions = []
        current_actions = knight_actions if self.right_box == (
        ) and self.left_box != () else actions
        for d_row, d_col in current_actions:
            new_row = row + d_row
            new_col = col + d_col

            if 0 <= new_row < self.board.rows and 0 <= new_col < self.board.cols and self.board.data[new_row][new_col] != 'w':
                new_positions.append((new_row, new_col))
        return new_positions

    def is_final_state(self):
        return self.position == self.goal_position and self.left_box == () and self.right_box == ()

    def unique_hash(self):
        return f"{self.position};rightbox:{self.right_box == ()};leftbox:{self.left_box == ()}"

    def get_cost_estimate(self):
        danger_distance = 3
        distance_to_fire = 0
        print(self.fire)
        if self.fire != (None, None):
            distance_to_fire = abs(
                self.position[0] - self.fire[0]) + abs(self.position[1] - self.fire[1])
            if distance_to_fire < danger_distance:
                return abs(self.position[0] - self.goal_position[0]) + abs(self.position[1] - self.goal_position[1]) - distance_to_fire + 10000
        return abs(self.position[0] - self.goal_position[0]) + abs(self.position[1] - self.goal_position[1]) - distance_to_fire

    def get_current_cost(self):
        return self.cost
