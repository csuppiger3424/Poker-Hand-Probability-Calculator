class Player:
    def __init__(self, name, hand, money):
        self.Name = name
        self.Hand = hand
        self.playing = False
        self.money = money

    def fold(self):
        self.playing = False

    def bet(self, money):
        self.money -= money