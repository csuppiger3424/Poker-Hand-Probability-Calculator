from classes.table import Table

class Game:
    def __init__(self, table):
        """
        Initialize the game with a table.
        Args:
            table (Table): The table object containing players, the deck, and the pot.
        """
        self.table = table

    def play_game(self):
        """
        Play out the entire game.
        """
        # print("Starting the game...")

        # Deal cards to players
        # print("Dealing cards to players...")
        self.table.deal()
        self.display_player_hands()

        # Deal the flop
        # print("Dealing the flop...")
        self.table.flop()
        self.display_community_cards()

        # Deal the turn
        # print("Dealing the turn...")
        self.table.turn()
        self.display_community_cards()

        # Deal the river
        # print("Dealing the river...")
        self.table.river()
        self.display_community_cards()

        # Determine the winner
        # print("Determining the winner...")
        winner = self.determine_winner()
        # print(f"The winner is {winner.name} with a {winner.get_hand_type()}!")

    def display_player_hands(self):
        """
        Display the hands of all players.
        """
        # for player in self.table.players:
            # print(f"{player.name}'s hand: {player.hand}")

    def display_community_cards(self):
        """
        Display the community cards on the table.
        """
        community_cards = ', '.join(str(card) for card in self.table.cards)
        # print(f"Community cards: {community_cards}")

    def determine_winner(self):
        """
        Determine the winner of the game based on the best hand.
        Returns:
            Player: The player with the best hand.
        """
        best_player = None
        best_hand = None

        for player in self.table.players:
            if not player.is_playing():
                continue

            if best_player is None or player.hand.compare_with(best_hand) == 1:
                best_player = player
                best_hand = player.hand

        return best_player