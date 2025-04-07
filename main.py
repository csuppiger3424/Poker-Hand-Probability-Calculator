from classes.card import Card
from classes.deck import Deck
from classes.player import Player
from classes.table import Table
from classes.hand import Hand

def main():
    d = Deck()
    colby = Player("Colby", 1000)
    ben = Player("Ben", 1000)
    vaughn = Player("Vaughn", 1000)
    players = [colby, ben, vaughn]

    t = Table(players)
    t.deal()

    cards1 = []
    cards1.append(Card("Club", 6))
    cards1.append(Card("Heart", 4))
    cards1.append(Card("Spade", 3))
    cards1.append(Card("Diamond", 5))
    cards1.append(Card("Club", 7))
    cards1.append(Card("Spade", 8))

    h1 = Hand(cards1)

    cards2 = []
    cards2.append(Card("Club", 2))
    cards2.append(Card("Club", 4))
    cards2.append(Card("Club", 3))
    cards2.append(Card("Spade", 5))
    cards2.append(Card("Club", 6))
    cards2.append(Card("Spade", 9))

    h2 = Hand(cards2)
    print(h1.getHandType())
    print(h2.getHandType())
    print(h1.compareHands(h2))
    
    # for i in range(10):
    #     print(t.deck.deck[i])

    # print("dealing---------------")
    # t.deal()

    # for i in range(10):
    #     print(t.deck.deck[i])

    # print("flop---------------")
    # t.flop()

    # for i in range(10):
    #     print(t.deck.deck[i])

    # print("table cards---------------")
    # for i in range(len(t.cards)):
    #     print(t.cards[i])

    # print("turn---------------")
    # t.turnRiver()

    # for i in range(10):
    #     print(t.deck.deck[i])

    # print("table cards---------------")
    # for i in range(len(t.cards)):
    #     print(t.cards[i])

    # print("river---------------")
    # t.turnRiver()

    # for i in range(10):
    #     print(t.deck.deck[i])

    # print("table cards---------------")
    # for i in range(len(t.cards)):
    #     print(t.cards[i])

        
if __name__ == "__main__":
    main()
    