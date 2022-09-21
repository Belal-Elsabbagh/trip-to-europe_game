"""main game runner"""

from game import Game
from game.player import Player
from game.play_turn_queue import PlayersQueue

if __name__ == '__main__':
    game_instance = Game(PlayersQueue([
        Player("P1"),
        Player("P2"),
        Player("P3"),
        Player("P4")
    ]))
    game_instance.start_game()
