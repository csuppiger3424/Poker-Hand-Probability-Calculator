from classes.deck import Deck
from classes.card import Card
from classes.player import Player

class Table:
    def __init__(self, players):
        self.cards = []
        self.deck = Deck()
        self.players = players
        self.turn = 0
        self.pot = 0

    def nextRound(self):
        self.players.append(self.players.pop(0))

    def deal(self):
        for i in range(len(self.players)):
            self.players[i].getCard(self.deck.cards_list[0])
            self.deck.cards_list.pop(0)
            self.players[i].getCard(self.deck.cards_list[0])
            self.deck.cards_list.pop(0)

    def flop(self):
        self.deck.cards_list.pop(0)
        self.cards.append(self.deck.cards_list.pop(0))
        self.cards.append(self.deck.cards_list.pop(0))
        self.cards.append(self.deck.cards_list.pop(0))

    def turnRiver(self):
        self.deck.cards_list.pop(0)
        self.cards.append(self.deck.cards_list.pop(0))
