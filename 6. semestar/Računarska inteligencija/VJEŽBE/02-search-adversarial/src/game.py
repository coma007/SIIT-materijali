# importing required librarys
import time

import pygame
import chess
import math

from bot import Minimax, AlphaBeta

X = 800
Y = 800
scrn = pygame.display.set_mode((X, Y))
pygame.init()

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)

images_location = "images"

pieces = {'p': pygame.image.load(f'{images_location}/b_pawn.png'),
          'n': pygame.image.load(f'{images_location}/b_knight.png'),
          'b': pygame.image.load(f'{images_location}/b_bishop.png'),
          'r': pygame.image.load(f'{images_location}/b_rook.png'),
          'q': pygame.image.load(f'{images_location}/b_queen.png'),
          'k': pygame.image.load(f'{images_location}/b_king.png'),
          'P': pygame.image.load(f'{images_location}/w_pawn.png'),
          'N': pygame.image.load(f'{images_location}/w_knight.png'),
          'B': pygame.image.load(f'{images_location}/w_bishop.png'),
          'R': pygame.image.load(f'{images_location}/w_rook.png'),
          'Q': pygame.image.load(f'{images_location}/w_queen.png'),
          'K': pygame.image.load(f'{images_location}/w_king.png'),

          }


def update(scrn, board, white_view):
    # draw the squares
    for row in range(8):
        for col in range(8):
            if white_view:
                x = col * 100
                y = row * 100
            else:
                x = (7 - col) * 100
                y = (7 - row) * 100

            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = GREY
            pygame.draw.rect(scrn, color, pygame.Rect(x, y, 100, 100))

    for i in range(64):
        piece = board.piece_at(i)
        if piece == None:
            pass
        else:
            if white_view:
                scrn.blit(pieces[str(piece)], ((i % 8) * 100, 700 - (i // 8) * 100))
            else:
                scrn.blit(pieces[str(piece)], ((7 - i % 8) * 100, (i // 8) * 100))

    pygame.display.flip()


def main_one_agent(BOARD, agent, agent_color):
    """
    Za igranje coveka protiv bota
    color is True = Bot igra sa belim figurama
    color is False = Bot igra sa crnim figurama
    """
    scrn.fill(BLACK)
    pygame.display.set_caption('Chess')

    index_moves = []

    status = True
    while status:
        update(scrn, BOARD, not agent_color)

        if BOARD.turn == agent_color:
            start = time.time()
            BOARD.push(agent.perform_adversarial_search())
            print(f'Bot was thinking for {time.time() - start} seconds')
            scrn.fill(BLACK)

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    status = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # reset previous screen from clicks
                    scrn.fill(BLACK)
                    # get position of mouse
                    pos = pygame.mouse.get_pos()

                    # find which square was clicked and index of it
                    if not agent_color:
                        square = (math.floor(pos[0] / 100), math.floor(pos[1] / 100))
                    else:
                        square = (7 - math.floor(pos[0] / 100), 7 - math.floor(pos[1] / 100))

                    index = (7 - square[1]) * 8 + (square[0])

                    if index in index_moves:

                        move = moves[index_moves.index(index)]
                        BOARD.push(move)
                        index = None
                        index_moves = []

                    # show possible moves
                    else:

                        piece = BOARD.piece_at(index)

                        if piece == None:

                            pass
                        else:

                            all_moves = list(BOARD.legal_moves)
                            moves = []
                            for m in all_moves:
                                if m.from_square == index:
                                    moves.append(m)

                                    t = m.to_square

                                    if not agent_color:
                                        TX1 = 100 * (t % 8)
                                        TY1 = 100 * (7 - t // 8)
                                    else:
                                        TX1 = 100 * (7 - t % 8)
                                        TY1 = 100 * (t // 8)

                                    pygame.draw.rect(scrn, BLUE, pygame.Rect(TX1, TY1, 100, 100), 5)
                            index_moves = [a.to_square for a in moves]

        if BOARD.outcome() is not None:
            break
    # pygame.quit()


def main_two_agent(BOARD, agent1, agent_color1, agent2):
    scrn.fill(BLACK)
    pygame.display.set_caption('Chess')

    status = True
    while status:
        update(scrn, BOARD, False)

        if BOARD.turn == agent_color1:
            BOARD.push(agent1.perform_adversarial_search())
        else:
            BOARD.push(agent2.perform_adversarial_search())

        scrn.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False

        if BOARD.outcome() is not None:
            print(BOARD.outcome())
            status = False
            print(BOARD)


if __name__ == '__main__':
    # inicijalizacija sahovske table
    board = chess.Board()  # konstruktoru se može proslediti FEN string specifične pozicije
    # 1r2k1r1/pbppnp1p/1b3P2/8/Q7/B1PB1q2/P4PPP/3R2K1 w - - 0 1

    # definisi bota -> Minimax
    TURN = False  # bot - crni -> staviti True za belog
    bot = AlphaBeta(board, 3, TURN)
    main_one_agent(board, bot, TURN)

    # kod ispod služi za pokretanje table sa 2 bota
    # bot_white = AlphaBeta(board, 3, TURN)
    # bot_black = AlphaBeta(board, 3, not TURN)
    # main_two_agent(board, bot_white, True, bot_black)
