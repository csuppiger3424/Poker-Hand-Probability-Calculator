import pytest
from classes.card import Card
from classes.deck import Deck

def test_deck_default_initialization():
    """
    Test the default initialization of the deck.
    """
    deck = Deck()
    assert len(deck.cards_list) == 52  # There should be 52 cards in a standard deck
    assert isinstance(deck.cards_list[0], Card)  # The first card should be an instance of Card

    # Test that the deck contains all suits and ranks
    suits = {"Spade", "Club", "Heart", "Diamond"}
    ranks = set(range(2, 15))
    cards = {(card.suit, card.number) for card in deck.cards_list}
    assert len(cards) == 52  # Ensure all cards are unique
    for suit in suits:
        for rank in ranks:
            assert (suit, rank) in cards

def test_deck_rigged_for_players_and_table():
    """
    Test the initialization of the deck with rigged player and table cards.
    """
    # Rigged cards for players and the table
    players = [
        {0: [Card("Spade", 10), Card("Heart", 11)]},  # Fixed cards for Player 0
        {1: [Card("Diamond", 12), Card("Club", 13)]},  # Fixed cards for Player 1
        {2: [Card("Heart", 2), Card("Spade", 3)]}  # Fixed cards for Player 2
    ]
    table_cards = [Card("Club", 4), Card("Club", 5), Card("Club", 6), Card("Heart", 7), Card("Diamond", 8)]

    deck = Deck(players=players, table_cards=table_cards)

    # Validate player cards
    assert deck.cards_list[0].compare_card(Card("Spade", 10))  # Player 0, Card 1
    assert deck.cards_list[1].compare_card(Card("Diamond", 12))  # Player 1, Card 1
    assert deck.cards_list[2].compare_card(Card("Heart", 2))  # Player 2, Card 1
    assert deck.cards_list[3].compare_card(Card("Heart", 11))  # Player 0, Card 2
    assert deck.cards_list[4].compare_card(Card("Club", 13))  # Player 1, Card 2
    assert deck.cards_list[5].compare_card(Card("Spade", 3))  # Player 2, Card 2

    # Validate burn card before the flop
    assert isinstance(deck.cards_list[6], Card)  # Burn card

    # Validate flop cards
    assert deck.cards_list[7].compare_card(Card("Club", 4))  # Flop card 1
    assert deck.cards_list[8].compare_card(Card("Club", 5))  # Flop card 2
    assert deck.cards_list[9].compare_card(Card("Club", 6))  # Flop card 3

    # Validate burn card before the turn
    assert isinstance(deck.cards_list[10], Card)  # Burn card

    # Validate turn card
    assert deck.cards_list[11].compare_card(Card("Heart", 7))  # Turn card

    # Validate burn card before the river
    assert isinstance(deck.cards_list[12], Card)  # Burn card

    # Validate river card
    assert deck.cards_list[13].compare_card(Card("Diamond", 8))  # River card

def test_deck_invalid_table_cards():
    """
    Test that initializing the deck with invalid table cards raises an error.
    """
    invalid_table_cards = [Card("Diamond", 2), Card("Diamond", 3)]  # Invalid length
    with pytest.raises(ValueError, match="The table must have 0, 3, 4, or 5 cards."):
        Deck(table_cards=invalid_table_cards)

def test_deck_table_cards_without_rigged_players():
    """
    Test that providing table cards without rigged player cards raises an error.
    """
    players = [
        {0: None},  # Random cards for Player 0
        {1: None},  # Random cards for Player 1
    ]
    table_cards = [Card("Club", 4), Card("Club", 5), Card("Club", 6)]

    with pytest.raises(ValueError, match="Table cards cannot be provided if there are no rigged player cards."):
        Deck(players=players, table_cards=table_cards)

def test_deck_randomized_for_unrigged_players():
    """
    Test that players without fixed cards are assigned random cards.
    """
    deck = Deck()

    # Ensure the deck size is reduced correctly
    assert len(deck.cards_list) == 52  # 52 - 4 cards dealt to players

def test_deck_random_players_and_table_cards():
    """
    Test that players without fixed cards are assigned random cards and table cards are in the correct order.
    """
    players = [
        {0: None},  # Random cards for Player 0
        {1: [Card("Diamond", 12), Card("Club", 13)]},  # Fixed cards for Player 1
        {2: None}  # Random cards for Player 2
    ]
    table_cards = [Card("Club", 4), Card("Club", 5), Card("Club", 6), Card("Heart", 7), Card("Diamond", 8)]

    deck = Deck(players=players, table_cards=table_cards)

    # Validate Player 0 has random cards
    assert isinstance(deck.cards_list[0], Card)  # Player 0, Card 1
    assert isinstance(deck.cards_list[3], Card)  # Player 0, Card 2

    # Validate Player 1 has fixed cards
    assert deck.cards_list[1].compare_card(Card("Diamond", 12))  # Player 1, Card 1
    assert deck.cards_list[4].compare_card(Card("Club", 13))  # Player 1, Card 2

    # Validate Player 2 has random cards
    assert isinstance(deck.cards_list[2], Card)  # Player 2, Card 1
    assert isinstance(deck.cards_list[5], Card)  # Player 2, Card 2

    # Validate burn card before the flop
    assert isinstance(deck.cards_list[6], Card)  # Burn card

    # Validate flop cards
    assert deck.cards_list[7].compare_card(Card("Club", 4))  # Flop card 1
    assert deck.cards_list[8].compare_card(Card("Club", 5))  # Flop card 2
    assert deck.cards_list[9].compare_card(Card("Club", 6))  # Flop card 3

    # Validate burn card before the turn
    assert isinstance(deck.cards_list[10], Card)  # Burn card

    # Validate turn card
    assert deck.cards_list[11].compare_card(Card("Heart", 7))  # Turn card

    # Validate burn card before the river
    assert isinstance(deck.cards_list[12], Card)  # Burn card

    # Validate river card
    assert deck.cards_list[13].compare_card(Card("Diamond", 8))  # River card

def test_deck_str():
    """
    Test the string representation of the deck.
    """
    deck = Deck()
    deck_str = str(deck)
    assert "START OF DECK" in deck_str
    assert "END OF DECK" in deck_str
    assert len(deck_str.splitlines()) > 2  # There should be cards listed between the start and end markers

def test_remove_card_from_top():
    """
    Test removing cards from the top of the deck.
    """
    deck = Deck()
    initial_length = len(deck.cards_list)

    top_card = deck.remove_card_from_top()
    assert isinstance(top_card, Card)  # The removed card should be an instance of Card
    assert len(deck.cards_list) == initial_length - 1  # The deck should have one less card

    # Remove all cards and ensure the deck becomes empty
    for _ in range(len(deck.cards_list)):
        deck.remove_card_from_top()
    assert len(deck.cards_list) == 0

    # Attempt to remove a card from an empty deck
    with pytest.raises(ValueError, match="The deck is empty. Cannot remove a card."):
        deck.remove_card_from_top()

def test_top_of_deck(capsys):
    """
    Test printing the top 10 cards of the deck.
    """
    deck = Deck()
    deck.top_of_deck()
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    assert len(output) <= 10  # Ensure no more than 10 cards are printed
    for line in output:
        assert isinstance(line, str)  # Each line should be a string

def test_deck_duplicate_card_error():
    """
    Test that initializing the deck with duplicate cards raises an error.
    """
    # Rigged cards for players with a duplicate card
    players = [
        {0: [Card("Spade", 10), Card("Heart", 11)]},  # Fixed cards for Player 0
        {1: [Card("Spade", 10), Card("Club", 13)]},  # Duplicate card for Player 1
    ]
    table_cards = [Card("Club", 4), Card("Club", 5), Card("Club", 6)]

    # Attempt to create a deck with duplicate cards
    with pytest.raises(ValueError, match="Duplicate card found in the deck: 10 of Spades"):
        Deck(players=players, table_cards=table_cards)