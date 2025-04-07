from classes.player import Player

import pytest

# def test_player_init():
#     from classes.card import Card

#     player = Player("Alice", 1000)
#     assert player.name == "Alice"
#     assert player.chips == 1000
#     assert player.cards_list == []
#     assert player.folded == False

# def test_player_str():
#     player = Player("Bob", 1500)
#     assert str(player) == "Bob has 1500 chips"

# def test_invalid_player_init():
#     with pytest.raises(ValueError):
#         Player("Charlie", -100)  # Invalid initial chips
#     with pytest.raises(ValueError):

# def test_player_fold():

#     player = Player("Bob")
#     assert player.folded == False
#     player.fold()
#     assert player.folded == True

# def test_player_unfold():

#     player = Player("Charlie")
#     player.fold()
#     assert player.folded == True
#     player.unfold()
#     assert player.folded == False

# def test_player_bet():
#     player = Player("David")
#     assert player.chips == 1000
#     player.bet(100)
#     assert player.chips == 900
#     player.bet(200)
#     assert player.chips == 700
#     player.bet(700) 

# def test_player_bet_over_chips():
#     player = Player("Eve")
#     assert player.chips == 1000
#     with pytest.raises(ValueError):
#         player.bet(1100)  # Trying to bet more than available chips 
