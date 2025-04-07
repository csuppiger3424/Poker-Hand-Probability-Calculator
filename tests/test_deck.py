import pytest
import random

from classes.card import Card
from classes.deck import Deck

def test_deck_initialization():
    deck = Deck()
    assert len(deck.cards_list) == 52  # There should be 52 cards in a standard deck
    assert isinstance(deck.cards_list[0], Card)  # The first card should be an instance of Card

def test_deck_shuffle():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1.cards_list != deck2.cards_list  # The decks should be different after shuffling

def test_deck_str():
    deck = Deck()
    deck_str = str(deck)
    assert "START OF DECK" in deck_str
    assert "END OF DECK" in deck_str
    assert len(deck_str.splitlines()) > 2  # There should be cards listed between the start and end markers

# def test_top_of_deck():
#     deck = Deck()
#     deck_str = deck.top_of_deck()
#     assert "START OF DECK" in deck_str
#     assert "END OF DECK" in deck_str
#     assert len(deck_str.splitlines()) > 2  # There should be cards listed between the start and end markers