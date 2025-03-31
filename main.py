from Classes.card import Card

def main():
    deck = []
    for i in range(1,14):
        card1 = Card("Spade", i)
        card2 = Card("Club", i)
        card3 = Card("Heart", i)
        card4 = Card("Diamond", i)
        deck.append(card1)
        deck.append(card2)
        deck.append(card3)
        deck.append(card4)

    for card in deck:
        print(card.toString())
        

if __name__ == "__main__":
    main()