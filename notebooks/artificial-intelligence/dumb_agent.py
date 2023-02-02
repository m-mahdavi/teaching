import random

class GomokuAgent:
    
    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.name = __name__
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol
    
    def play(self, board):
        for v in range(15 * 15):
            i = v // 15
            j = v % 15
            if board[i, j] == self.blank_symbol:
                return (i, j)