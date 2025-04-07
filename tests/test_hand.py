import pytest

from classes.hand import Hand
from classes.card import Card

def test_hand_init():
    list_of_cards = [Card("Heart", 10), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert hand.cards_list == list_of_cards

    list_of_cards = [Card("Diamond", 12), Card("Club", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.cards_list == list_of_cards

    list_of_cards = [Card("Spade", 2), Card("Club", 3), Card("Heart", 4), Card("Diamond", 5), Card("Spade", 6)]
    hand = Hand(list_of_cards)
    assert hand.cards_list == list_of_cards

def test_invalid_hand_init():
    with pytest.raises(ValueError):
        Hand([Card("Heart", 10)])
    with pytest.raises(ValueError):
        Hand([Card("Heart", 10), Card("Spade", 11), Card("Diamond", 12), Card("Club", 13), Card("Heart", 14), Card("Spade", 15), Card("Diamond", 16)])

def test_hand_str():
    list_of_cards = [Card("Heart", 10), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert str(hand) == "10 of Hearts, Jack of Spades"

    list_of_cards = [Card("Diamond", 12), Card("Club", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert str(hand) == "Queen of Diamonds, King of Clubs, Ace of Hearts"

    list_of_cards = [Card("Spade", 2), Card("Club", 3), Card("Heart", 4), Card("Diamond", 5), Card("Spade", 6)]
    hand = Hand(list_of_cards)
    assert str(hand) == "2 of Spades, 3 of Clubs, 4 of Hearts, 5 of Diamonds, 6 of Spades"

def test_hand_has_royal_flush():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 9)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == False

def test_hand_has_straight_flush():
    # True case
    list_of_cards = [Card("Spade", 5), Card("Spade", 6), Card("Spade", 7), Card("Spade", 8), Card("Spade", 9)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == True

    # False case
    list_of_cards = [Card("Heart", 5), Card("Heart", 6), Card("Heart", 7), Card("Heart", 8), Card("Spade", 9)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == False

def test_hand_has_four_of_a_kind():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == False

def test_hand_has_full_house():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == False

def test_hand_has_flush():
    # True case
    list_of_cards = [Card("Spade", 2), Card("Spade", 4), Card("Spade", 6), Card("Spade", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.hasFlush() == True

    # False case
    list_of_cards = [Card("Heart", 2), Card("Heart", 4), Card("Heart", 6), Card("Heart", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.hasFlush() == False

def test_hand_has_straight():
    # True case
    list_of_cards = [Card("Spade", 5), Card("Heart", 6), Card("Diamond", 7), Card("Club", 8), Card("Spade", 9)]
    hand = Hand(list_of_cards)
    assert hand.hasStraight() == True

    # False case
    list_of_cards = [Card("Heart", 5), Card("Heart", 6), Card("Heart", 7), Card("Heart", 8), Card("Heart", 10)]
    hand = Hand(list_of_cards)
    assert hand.hasStraight() == False

def test_hand_has_three_of_a_kind():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11), Card("Spade", 12)]
    hand = Hand(list_of_cards)
    assert hand.hasThreeOfAKind() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.hasThreeOfAKind() == False

def test_hand_has_two_pair():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 11), Card("Club", 11), Card("Spade", 12)]
    hand = Hand(list_of_cards)
    assert hand.hasTwoPair() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.hasTwoPair() == False

def test_hand_has_one_pair():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 11), Card("Club", 12), Card("Spade", 13)]
    hand = Hand(list_of_cards)
    assert hand.hasOnePair() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.hasOnePair() == False

def test_hand_has_high_card():
    # True case (always true)
    list_of_cards = [Card("Spade", 2), Card("Heart", 4), Card("Diamond", 6), Card("Club", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.hasHighCard() == True