import time
import flask
import gomoku_game 


app = flask.Flask(__name__)


import teams.dumb_agent
import teams.dumber_agent

p1 = teams.dumb_agent.GomokuAgent(gomoku_game.PLAYER_1_SYMBOL, gomoku_game.BLANK_SYMBOL, gomoku_game.PLAYER_2_SYMBOL)
p2 = teams.dumber_agent.GomokuAgent(gomoku_game.PLAYER_2_SYMBOL, gomoku_game.BLANK_SYMBOL, gomoku_game.PLAYER_1_SYMBOL)
game = gomoku_game.GomokuGame(p1, p2)

team_info = {
    "player1": {"name": p1.name, "symbol": "X"},
    "player2": {"name": p2.name, "symbol": "O"}
}

@app.route("/")
def index():
    return flask.render_template("index.html", team_info=team_info)

@app.route("/get_board")
def get_board():
    return flask.jsonify(game.board.tolist())

@app.route("/play_turn")
def play_turn():
    board, winner = game.play_turn()
    winner_symbol = winner.agent_symbol if winner else None
    return flask.jsonify({"board": board.tolist(), "winner": winner_symbol})

if __name__ == "__main__":
    app.run(debug=True)
