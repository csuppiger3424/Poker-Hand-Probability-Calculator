class Player:

    def __init__(self, name, money):
        self.name = name
        self.playing = True
        if money < 0:
            raise ValueError("Money cannot be negative")
        self.chips = money
        self.cards_list = []

    def __str__(self):
        return str(self.name + " has " + str(self.chips) + " dollars")

    def fold(self):
        self.playing = False

    def bet(self, money):
        self.chips -= money

    def add_card(self, card):
        self.cards_list.append(card)