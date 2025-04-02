from Classes.card import Card
from Classes.deck import Deck
from Classes.player import Player
from Classes.table import Table

def main():
    d = Deck()
    colby = Player("Colby", 1000)
    ben = Player("Ben", 1000)
    vaughn = Player("Vaughn", 1000)
    players = [colby, ben, vaughn]

    t = Table(players)
    t.deal()

    print(t.deck)
    print(t.players[0].hand)

        
if __name__ == "__main__":
    main()
    