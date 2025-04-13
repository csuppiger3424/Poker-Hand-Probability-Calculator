import pytest
from classes.simulation import Simulation
from classes.card import Card
from classes.player import Player

def test_simulation_initialization():
    """
    Test initializing the simulation with valid parameters.
    """
    num_games = 10
    num_players = 3
    table_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12)]
    player1_cards = [Card("Heart", 2), Card("Heart", 3)]

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)

    assert simulation.num_games == num_games
    assert len(simulation.players) == num_players
    assert simulation.table_cards == table_cards
    assert simulation.player1_cards == player1_cards
    assert simulation.player1_win_percentage == 0.0

def test_simulation_run_with_rigged_deck():
    """
    Test running the simulation with a rigged deck.
    """
    num_games = 10
    num_players = 2
    table_cards = [Card("Spade", 10), Card("Heart", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    player1_cards = [Card("Heart", 10), Card("Spade", 11)]  # Player 1 has a Royal Flush

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)
    simulation.run()

    # Player 1 should win all games because they have a Royal Flush
    assert simulation.player1_win_percentage == 100.0

def test_simulation_run_with_random_players():
    """
    Test running the simulation with random player cards.
    """
    num_games = 100
    num_players = 3
    table_cards = []
    player1_cards = None  # Player 1 gets random cards

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)
    simulation.run()

    # Since the players have random cards, Player 1's win percentage should be between 0 and 100
    assert 0.0 <= simulation.player1_win_percentage <= 100.0

def test_simulation_run_with_partial_rigging():
    """
    Test running the simulation with partial rigging (Player 1 rigged, others random).
    """
    num_games = 50
    num_players = 4
    table_cards = [Card("Club", 4), Card("Club", 5), Card("Club", 6), Card("Heart", 7), Card("Diamond", 8)]
    player1_cards = [Card("Spade", 10), Card("Spade", 11)]  # Player 1 has rigged cards

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)
    simulation.run()

    # Player 1 has an advantage, so their win percentage should be greater than 0
    assert simulation.player1_win_percentage > 0.0

def test_simulation_get_player1_win_percentage():
    """
    Test retrieving Player 1's win percentage after running the simulation.
    """
    num_games = 10
    num_players = 2
    table_cards = [Card("Spade", 10), Card("Heart", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    player1_cards = [Card("Heart", 10), Card("Spade", 11)]  # Player 1 has a Royal Flush

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)
    simulation.run()

    # Player 1 should win all games because they have a Royal Flush
    assert simulation.get_player1_win_percentage() == 100.0

def test_simulation_random_player_generation():
    """
    Test that the simulation generates the correct number of players with random names and chips.
    """
    num_games = 5
    num_players = 6
    table_cards = []
    player1_cards = [Card("Heart", 2), Card("Heart", 3)]

    simulation = Simulation(num_games=num_games, num_players=num_players, table_cards=table_cards, player1_cards=player1_cards)

    # Ensure the correct number of players are generated
    assert len(simulation.players) == num_players

    # Ensure each player has a unique name
    player_names = [player.name for player in simulation.players]
    assert len(player_names) == len(set(player_names))  # No duplicate names

    # Ensure each player has a valid chip count
    for player in simulation.players:
        assert 500 <= player.chips <= 2000