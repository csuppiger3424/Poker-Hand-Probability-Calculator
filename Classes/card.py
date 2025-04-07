class Card:
    def __init__(self, suit, number):
        valid_suits = ["Spade", "Club", "Heart", "Diamond"]
        if suit not in valid_suits:
            raise ValueError(f"Invalid suit: {suit}. Valid suits are: {valid_suits}.")
        self.suit = suit
        if number < 2 or number > 14:
            raise ValueError(f"Invalid card number: {number}. Valid numbers are from 2 to 14.")
        self.number = number

    def __str__(self):
        if self.number == 14:
            return "Ace of " + self.suit + "s"
        elif self.number == 11:
            return "Jack of " + self.suit + "s"
        elif self.number == 12:
            return "Queen of " + self.suit + "s"
        elif self.number == 13:
            return "King of " + self.suit + "s"
        else:
            return str(self.number) + " of " + self.suit + "s"