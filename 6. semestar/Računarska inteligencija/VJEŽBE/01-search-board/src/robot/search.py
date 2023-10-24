from __future__ import print_function

from collections import deque
from abc import *


class Search(object):
    """
    Apstraktna klasa za pretragu.
    """

    def __init__(self, board):
        self.board = board

    def search(self, initial_state):
        """
        Implementirana pretraga.

        :param initial_state: Inicijalno stanje. Tip: implementacija apstraktne klase State.
        :return: path, processed_list, states_list
        """
        # inicijalizacija pretrage
        initial_state = initial_state(self.board)  # pocetno stanje
        states_list = deque([initial_state])  # deque - "brza" lista u Python-u
        # set - za brzu pretragu stanja
        states_set = {initial_state.unique_hash()}

        processed_list = deque([])  # deque procesiranih stanja
        processed_set = set()  # set procesiranih stanja

        # pretraga
        while len(states_list) > 0:  # dok ima stanja za obradu
            # preuzmi sledece stanje za obradu
            curr_state = self.select_state(states_list)
            # izbaci stanja iz seta stanja
            states_set.remove(curr_state.unique_hash())

            # ubaci stanje u listu procesiranih stanja
            processed_list.append(curr_state)
            # ubaci stanje u set procesiranih stanja
            processed_set.add(curr_state.unique_hash())

            if curr_state.is_final_state():  # ako je krajnje stanje
                # rekonsturisi putanju
                return Search.reconstruct_path(curr_state), processed_list, states_list

            # ako nije krajnje stanje
            # izgenerisi sledeca moguca stanja
            new_states = curr_state.get_next_states()
            # iz liste sledecih mogucih stanja izbaci ona koja su vec u listi i koja su vec procesirana
            new_states = [new_state for new_state in new_states if
                          new_state.unique_hash() not in processed_set and
                          new_state.unique_hash() not in states_set]
            # dodaj sledeca moguca stanja na kraj liste stanja
            states_list.extend(new_states)
            # dodaj sledeca moguca stanja u set stanja
            states_set.update([new_state.unique_hash()
                              for new_state in new_states])
        return None, processed_list, states_list

    @staticmethod
    def reconstruct_path(final_state):
        path = []
        while final_state is not None:
            path.append(final_state.position)
            final_state = final_state.parent
        return reversed(path)

    @abstractmethod
    def select_state(self, states):
        """
        Apstraktna metoda koja, na osnovu liste svih mogucih sledecih stanja,
        bira sledece stanje za obradu.
        *** STRATEGIJA PRETRAGE SE IMPLEMENTIRA OVERRIDE-ovanjem OVE METODE ***

        :param states: lista svih mogucih sledecih stanja
        :return: odabrano sledece stanje za obradu
        """
        pass


class BreadthFirstSearch(Search):

    def select_state(self, states):
        # struktura podataka je red (queue)
        # dodaj na kraj, uzimaj sa pocetka
        return states.popleft()


class DepthFirstSearch(Search):

    def select_state(self, states):
        # TODO 1: Implementirati DFS
        return states.pop()


class IterativeDepthFirstSearch(Search):

    limit = 2

    def select_state(self, states):
        # TODO 2: Implementirati IDFS
        # Po potrebi koristiti state.depth
        for state in reversed(states):
            if state.depth < self.limit:
                states.remove(state)
                return state
        self.limit += 2
        for state in reversed(states):
            if state.depth < self.limit:
                states.remove(state)
                return state


class GreedySearch(Search):
    def select_state(self, states):
        # TODO 3: Implementirati GS
        # implementirati get_cost_estimate metodu u RobotState
        minimum_cost = 1000000
        optimal_state = None
        for state in states:
            if minimum_cost > state.get_cost_estimate():
                minimum_cost = state.get_cost_estimate()
                optimal_state = state
        states.remove(optimal_state)
        return optimal_state


class AStarSearch(Search):
    def select_state(self, states):
        # TODO 4: Implementirati A*
        # implementirati get_cost_estimate i get_current_cost metode u RobotState
        minimum_cost = 1000000
        optimal_state = None
        for state in states:
            if minimum_cost > state.get_current_cost() + state.get_cost_estimate():
                minimum_cost = state.get_current_cost() + state.get_cost_estimate()
                optimal_state = state
        states.remove(optimal_state)
        return optimal_state
