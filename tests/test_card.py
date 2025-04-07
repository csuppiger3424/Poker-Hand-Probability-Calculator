import pytest

from classes.card import Card

def test_card_init():
    card = Card("Hearts", 10)
    assert card.suit == "Hearts"
    assert card.number == 10

def test_card_str():
    card = Card("Diamonds", 5)
    assert str(card) == "5 of Diamonds"

# def test_invalid_card_init():
#     with pytest.raises(ValueError):
#         Card("InvalidSuit", 10)
#     with pytest.raises(ValueError):
#         Card("Hearts", 15)  # Invalid number for a card
#     with pytest.raises(ValueError):
#         Card("Diamonds", -1)  # Invalid number for a card

