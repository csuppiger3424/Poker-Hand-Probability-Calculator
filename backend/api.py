from flask import Flask, request, jsonify
from classes.simulation import Simulation
from classes.card import Card

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    num_games = data['num_games']
    num_players = data['num_players']
    player_cards = [Card(c['suit'], c['rank']) for c in data['player_cards']]
    table_cards = [Card(c['suit'], c['rank']) for c in data['table_cards']]

    sim = Simulation(num_games, num_players, table_cards, player_cards)
    sim.run()

    return jsonify({
        'player1_win_percentage': sim.player1_win_percentage
    })

if __name__ == '__main__':
    app.run(debug=True)