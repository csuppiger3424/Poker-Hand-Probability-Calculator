import random
from classes.card import Card

class Deck:
    def __init__(self):
        self.cards_list = []
        for i in range(2,15):
            self.cards_list.append(Card("Spade", i))
            self.cards_list.append(Card("Club", i))
            self.cards_list.append(Card("Heart", i))
            self.cards_list.append(Card("Diamond", i))
        random.shuffle(self.cards_list)

    def __str__(self):
        string_to_return =""
        string_to_return += "START OF DECK" + "\n"
        for i in range(len(self.cards_list)):
            string_to_return += str(self.cards_list[i]) + "\n"
        string_to_return += "END OF DECK" + "\n"
        return string_to_return
    
    def top_of_deck(self):
        for i in range(len(self.cards_list),10):
            print(self.cards_list[i])