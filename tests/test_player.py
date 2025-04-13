import pytest
from classes.player import Player
from classes.card import Card
from classes.hand import Hand

def test_player_init():
    # Test valid initialization
    player = Player("Alice", 1000)
    assert player.name == "Alice"
    assert player.chips == 1000
    assert player.playing is True
    assert len(player.hand.cards_list) == 0

    # Test initialization with cards
    cards = [Card("Spade", 10), Card("Heart", 11)]
    player = Player("Bob", 500, cards)
    assert player.name == "Bob"
    assert player.chips == 500
    assert len(player.hand.cards_list) == 2
    assert player.hand.cards_list == cards

    # Test initialization with negative money
    with pytest.raises(ValueError, match="Money cannot be negative"):
        Player("Charlie", -100)

def test_player_str():
    # Test string representation
    player = Player("Alice", 1000)
    assert str(player) == "Alice has 1000 chips and the following hand: Empty Hand"

    cards = [Card("Spade", 10), Card("Heart", 11)]
    player = Player("Bob", 500, cards)
    assert str(player) == "Bob has 500 chips and the following hand: 10 of Spades, Jack of Hearts"

def test_player_fold():
    # Test folding
    player = Player("Alice", 1000)
    assert player.playing is True
    player.fold()
    assert player.playing is False

def test_player_check():
    # Test checking
    player = Player("Alice", 1000)
    assert player.check() == "Alice checks."

    # Test checking after folding
    player.fold()
    with pytest.raises(ValueError, match="Alice cannot check because they have folded."):
        player.check()

def test_player_bet():
    # Test valid bet
    player = Player("Alice", 1000)
    assert player.bet(200) == "Alice bets 200 chips."
    assert player.chips == 800

    # Test betting more than available chips
    with pytest.raises(ValueError, match="Alice does not have enough chips to bet 1000."):
        player.bet(1000)

    # Test betting a negative amount
    with pytest.raises(ValueError, match="Bet amount cannot be negative."):
        player.bet(-100)

def test_player_add_card():
    # Test adding cards to the player's hand
    player = Player("Alice", 1000)
    card1 = Card("Spade", 10)
    card2 = Card("Heart", 11)

    player.add_card(card1)
    assert len(player.hand.cards_list) == 1
    assert player.hand.cards_list[-1] == card1

    player.add_card(card2)
    assert len(player.hand.cards_list) == 2
    assert player.hand.cards_list[-1] == card2

def test_player_reset_hand():
    # Test resetting the player's hand
    cards = [Card("Spade", 10), Card("Heart", 11)]
    player = Player("Alice", 1000, cards)
    assert len(player.hand.cards_list) == 2

    player.reset_hand()
    assert len(player.hand.cards_list) == 0

def test_player_is_playing():
    # Test checking if the player is still in the game
    player = Player("Alice", 1000)
    assert player.is_playing() is True

    player.fold()
    assert player.is_playing() is False

def test_player_get_hand_type():
    # Test getting the type of hand the player has
    cards = [Card("Spade", 10), Card("Spade", 11), Card("Spade", 12), Card("Spade", 13), Card("Spade", 14)]
    player = Player("Alice", 1000, cards)
    assert player.get_hand_type() == "Royal Flush"

def test_player_get_chips():
    # Test getting the player's chip count
    player = Player("Alice", 1000)
    assert player.get_chips() == 1000

    player.bet(200)
    assert player.get_chips() == 800