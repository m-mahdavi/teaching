import time
import numpy as np
from flask import Flask, render_template, jsonify

import dumb_agent
import dumber_agent

app = Flask(__name__)

# Constants
BOARD_SIZE = 15
WIN_LINE_LENGTH = 5
WAIT_TIME = 1
BLANK_SYMBOL = 0
PLAYER_1_SYMBOL = -1
PLAYER_2_SYMBOL = 1

# Initialize the game
board = np.zeros((BOARD_SIZE, BOARD_SIZE))
p1 = dumb_agent.GomokuAgent(PLAYER_1_SYMBOL, BLANK_SYMBOL, PLAYER_2_SYMBOL)
p2 = dumber_agent.GomokuAgent(PLAYER_2_SYMBOL, BLANK_SYMBOL, PLAYER_1_SYMBOL)
winner = ""
team_info = {
    "player1": {"name": p1.name, "symbol": "X"},
    "player2": {"name": p2.name, "symbol": "O"}
}
turn_counter = 0

@app.route("/")
def index():
    return render_template("index.html", team_info=team_info)

@app.route("/get_board")
def get_board():
    return jsonify(board.tolist())

@app.route("/play_turn")
def play_turn():
    global board, winner, turn_counter
    if np.count_nonzero(board) != BOARD_SIZE * BOARD_SIZE and not winner:
        current_player = p1 if turn_counter % 2 == 0 else p2
        opponent = p2 if turn_counter % 2 == 0 else p1
        time.sleep(WAIT_TIME)
        board, winner, move = turn(board, current_player, opponent)
        turn_counter += 1
    winner_symbol = winner.agent_symbol if winner else None
    return jsonify({"board": board.tolist(), "winner": winner_symbol})

def turn(board, agent, opponent):
    move = agent.play(board)

    if not is_valid(board, move):
        return board, opponent, move
    
    board[move] = agent.agent_symbol
    
    if is_winner(board, move):
        return board, agent, move
    
    return board, "", move

def is_winner(board, move):
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

def is_valid(board, move):
    i, j = move
    if i >= 0 and i < BOARD_SIZE and j >= 0 and j < BOARD_SIZE and board[i, j] == BLANK_SYMBOL:
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
