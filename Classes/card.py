class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __str__(self):
        if self.number == 1:
            return "Ace of " + self.suit + "s"
        elif self.number == 11:
            return "Jack of " + self.suit + "s"
        elif self.number == 12:
            return "Queen of " + self.suit + "s"
        elif self.number == 13:
            return "King of " + self.suit + "s"
        else:
            return str(self.number) + " of " + self.suit + "s"