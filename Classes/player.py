from classes.card import Card
from classes.deck import Deck
from classes.hand import Hand

class Player:
    def __init__(self, name, money, cards_list=None):
        """
        Initialize a player with a name, starting money, and an optional list of cards.
        """
        self.name = name
        self.playing = True
        self.hand = Hand(cards_list if cards_list else [])
        if money < 0:
            raise ValueError("Money cannot be negative")
        self.chips = money

    def __str__(self):
        """
        Return a string representation of the player.
        """
        return f"{self.name} has {self.chips} chips and the following hand: {self.hand}"
    
    def reset_hand(self):
        """
        Reset the player's hand for a new round.
        """
        self.hand.reset_hand()

    def fold(self):
        """
        Mark the player as no longer playing in the current round.
        """
        self.playing = False

    def check(self):
        """
        Allow the player to check (take no action but stay in the game).
        """
        if not self.playing:
            raise ValueError(f"{self.name} cannot check because they have folded.")
        return f"{self.name} checks."

    def bet(self, amount):
        """
        Deduct the bet amount from the player's chips.
        """
        if amount > self.chips:
            raise ValueError(f"{self.name} does not have enough chips to bet {amount}.")
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        self.chips -= amount
        return f"{self.name} bets {amount} chips."

    def add_card(self, card):
        """
        Add a card to the player's hand.
        """
        self.hand.add_card(card)

    def reset_hand(self):
        """
        Reset the player's hand for a new round.
        """
        self.hand = Hand([])

    def is_playing(self):
        """
        Check if the player is still in the game.
        """
        return self.playing

    def get_hand_type(self):
        """
        Get the type of hand the player currently has.
        """
        return self.hand.get_hand_type()

    def get_chips(self):
        """
        Get the current chip count of the player.
        """
        return self.chips