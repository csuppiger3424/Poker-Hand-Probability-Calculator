class Player:

    def __init__(self, name, money):
        self.name = name
        self.playing = True
        self.money = money
        self.hand = []

    def __str__(self):
        return str(self.name + " has " + str(self.money) + " dollars")

    def fold(self):
        self.playing = False

    def bet(self, money):
        self.money -= money

    def getCard(self, card):
        self.hand.append(card)