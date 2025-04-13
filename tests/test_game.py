import pytest
from classes.game import Game
from classes.table import Table
from classes.player import Player
from classes.card import Card
from classes.deck import Deck

def test_game_initialization():
    """
    Test initializing the game with a table and players.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])
    game = Game(table)

    assert game.table == table
    assert len(game.table.players) == 2
    assert game.table.players[0].name == "Alice"
    assert game.table.players[1].name == "Bob"
    assert len(game.table.deck.cards_list) == 52  # Full deck of cards

def test_game_play_game():
    """
    Test playing a full game.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])
    game = Game(table)

    # Play the game
    game.play_game()

    # Ensure cards are dealt to players
    assert len(player1.hand.cards_list) == 7  # 2 player cards + 5 community cards
    assert len(player2.hand.cards_list) == 7  # 2 player cards + 5 community cards

    # Ensure community cards are dealt
    assert len(game.table.cards) == 5  # 3 flop + 1 turn + 1 river

    # Ensure the deck has the correct number of remaining cards
    assert len(game.table.deck.cards_list) == 40  # 52 - 2*2 (player cards) - 5 (community cards) - 3 (burned cards)

def test_game_determine_winner():
    """
    Test determining the winner with a rigged deck for multiple players.
    """
    # Rigged cards for players
    players = [
        {0: [Card("Spade", 10), Card("Spade", 11)]},  # Player 1's rigged cards (Royal Flush)
        {1: [Card("Heart", 9), Card("Heart", 10)]},  # Player 2's rigged cards (Straight Flush)
        {2: [Card("Diamond", 2), Card("Diamond", 3)]}  # Player 3's rigged cards (Low cards)
    ]

    # Rigged community cards
    table_cards = [
        Card("Spade", 12),  # Queen of Spades
        Card("Spade", 13),  # King of Spades
        Card("Spade", 14)   # Ace of Spades
    ]

    # Create the rigged deck
    deck = Deck(players=players, table_cards=table_cards)

    # Create players
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    player3 = Player("Charlie", 1000)

    # Create a table with the rigged deck
    table = Table(deck, [player1, player2, player3])

    # Create and play the game
    game = Game(table)
    game.play_game()

    # Determine the winner
    winner = game.determine_winner()
    assert winner.name == "Alice"  # Alice should win with a Royal Flush

def test_game_display_player_hands(capsys):
    """
    Test displaying player hands.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])
    game = Game(table)

    table.deal()
    game.display_player_hands()

    captured = capsys.readouterr()
    assert "Alice's hand:" in captured.out
    assert "Bob's hand:" in captured.out

def test_game_display_community_cards(capsys):
    """
    Test displaying community cards.
    """
    deck = Deck()
    player1 = Player("Alice", 1000)
    player2 = Player("Bob", 1000)
    table = Table(deck, [player1, player2])
    game = Game(table)

    table.flop()
    game.display_community_cards()

    captured = capsys.readouterr()
    assert "Community cards:" in captured.out
    assert len(table.cards) == 3  # Flop should have 3 cards