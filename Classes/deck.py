import random
from Classes.card import Card

class Deck:
    deck = []
    for i in range(1,14):
        deck.append(Card("Spade", i))
        deck.append(Card("Club", i))
        deck.append(Card("Heart", i))
        deck.append(Card("Diamond", i))
    random.shuffle(deck)

    def __str__(self):
        for i in range(len(self.deck)):
            print(self.deck[i])
        return "--------------------------"