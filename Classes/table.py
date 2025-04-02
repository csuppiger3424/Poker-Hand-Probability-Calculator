from Classes.deck import Deck
from Classes.card import Card
from Classes.player import Player

class Table:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.turn = 0
        self.pot = 0

    def nextRound(self):
        self.players.append(self.players.pop(0))

    def deal(self):
        for i in range(len(self.players)):
            self.players[i].getCard(self.deck.deck[0])
            self.deck.deck.pop(0)
        for i in range(len(self.players)):
            self.players[i].getCard(self.deck.deck[0])
            self.deck.deck.pop(0)