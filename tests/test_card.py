import pytest

from classes.card import Card

def test_card_init():
    card = Card("Heart", 10)
    assert card.suit == "Heart"
    assert card.number == 10

    card = Card("Spade", 2)
    assert card.suit == "Spade"
    assert card.number == 2

    card = Card("Diamond", 14)
    assert card.suit == "Diamond"
    assert card.number == 14

    card = Card("Club", 11)
    assert card.suit == "Club"
    assert card.number == 11

def test_card_str():
    card = Card("Diamond", 5)
    assert str(card) == "5 of Diamonds"

    card = Card("Spade", 14)
    assert str(card) == "Ace of Spades"

    card = Card("Club", 11)
    assert str(card) == "Jack of Clubs"

    card = Card("Heart", 12)
    assert str(card) == "Queen of Hearts"

def test_invalid_card_init():
    with pytest.raises(ValueError):
        Card("InvalidSuit", 10)
    with pytest.raises(ValueError):
        Card("Hearts", 15)  # Invalid number for a card
    with pytest.raises(ValueError):
        Card("Diamonds", -1)  # Invalid number for a card

