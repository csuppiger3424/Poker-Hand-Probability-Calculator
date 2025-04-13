from classes.deck import Deck
from classes.card import Card
from classes.player import Player

class Table:
    def __init__(self, deck, players):
        """
        Initialize the table with a deck and a list of players.
        Args:
            deck (Deck): The deck object to be used for the game.
            players (list of Player): A list of Player objects participating in the game.
        """
        self.deck = deck  # The deck used for the game
        self.players = players  # List of Player objects
        self.cards = []  # Community cards on the table
        self.pot = 0  # Total money in the pot

    def add_to_pot(self, amount):
        """
        Add money to the pot.
        """
        if amount < 0:
            raise ValueError("Cannot add a negative amount to the pot.")
        self.pot += amount

    def deal(self):
        """
        Deal two cards to each player in a round-robin fashion.
        """
        for _ in range(2):  # Each player gets 2 cards
            for player in self.players:
                player.add_card(self.deck.remove_card_from_top())

    def flop(self):
        """
        Deal the flop (three community cards) and add them to each player's hand.
        """
        self.deck.remove_card_from_top()  # Burn one card
        for _ in range(3):  # Deal three flop cards
            card = self.deck.remove_card_from_top()
            self.cards.append(card)
            for player in self.players:
                player.add_card(card)

    def turn(self):
        """
        Deal the turn (one community card) and add it to each player's hand.
        """
        self.deck.remove_card_from_top()  # Burn one card
        card = self.deck.remove_card_from_top()  # Turn card
        self.cards.append(card)
        for player in self.players:
            player.add_card(card)

    def river(self):
        """
        Deal the river (one community card) and add it to each player's hand.
        """
        self.deck.remove_card_from_top()  # Burn one card
        card = self.deck.remove_card_from_top()  # River card
        self.cards.append(card)
        for player in self.players:
            player.add_card(card)

    def __str__(self):
        """
        Return a string representation of the table.
        """
        community_cards = ', '.join(str(card) for card in self.cards) if self.cards else "No community cards"
        return f"Pot: {self.pot}\nCommunity Cards: {community_cards}\nPlayers: {[player.name for player in self.players]}"
