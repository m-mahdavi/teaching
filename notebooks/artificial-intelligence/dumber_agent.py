import random

class GomokuAgent:
    
    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.name = __name__
        self.agent_symbol = agent_symbol
        self.blank_symbol = blank_symbol
        self.opponent_symbol = opponent_symbol
    
    def play(self, board):
        i = random.randint(0, 14)
        j = random.randint(0, 14)
        while board[i, j] != self.blank_symbol:
            i = random.randint(0, 14)
            j = random.randint(0, 14)
        return (i, j)