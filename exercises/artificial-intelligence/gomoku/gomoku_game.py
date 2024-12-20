import time
import numpy as np


BOARD_SIZE = 15
WIN_LINE_LENGTH = 5
WAIT_TIME = 1
BLANK_SYMBOL = 0
PLAYER_1_SYMBOL = 1
PLAYER_2_SYMBOL = 2


class GomokuGame:
    def __init__(self, p1, p2):
        self.board = np.zeros((BOARD_SIZE, BOARD_SIZE))
        self.p1 = p1
        self.p2 = p2
        self.winner = None
        self.turn_counter = 0

    def play_turn(self):
        if np.count_nonzero(self.board) != BOARD_SIZE * BOARD_SIZE and not self.winner:
            current_player = self.p1 if self.turn_counter % 2 == 0 else self.p2
            opponent = self.p2 if self.turn_counter % 2 == 0 else self.p1
            time.sleep(WAIT_TIME)
            self.board, self.winner, move = self.turn(self.board, current_player, opponent)
            self.turn_counter += 1
        return self.board, self.winner

    def turn(self, board, agent, opponent):
        move = agent.play(board)

        if not self.is_valid(board, move):
            return board, opponent, move
        
        board[move] = agent.agent_symbol
        
        if self.is_winner(board, move):
            return board, agent, move
        
        return board, None, move

    def is_winner(self, board, move):
        i, j = move
        player = board[i, j]

        def check(values):
            counter = 0
            for value in values:
                if value == player:
                    counter += 1
                else:
                    counter = 0
                if counter >= WIN_LINE_LENGTH:
                    return True
            return False

        c1 = check(board[i, :])
        c2 = check(board[:, j])
        c3 = check(board.diagonal(j-i))
        c4 = check(np.fliplr(board).diagonal(board.shape[0]-i-j-1))
        
        if c1 or c2 or c3 or c4:
            return player
        
        return False

    def is_valid(self, board, move):
        i, j = move
        if i >= 0 and i < BOARD_SIZE and j >= 0 and j < BOARD_SIZE and board[i, j] == BLANK_SYMBOL:
            return True
        return False
