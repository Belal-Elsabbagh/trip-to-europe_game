import game
from game import player
from play_turn_queue import PlayersQueue


def test_start_game():
    game_instance = game.Game(PlayersQueue([
        player.Player("P1"),
        player.Player("P2")
    ]))
    game_instance.start_game()
    assert game_instance is not None
