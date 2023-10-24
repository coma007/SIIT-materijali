import random
from abc import abstractmethod

import chess
import math


class AdversarialSearch(object):
    """
    Apstraktna klasa za suparnicku/protivnicku pretragu.
    """

    def __init__(self, board, max_depth, turn):
        """
        :param board: tabla koja predstavlja pocetno stanje
        :param max_depth: maksimalna dubina pretrage (koliko poteza unapred)
        :param turn: da li bot igra sa belim ili crnim figurama
        """
        self.board = board
        self.max_depth = max_depth
        self.turn = turn


    @abstractmethod
    def perform_adversarial_search(self):
        """
        Apstraktna metoda koja vrsi pretragu i vraca sledece stanje
        :return: odigran potez
        """
        pass

    def evaluate_position(self, position):
        """
        position: chess.Board instanca
        :return: number - vrednost evaluacije
        """
        # Jednostavna evaluacino funkcija

        # Provera da li je došlo do kraja partije
        if position.is_checkmate():
            return 100000 if position.turn else -100
        if position.is_stalemate() or position.is_insufficient_material() or position.is_fivefold_repetition():
            return 0
        
        # Poredjenje ukupne vrednost crnih i belih figura
        score = 0
        material = {"P": 1, "N": 3, "B": 3, "R": 5, "Q": 9, "K": 100} # vrednovanje figura
        for square in chess.SQUARES:
            piece = position.piece_at(square)
            if piece is not None:
                value = material[piece.symbol().upper()]
                if piece.color == chess.WHITE:
                    score += value
                else:
                    score -= value

        return score



class Minimax(AdversarialSearch):

    def perform_adversarial_search(self):
        best_score, best_move = self.minimax(self.board, 0, self.turn)
        return best_move

    
    def minimax(self, position, depth, maximizing):
        # TODO 1: Implementirati minimax algoritam
        # Lista mogucih poteza = list(self.board.legal_moves)
        # Kreiranje novog stanja:
        #   Kopiramo tablu - updated_board = position.copy()
        #   Odigramo potez na njoj - updated_board.push(move)
        if depth == 0 or position.is_checkmate():
            return self.evaluate_position(position) # heuristic
        if maximizing:
            best_value = - math.inf
            for move in list(self.board.legal_moves):
                value = self.minimax(move, depth - 1, FALSE)
                best_value = max(best_value, value)
            return best_value
            # for 
        else:
            best_value = math.inf
            for move in list(self.board.legal_moves):
                value = self.minimax(move, depth - 1, TRUE)
                best_value = min(best_value, value)
            return best_value


class AlphaBeta(AdversarialSearch):

    
    def perform_adversarial_search(self):
        best_score, best_move = self.alpha_beta_pruning(self.board, 0, self.turn)
        return best_move

    # nije za studente
    def alpha_beta_pruning(self, position, depth, maximizing, alpha=-float('inf'), beta=float('inf')):
        # TODO 2: Implementirati alpha-beta-algoritam
        pass
