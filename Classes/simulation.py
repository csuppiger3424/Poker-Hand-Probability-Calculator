import random
from classes.game import Game
from classes.table import Table
from classes.deck import Deck
from classes.player import Player

class Simulation:
    def __init__(self, num_games, num_players, table_cards, player1_cards):
        """
        Initialize the simulation.
        Args:
            num_games (int): Number of games to simulate.
            num_players (int): Number of players participating in the game.
            table_cards (list of Card): Fixed community cards for the table (0, 3, 4, or 5 cards).
            player1_cards (list of Card): The two cards that will be given to Player 1.
        """
        self.num_games = num_games
        self.num_players = num_players
        self.players = self._generate_players(num_players)
        self.table_cards = table_cards
        self.player1_cards = player1_cards
        self.player1_win_percentage = 0.0

    def _generate_players(self, num_players):
        """
        Generate a list of Player objects with random names and starting chips.
        Args:
            num_players (int): Number of players to generate.
        Returns:
            list of Player: A list of randomly generated Player objects.
        """
        names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
        random.shuffle(names)
        players = [Player(names[i], random.randint(500, 2000)) for i in range(num_players)]
        return players

    def run(self):
        """
        Run the simulation for the specified number of games.
        """
        player1_wins = 0

        for _ in range(self.num_games):
            # Rig the deck for Player 1
            rigged_players = [
                {0: self.player1_cards}  # Player 1 gets the specified cards
            ] + [{i: None} for i in range(1, self.num_players)]  # Other players get random cards

            # Create a rigged deck
            deck = Deck(players=rigged_players, table_cards=self.table_cards)

            # Create a table
            table = Table(deck, self.players)

            # Create and play the game
            game = Game(table)
            game.play_game()

            # Determine the winner
            winner = game.determine_winner()

            # Check if Player 1 (index 0) won
            if winner == self.players[0]:
                player1_wins += 1

            # Reset players' hands for the next game
            for player in self.players:
                player.reset_hand()

        # Calculate Player 1's win percentage
        self.player1_win_percentage = (player1_wins / self.num_games) * 100

    def get_player1_win_percentage(self):
        """
        Get the percentage of games Player 1 won.
        Returns:
            float: The percentage of games Player 1 won.
        """
        return self.player1_win_percentage