import pytest
from classes.table import Table
from classes.card import Card
from classes.deck import Deck
from classes.player import Player

def test_table_init():
    """
    Test initialization of the table with a deck and players.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    assert len(table.players) == 2
    assert table.players[0].name == "Alice"
    assert table.players[1].name == "Bob"
    assert len(table.cards) == 0  # No community cards initially
    assert table.pot == 0  # Pot starts at 0
    assert len(table.deck.cards_list) == 52  # Full deck of cards

def test_table_init_multiple_players():
    """
    Test initialization with more than 2 players.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    player3 = Player("Charlie", 1000)
    table = Table(deck, [player1, player2, player3])

    assert len(table.players) == 3
    assert table.players[0].name == "Alice"
    assert table.players[1].name == "Bob"
    assert table.players[2].name == "Charlie"
    assert len(table.cards) == 0  # No community cards initially
    assert table.pot == 0  # Pot starts at 0
    assert len(table.deck.cards_list) == 52  # Full deck of cards

def test_add_to_pot():
    """
    Test adding money to the pot.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    table.add_to_pot(100)
    assert table.pot == 100

    table.add_to_pot(200)
    assert table.pot == 300

    # Test adding a negative amount
    with pytest.raises(ValueError, match="Cannot add a negative amount to the pot."):
        table.add_to_pot(-50)

def test_deal():
    """
    Test dealing cards to players.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    table.deal()

    assert len(player1.hand.cards_list) == 2
    assert len(player2.hand.cards_list) == 2
    assert len(table.deck.cards_list) == 48  # 4 cards dealt

def test_deal_multiple_players():
    """
    Test dealing cards to more than 2 players.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    player3 = Player("Charlie", 1000)
    table = Table(deck, [player1, player2, player3])

    table.deal()

    assert len(player1.hand.cards_list) == 2
    assert len(player2.hand.cards_list) == 2
    assert len(player3.hand.cards_list) == 2
    assert len(table.deck.cards_list) == 46  # 6 cards dealt

def test_flop():
    """
    Test dealing the flop (three community cards).
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    table.deal()  # Deal cards to players first
    table.flop()

    assert len(table.cards) == 3  # Three community cards
    assert len(table.deck.cards_list) == 44  # 1 card burned + 3 dealt
    assert len(player1.hand.cards_list) == 5  # 2 player cards + 3 community cards
    assert len(player2.hand.cards_list) == 5  # 2 player cards + 3 community cards

def test_turn():
    """
    Test dealing the turn (one community card).
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    table.deal()  # Deal cards to players first
    table.flop()  # Deal the flop first
    table.turn()

    assert len(table.cards) == 4  # Three flop cards + one turn card
    assert len(table.deck.cards_list) == 42  # 1 card burned + 3 dealt after flop + 1 card burned + 1 dealt after turn
    assert len(player1.hand.cards_list) == 6  # 2 player cards + 4 community cards
    assert len(player2.hand.cards_list) == 6  # 2 player cards + 4 community cards

def test_river():
    """
    Test dealing the river (one community card).
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    table.deal()  # Deal cards to players first
    table.flop()  # Deal the flop first
    table.turn()  # Deal the turn
    table.river()

    assert len(table.cards) == 5  # Three flop cards + one turn card + one river card
    assert len(table.deck.cards_list) == 40  # 1 card burned + 1 dealt after turn + 1 card burned + 1 dealt after river
    assert len(player1.hand.cards_list) == 7  # 2 player cards + 5 community cards
    assert len(player2.hand.cards_list) == 7  # 2 player cards + 5 community cards

def test_table_str():
    """
    Test the string representation of the table.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])

    assert str(table) == "Pot: 0\nCommunity Cards: No community cards\nPlayers: ['Alice', 'Bob']"

    table.add_to_pot(200)
    table.deal()  # Deal cards to players first
    table.flop()
    assert "Pot: 200" in str(table)
    assert "Community Cards:" in str(table)
    assert "Players: ['Alice', 'Bob']" in str(table)

def test_rigged_deck_with_royal_flush_and_four_of_a_kind():
    """
    Test a rigged deck where:
    - Player 1 has a Royal Flush.
    - Player 2 has Four of a Kind.
    - Player 3 has random cards.
    """
    # Rigged cards for players
    players = [
        {0: [Card("Spade", 10), Card("Spade", 11)]},  # Player 1's rigged cards (part of Royal Flush)
        {1: [Card("Spade", 9), Card("Diamond", 9)]},  # Player 2's rigged cards (part of Four of a Kind)
        {2: None}  # Player 3 gets random cards
    ]

    # Rigged community cards
    table_cards = [
        Card("Spade", 12),  # Queen of Spades
        Card("Spade", 13),  # King of Spades
        Card("Spade", 14),  # Ace of Spades
        Card("Heart", 9),   # Part of Four of a Kind
        Card("Club", 9)     # Random card
    ]

    # Create the rigged deck
    deck = Deck(players=players, table_cards=table_cards)

    # Create players
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    player3 = Player("Charlie", 1000)

    # Create a table with the rigged deck
    table = Table(deck, [player1, player2, player3])

    # Deal cards to players
    table.deal()

    # Validate Player 1's hand (Royal Flush)
    assert player1.hand.cards_list[0].compare_card(Card("Spade", 10))  # 10 of Spades
    assert player1.hand.cards_list[1].compare_card(Card("Spade", 11))  # Jack of Spades

    # Validate Player 2's hand (Four of a Kind)
    assert player2.hand.cards_list[0].compare_card(Card("Spade", 9))  # 9 of Spades
    assert player2.hand.cards_list[1].compare_card(Card("Diamond", 9))  # 9 of Diamonds

    # Validate Player 3's hand (Random cards)
    assert isinstance(player3.hand.cards_list[0], Card)
    assert isinstance(player3.hand.cards_list[1], Card)

    # Deal the flop, turn, and river
    table.flop()
    table.turn()
    table.river()

    # Validate the community cards
    assert table.cards[0].compare_card(Card("Spade", 12))  # Queen of Spades
    assert table.cards[1].compare_card(Card("Spade", 13))  # King of Spades
    assert table.cards[2].compare_card(Card("Spade", 14))  # Ace of Spades
    assert table.cards[3].compare_card(Card("Heart", 9))   # 9 of Hearts
    assert table.cards[4].compare_card(Card("Club", 9))    # 9 of Clubs

    # Validate Player 1's full hand (Royal Flush)
    assert len(player1.hand.cards_list) == 7
    assert player1.hand.cards_list[2].compare_card(Card("Spade", 12))  # Queen of Spades
    assert player1.hand.cards_list[3].compare_card(Card("Spade", 13))  # King of Spades
    assert player1.hand.cards_list[4].compare_card(Card("Spade", 14))  # Ace of Spades
    assert player1.hand.cards_list[5].compare_card(Card("Heart", 9))   # 9 of Hearts
    assert player1.hand.cards_list[6].compare_card(Card("Club", 9))    # 9 of Clubs

    # Validate Player 2's full hand (Four of a Kind)
    assert len(player2.hand.cards_list) == 7
    assert player2.hand.cards_list[2].compare_card(Card("Spade", 12))  # Queen of Spades
    assert player2.hand.cards_list[3].compare_card(Card("Spade", 13))  # King of Spades
    assert player2.hand.cards_list[4].compare_card(Card("Spade", 14))  # Ace of Spades
    assert player2.hand.cards_list[5].compare_card(Card("Heart", 9))   # 9 of Hearts
    assert player2.hand.cards_list[6].compare_card(Card("Club", 9))    # 9 of Clubs

    # Validate Player 3's full hand (Random cards + community cards)
    assert len(player3.hand.cards_list) == 7
    assert player3.hand.cards_list[2].compare_card(Card("Spade", 12))  # Queen of Spades
    assert player3.hand.cards_list[3].compare_card(Card("Spade", 13))  # King of Spades
    assert player3.hand.cards_list[4].compare_card(Card("Spade", 14))  # Ace of Spades
    assert player3.hand.cards_list[5].compare_card(Card("Heart", 9))   # 9 of Hearts
    assert player3.hand.cards_list[6].compare_card(Card("Club", 9))    # 9 of Clubs

def test_rigged_deck_with_straight_and_flush():
    """
    Test a rigged deck where:
    - Player 1 has a Straight.
    - Player 2 has a Flush.
    """
    # Rigged cards for players
    players = [
        {0: [Card("Heart", 5), Card("Diamond", 6)]},  # Player 1's rigged cards (part of Straight)
        {1: [Card("Spade", 2), Card("Spade", 4)]}  # Player 2's rigged cards (part of Flush)
    ]

    # Rigged community cards
    table_cards = [
        Card("Spade", 7),  # Part of Straight and Flush
        Card("Heart", 8),  # Part of Straight
        Card("Diamond", 9),  # Part of Straight
        Card("Spade", 6),  # Part of Flush
        Card("Spade", 8)  # Part of Flush
    ]

    # Create the rigged deck
    deck = Deck(players=players, table_cards=table_cards)

    # Create players
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)

    # Create a table with the rigged deck
    table = Table(deck, [player1, player2])

    # Deal cards to players
    table.deal()

    # Validate Player 1's hand (Straight)
    assert player1.hand.cards_list[0].compare_card(Card("Heart", 5))  # 5 of Hearts
    assert player1.hand.cards_list[1].compare_card(Card("Diamond", 6))  # 6 of Diamonds

    # Validate Player 2's hand (Flush)
    assert player2.hand.cards_list[0].compare_card(Card("Spade", 2))  # 2 of Spades
    assert player2.hand.cards_list[1].compare_card(Card("Spade", 4))  # 4 of Spades

    # Deal the flop, turn, and river
    table.flop()
    table.turn()
    table.river()

    # Validate the community cards
    assert table.cards[0].compare_card(Card("Spade", 7))  # 7 of Clubs
    assert table.cards[1].compare_card(Card("Heart", 8))  # 8 of Hearts
    assert table.cards[2].compare_card(Card("Diamond", 9))  # 9 of Diamonds
    assert table.cards[3].compare_card(Card("Spade", 6))  # 6 of Spades
    assert table.cards[4].compare_card(Card("Spade", 8))  # 8 of Spades

    # Validate Player 1's full hand (Straight)
    assert player1.get_hand_type() == "Straight"

    # Validate Player 2's full hand (Flush)
    assert player2.get_hand_type() == "Flush"

def test_rigged_deck_with_three_of_a_kind():
    """
    Test a rigged deck where:
    - Player 1 has Three of a Kind.
    - Other players have random cards.
    """
    # Rigged cards for players
    players = [
        {0: [Card("Heart", 10), Card("Diamond", 10)]},  # Player 1's rigged cards (part of Three of a Kind)
        {1: [Card("Spade", 2), Card("Club", 3)]},  # Player 2's random cards
        {2: [Card("Heart", 4), Card("Diamond", 5)]},  # Player 3's random cards
        {3: [Card("Spade", 6), Card("Club", 7)]}  # Player 4's random cards
    ]

    # Rigged community cards
    table_cards = [
        Card("Club", 10),  # Part of Three of a Kind
        Card("Heart", 2),  # Random card
        Card("Diamond", 3),  # Random card
        Card("Spade", 4),  # Random card
        Card("Club", 5)  # Random card
    ]

    # Create the rigged deck
    deck = Deck(players=players, table_cards=table_cards)

    # Create players
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    player3 = Player("Charlie", 1000)
    player4 = Player("Diana", 1000)

    # Create a table with the rigged deck
    table = Table(deck, [player1, player2, player3, player4])

    # Deal cards to players
    table.deal()

    # Validate Player 1's hand (Three of a Kind)
    assert player1.hand.cards_list[0].compare_card(Card("Heart", 10))  # 10 of Hearts
    assert player1.hand.cards_list[1].compare_card(Card("Diamond", 10))  # 10 of Diamonds

    # Validate Player 2's hand (Random cards)
    assert player2.hand.cards_list[0].compare_card(Card("Spade", 2))  # 2 of Spades
    assert player2.hand.cards_list[1].compare_card(Card("Club", 3))  # 3 of Clubs

    # Validate Player 3's hand (Random cards)
    assert player3.hand.cards_list[0].compare_card(Card("Heart", 4))  # 4 of Hearts
    assert player3.hand.cards_list[1].compare_card(Card("Diamond", 5))  # 5 of Diamonds

    # Validate Player 4's hand (Random cards)
    assert player4.hand.cards_list[0].compare_card(Card("Spade", 6))  # 6 of Spades
    assert player4.hand.cards_list[1].compare_card(Card("Club", 7))  # 7 of Clubs

    # Deal the flop, turn, and river
    table.flop()
    table.turn()
    table.river()

    # Validate the community cards
    assert table.cards[0].compare_card(Card("Club", 10))  # 10 of Clubs
    assert table.cards[1].compare_card(Card("Heart", 2))  # 2 of Hearts
    assert table.cards[2].compare_card(Card("Diamond", 3))  # 3 of Diamonds
    assert table.cards[3].compare_card(Card("Spade", 4))  # 4 of Spades
    assert table.cards[4].compare_card(Card("Club", 5))  # 5 of Clubs

    # Validate Player 1's full hand (Three of a Kind)
    assert player1.get_hand_type() == "Three of a Kind"