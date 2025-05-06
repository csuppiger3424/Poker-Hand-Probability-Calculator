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

def test_has_royal_flush():
    # True case with exactly 5 cards
    list_of_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == True

    # True case with more than 5 cards
    list_of_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14), Card("Heart", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == True

    # False case with less than 5 cards
    list_of_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == False

    # False case with more than 5 cards but no royal flush
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 9), Card("Spade", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_royal_flush() == False

def test_has_straight_flush():
    # True case with exactly 5 cards
    list_of_cards = [Card("Spade", 5), Card("Spade", 6), Card("Spade", 7), Card("Spade", 8), Card("Spade", 9)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == True

    # True case with more than 5 cards
    list_of_cards = [Card("Spade", 5), Card("Spade", 6), Card("Spade", 7), Card("Spade", 8), Card("Spade", 9), Card("Heart", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == True

    # False case with less than 5 cards
    list_of_cards = [Card("Spade", 5), Card("Spade", 6), Card("Spade", 7), Card("Spade", 8)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == False

    # False case with more than 5 cards but no straight flush
    list_of_cards = [Card("Heart", 5), Card("Heart", 6), Card("Heart", 7), Card("Heart", 8), Card("Spade", 9), Card("Club", 2), Card("Diamond", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_straight_flush() == False

def test_has_four_of_a_kind():
    # True case with exactly 5 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == True

    # True case with more than 5 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11), Card("Heart", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == True

    # False case with less than 4 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == False

    # False case with more than 5 cards but no four of a kind
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14), Card("Spade", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_four_of_a_kind() == False

def test_has_full_house():
    # True case with exactly 5 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == True

    # True case with more than 5 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11), Card("Spade", 11), Card("Heart", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == True

    # False case with less than 5 cards
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == False

    # False case with more than 5 cards but no full house
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14), Card("Spade", 2), Card("Club", 3)]
    hand = Hand(list_of_cards)
    assert hand.has_full_house() == False

def test_has_flush():
    # True case
    list_of_cards = [Card("Spade", 2), Card("Spade", 4), Card("Spade", 6), Card("Spade", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.has_flush() == True

    # False case
    list_of_cards = [Card("Heart", 2), Card("Heart", 4), Card("Heart", 6), Card("Heart", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.has_flush() == False

def test_has_straight():
    # True case
    list_of_cards = [Card("Spade", 5), Card("Heart", 6), Card("Diamond", 7), Card("Club", 8), Card("Spade", 9)]
    hand = Hand(list_of_cards)
    assert hand.has_straight() == True

    # False case
    list_of_cards = [Card("Heart", 5), Card("Heart", 6), Card("Heart", 7), Card("Heart", 8), Card("Heart", 10)]
    hand = Hand(list_of_cards)
    assert hand.has_straight() == False

def test_has_three_of_a_kind():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 11), Card("Spade", 12)]
    hand = Hand(list_of_cards)
    assert hand.has_three_of_a_kind() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_three_of_a_kind() == False

def test_has_two_pair():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 11), Card("Club", 11), Card("Spade", 12)]
    hand = Hand(list_of_cards)
    assert hand.has_two_pair() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_two_pair() == False

def test_has_one_pair():
    # True case
    list_of_cards = [Card("Spade", 10), Card("Heart", 10), Card("Diamond", 11), Card("Club", 12), Card("Spade", 13)]
    hand = Hand(list_of_cards)
    assert hand.has_one_pair() == True

    # False case
    list_of_cards = [Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13), Card("Heart", 14)]
    hand = Hand(list_of_cards)
    assert hand.has_one_pair() == False

def test_has_high_card():
    # True case (always true)
    list_of_cards = [Card("Spade", 2), Card("Heart", 4), Card("Diamond", 6), Card("Club", 8), Card("Spade", 10)]
    hand = Hand(list_of_cards)
    assert hand.has_high_card() == True

def test_get_hand_type():
    # Test Royal Flush
    list_of_cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Royal Flush"

    # Test Straight Flush
    list_of_cards = [Card("Heart", 5), Card("Heart", 6), Card("Heart", 7), Card("Heart", 8), Card("Heart", 9)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Straight Flush"

    # Test Four of a Kind
    list_of_cards = [Card("Club", 10), Card("Heart", 10), Card("Diamond", 10), Card("Spade", 10), Card("Heart", 2)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Four of a Kind"

    # Test Full House
    list_of_cards = [Card("Spade", 3), Card("Heart", 3), Card("Diamond", 3), Card("Club", 7), Card("Heart", 7)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Full House"

    # Test Flush
    list_of_cards = [Card("Diamond", 2), Card("Diamond", 4), Card("Diamond", 6), Card("Diamond", 8), Card("Diamond", 10)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Flush"

    # Test Straight
    list_of_cards = [Card("Club", 5), Card("Diamond", 6), Card("Heart", 7), Card("Spade", 8), Card("Club", 9)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Straight"

    # Test Three of a Kind
    list_of_cards = [Card("Heart", 4), Card("Diamond", 4), Card("Spade", 4), Card("Club", 9), Card("Heart", 10)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Three of a Kind"

    # Test Two Pair
    list_of_cards = [Card("Spade", 6), Card("Heart", 6), Card("Diamond", 9), Card("Club", 9), Card("Heart", 12)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "Two Pair"

    # Test One Pair
    list_of_cards = [Card("Club", 8), Card("Diamond", 8), Card("Heart", 3), Card("Spade", 5), Card("Club", 10)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "One Pair"

    # Test High Card
    list_of_cards = [Card("Heart", 2), Card("Diamond", 4), Card("Spade", 6), Card("Club", 8), Card("Heart", 11)]
    hand = Hand(list_of_cards)
    assert hand.get_hand_type() == "High Card"

def test_compare_high_card():
    # Hand 1 wins
    hand1 = Hand([Card("Spade", 14), Card("Heart", 13), Card("Diamond", 12)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 9), Card("Diamond", 8)])
    assert hand1.compare_high_card(hand2) == 1

    # Hand 2 wins
    hand1 = Hand([Card("Spade", 10), Card("Heart", 9), Card("Diamond", 8)])
    hand2 = Hand([Card("Spade", 14), Card("Heart", 13), Card("Diamond", 12)])
    assert hand1.compare_high_card(hand2) == -1

    # Tie
    hand1 = Hand([Card("Spade", 14), Card("Heart", 13), Card("Diamond", 12)])
    hand2 = Hand([Card("Club", 14), Card("Diamond", 13), Card("Heart", 12)])
    assert hand1.compare_high_card(hand2) == 0

def test_compare_one_pair():
    # Hand 1 wins with higher pair
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 8)])
    assert hand1.compare_one_pair(hand2) == 1

    # Hand 2 wins with higher pair
    hand1 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 8)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8)])
    assert hand1.compare_one_pair(hand2) == -1

    # Tie, fallback to high card
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8)])
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 7)])
    assert hand1.compare_one_pair(hand2) == 1

def test_compare_two_pair():
    # Hand 1 wins with higher top pair
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8), Card("Club", 8)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 7), Card("Club", 7)])
    assert hand1.compare_two_pair(hand2) == 1

    # Hand 2 wins with higher top pair
    hand1 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 7), Card("Club", 7)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8), Card("Club", 8)])
    assert hand1.compare_two_pair(hand2) == -1

    # Tie, fallback to high card
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 8), Card("Club", 8)])
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 8), Card("Spade", 8)])
    assert hand1.compare_two_pair(hand2) == 0

def test_compare_three_of_a_kind():
    # Hand 1 wins with higher three of a kind
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9)])
    assert hand1.compare_three_of_a_kind(hand2) == 1

    # Hand 2 wins with higher three of a kind
    hand1 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10)])
    assert hand1.compare_three_of_a_kind(hand2) == -1

    # Tie, fallback to high card
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8)])
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 10), Card("Spade", 7)])
    assert hand1.compare_three_of_a_kind(hand2) == 1

def test_compare_straight():
    # Hand 1 wins with higher straight
    hand1 = Hand([Card("Spade", 10), Card("Heart", 9), Card("Diamond", 8), Card("Club", 7), Card("Spade", 6)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 8), Card("Diamond", 7), Card("Club", 6), Card("Spade", 5)])
    assert hand1.compare_straight(hand2) == 1

    # Hand 2 wins with higher straight
    hand1 = Hand([Card("Spade", 9), Card("Heart", 8), Card("Diamond", 7), Card("Club", 6), Card("Spade", 5)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 9), Card("Diamond", 8), Card("Club", 7), Card("Spade", 6)])
    assert hand1.compare_straight(hand2) == -1

    # Tie with Ace as low
    hand1 = Hand([Card("Spade", 5), Card("Heart", 4), Card("Diamond", 3), Card("Club", 2), Card("Spade", 14)])  # A-2-3-4-5
    hand2 = Hand([Card("Spade", 5), Card("Heart", 4), Card("Diamond", 3), Card("Club", 2), Card("Spade", 14)])  # A-2-3-4-5
    assert hand1.compare_straight(hand2) == 0

    # High straight (10-J-Q-K-A) vs Low straight (A-2-3-4-5)
    hand1 = Hand([Card("Spade", 10), Card("Heart", 11), Card("Diamond", 12), Card("Club", 13), Card("Spade", 14)])  # High straight
    hand2 = Hand([Card("Spade", 14), Card("Heart", 2), Card("Diamond", 3), Card("Club", 4), Card("Spade", 5)])  # Low straight
    assert hand1.compare_straight(hand2) == 1  # Hand 1 wins

    # Low straight (A-2-3-4-5) vs High straight (10-J-Q-K-A)
    hand1 = Hand([Card("Spade", 14), Card("Heart", 2), Card("Diamond", 3), Card("Club", 4), Card("Spade", 5)])  # Low straight
    hand2 = Hand([Card("Spade", 10), Card("Heart", 11), Card("Diamond", 12), Card("Club", 13), Card("Spade", 14)])  # High straight
    assert hand1.compare_straight(hand2) == -1  # Hand 2 wins

def test_compare_flush():
    # Hand 1 wins with higher flush
    hand1 = Hand([Card("Spade", 14), Card("Spade", 13), Card("Spade", 12), Card("Spade", 11), Card("Spade", 10)])
    hand2 = Hand([Card("Heart", 9), Card("Heart", 8), Card("Heart", 7), Card("Heart", 6), Card("Heart", 5)])
    assert hand1.compare_flush(hand2) == 1

    # Hand 2 wins with higher flush
    hand1 = Hand([Card("Spade", 9), Card("Spade", 8), Card("Spade", 7), Card("Spade", 6), Card("Spade", 5)])
    hand2 = Hand([Card("Heart", 14), Card("Heart", 13), Card("Heart", 12), Card("Heart", 11), Card("Heart", 10)])
    assert hand1.compare_flush(hand2) == -1

    # Tie
    hand1 = Hand([Card("Spade", 14), Card("Spade", 13), Card("Spade", 12), Card("Spade", 11), Card("Spade", 10)])
    hand2 = Hand([Card("Heart", 14), Card("Heart", 13), Card("Heart", 12), Card("Heart", 11), Card("Heart", 10)])
    assert hand1.compare_flush(hand2) == 0

def test_compare_full_house():
    # Hand 1 wins with higher three of a kind
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8), Card("Spade", 8)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9), Card("Club", 7), Card("Spade", 7)])
    assert hand1.compare_full_house(hand2) == 1

    # Hand 2 wins with higher three of a kind
    hand1 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9), Card("Club", 7), Card("Spade", 7)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8), Card("Spade", 8)])
    assert hand1.compare_full_house(hand2) == -1

    # Tie
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8), Card("Spade", 8)])
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 10), Card("Spade", 8), Card("Heart", 8)])
    assert hand1.compare_full_house(hand2) == 0

def test_compare_four_of_a_kind():
    # Hand 1 wins with higher four of a kind
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11)])
    hand2 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9), Card("Club", 9), Card("Spade", 8)])
    assert hand1.compare_four_of_a_kind(hand2) == 1

    # Hand 2 wins with higher four of a kind
    hand1 = Hand([Card("Spade", 9), Card("Heart", 9), Card("Diamond", 9), Card("Club", 9), Card("Spade", 8)])
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11)])
    assert hand1.compare_four_of_a_kind(hand2) == -1

    # Tie, fallback to high card
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 11)])
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 10), Card("Spade", 10), Card("Heart", 9)])
    assert hand1.compare_four_of_a_kind(hand2) == 1

def test_compare_with():
    # Royal Flush vs Straight Flush
    hand1 = Hand([Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)])  # Royal Flush
    hand2 = Hand([Card("Heart", 9), Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13)])  # Straight Flush
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Straight Flush vs Four of a Kind
    hand1 = Hand([Card("Heart", 9), Card("Heart", 10), Card("Heart", 11), Card("Heart", 12), Card("Heart", 13)])  # Straight Flush
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 2)])  # Four of a Kind
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Four of a Kind vs Full House
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 10), Card("Spade", 2)])  # Four of a Kind
    hand2 = Hand([Card("Heart", 9), Card("Diamond", 9), Card("Spade", 9), Card("Club", 8), Card("Heart", 8)])  # Full House
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Full House vs Flush
    hand1 = Hand([Card("Heart", 9), Card("Diamond", 9), Card("Spade", 9), Card("Club", 8), Card("Heart", 8)])  # Full House
    hand2 = Hand([Card("Spade", 2), Card("Spade", 4), Card("Spade", 6), Card("Spade", 8), Card("Spade", 10)])  # Flush
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Flush vs Straight
    hand1 = Hand([Card("Spade", 2), Card("Spade", 4), Card("Spade", 6), Card("Spade", 8), Card("Spade", 10)])  # Flush
    hand2 = Hand([Card("Heart", 5), Card("Diamond", 6), Card("Club", 7), Card("Spade", 8), Card("Heart", 9)])  # Straight
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Straight vs Three of a Kind
    hand1 = Hand([Card("Heart", 5), Card("Diamond", 6), Card("Club", 7), Card("Spade", 8), Card("Heart", 9)])  # Straight
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8), Card("Spade", 7)])  # Three of a Kind
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Three of a Kind vs Two Pair
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 10), Card("Club", 8), Card("Spade", 7)])  # Three of a Kind
    hand2 = Hand([Card("Heart", 9), Card("Diamond", 9), Card("Spade", 8), Card("Club", 8), Card("Heart", 7)])  # Two Pair
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Two Pair vs One Pair
    hand1 = Hand([Card("Heart", 9), Card("Diamond", 9), Card("Spade", 8), Card("Club", 8), Card("Heart", 7)])  # Two Pair
    hand2 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 7), Card("Club", 6), Card("Spade", 5)])  # One Pair
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # One Pair vs High Card
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 7), Card("Club", 6), Card("Spade", 5)])  # One Pair
    hand2 = Hand([Card("Heart", 14), Card("Diamond", 13), Card("Spade", 12), Card("Club", 11), Card("Heart", 9)])  # High Card
    assert hand1.compare_with(hand2) == 1  # Hand 1 wins

    # Tie with High Card
    hand1 = Hand([Card("Heart", 14), Card("Diamond", 13), Card("Spade", 12), Card("Club", 11), Card("Heart", 9)])  # High Card
    hand2 = Hand([Card("Spade", 14), Card("Heart", 13), Card("Diamond", 12), Card("Club", 11), Card("Spade", 9)])  # High Card
    assert hand1.compare_with(hand2) == 0  # Tie

    # Tie with One Pair
    hand1 = Hand([Card("Spade", 10), Card("Heart", 10), Card("Diamond", 7), Card("Club", 6), Card("Spade", 5)])  # One Pair
    hand2 = Hand([Card("Club", 10), Card("Diamond", 10), Card("Heart", 7), Card("Spade", 6), Card("Heart", 5)])  # One Pair
    assert hand1.compare_with(hand2) == 0  # Tie

    # Straight with Ace as low vs Straight with Ace as high
    hand1 = Hand([Card("Spade", 14), Card("Heart", 2), Card("Diamond", 3), Card("Club", 4), Card("Spade", 5)])  # A-2-3-4-5
    hand2 = Hand([Card("Spade", 10), Card("Heart", 11), Card("Diamond", 12), Card("Club", 13), Card("Spade", 14)])  # 10-J-Q-K-A
    assert hand1.compare_with(hand2) == -1  # Hand 2 wins

    hand1 = Hand([Card("Heart", 5), Card("Heart", 6), Card("Diamond", 5), Card("Diamond", 6), Card("Diamond", 10), Card("Club", 5), Card("Club", 6)])
    hand2 = Hand([Card("Heart", 6), Card("Spade", 4), Card("Diamond", 5), Card("Diamond", 6), Card("Diamond", 10), Card("Club", 5), Card("Club", 6)])
    assert hand1.compare_with(hand2) == 0  # Hand 2 wins

def test_add_card():
    # Add a card to a hand with fewer than 7 cards
    list_of_cards = [Card("Heart", 10), Card("Spade", 11)]
    hand = Hand(list_of_cards)
    new_card = Card("Diamond", 12)
    hand.add_card(new_card)
    assert len(hand.cards_list) == 3
    assert hand.cards_list[-1] == new_card

    # Add multiple cards to a hand until it reaches 7 cards
    hand.add_card(Card("Club", 13))
    hand.add_card(Card("Heart", 14))
    hand.add_card(Card("Spade", 2))
    hand.add_card(Card("Diamond", 3))
    assert len(hand.cards_list) == 7

    # Attempt to add a card to a hand with 7 cards
    with pytest.raises(ValueError, match="A hand cannot contain more than 7 cards"):
        hand.add_card(Card("Club", 4))
