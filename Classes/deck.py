import random
from classes.card import Card

class Deck:
    def __init__(self, players=None, table_cards=None):
        """
        Initialize the deck with optional fixed cards for players and the table.
        Args:
            players (list of dict): A list of dictionaries where each dictionary represents a player.
                Each dictionary should have a key (player index starting at 0) and a list of fixed cards as the value.
                Example: [{0: [Card("Spade", 10), Card("Heart", 11)]}, {1: None}, {2: [Card("Diamond", 2), Card("Diamond", 3)]}]
            table_cards (list of Card): Fixed community cards for the table (0, 3, 4, or 5 cards).
        """
        self.cards_list = []

        # Add all cards to the deck
        for i in range(2, 15):
            self.cards_list.append(Card("Spade", i))
            self.cards_list.append(Card("Club", i))
            self.cards_list.append(Card("Heart", i))
            self.cards_list.append(Card("Diamond", i))

        # Validate table cards
        if table_cards and len(table_cards) not in {0, 3, 4, 5}:
            raise ValueError("The table must have 0, 3, 4, or 5 cards.")

        # Ensure table_cards cannot exist without rigged player cards
        if table_cards and (not players or all(player.get(list(player.keys())[0]) is None for player in players)):
            raise ValueError("Table cards cannot be provided if there are no rigged player cards.")

        # Handle None for players
        players = players or []

        # Remove fixed cards for players and table from the deck
        for player in players:
            for index, cards in player.items():
                if cards:
                    for fixed_card in cards:
                        self._remove_card(fixed_card)

        # Handle None for table cards
        table_cards = table_cards or []
        if table_cards:
            for fixed_card in table_cards:
                self._remove_card(fixed_card)

        # Shuffle the remaining cards
        random.shuffle(self.cards_list)

        # Rig the deck
        rigged_deck = []

        # Add player cards in the correct order
        max_players = len(players)
        for i in range(2):  # Each player gets 2 cards
            for player_index in range(max_players):
                player_cards = players[player_index].get(player_index, None)
                if player_cards:
                    rigged_deck.append(player_cards[i])
                else:
                    rigged_deck.append(self.cards_list.pop(0))  # Assign random card if not rigged

        # Add burn card before the flop
        rigged_deck.append(self.cards_list.pop(0))

        # Add flop cards
        if len(table_cards) >= 3:
            rigged_deck.extend(table_cards[:3])

        # Add burn card before the turn
        if len(table_cards) >= 4:
            rigged_deck.append(self.cards_list.pop(0))

        # Add turn card
        if len(table_cards) >= 4:
            rigged_deck.append(table_cards[3])

        # Add burn card before the river
        if len(table_cards) == 5:
            rigged_deck.append(self.cards_list.pop(0))

        # Add river card
        if len(table_cards) == 5:
            rigged_deck.append(table_cards[4])

        # Add the remaining shuffled cards to the deck
        rigged_deck.extend(self.cards_list)
        self.cards_list = rigged_deck

        # Check for duplicate cards
        self._validate_no_duplicates()

    def _remove_card(self, card):
        """
        Remove a specific card from the deck.
        """
        for i, deck_card in enumerate(self.cards_list):
            if deck_card.suit == card.suit and deck_card.number == card.number:
                del self.cards_list[i]
                break

    def _validate_no_duplicates(self):
        """
        Validate that there are no duplicate cards in the deck.
        """
        seen_cards = set()
        for card in self.cards_list:
            card_tuple = (card.suit, card.number)
            if card_tuple in seen_cards:
                raise ValueError(f"Duplicate card found in the deck: {card}")
            seen_cards.add(card_tuple)

    def __str__(self):
        string_to_return = ""
        string_to_return += "START OF DECK" + "\n"
        for i in range(len(self.cards_list)):
            string_to_return += str(self.cards_list[i]) + "\n"
        string_to_return += "END OF DECK" + "\n"
        return string_to_return

    def remove_card_from_top(self):
        """
        Remove and return the top card from the deck.
        """
        if not self.cards_list:
            raise ValueError("The deck is empty. Cannot remove a card.")
        return self.cards_list.pop(0)

    def top_of_deck(self):
        """
        Print the top 10 cards of the deck.
        """
        # for i in range(min(len(self.cards_list), 10)):
            # print(self.cards_list[i])