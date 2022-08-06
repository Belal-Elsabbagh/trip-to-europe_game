import game
from game.player import Player

if __name__ == '__main__':
    game_instance = game.Game([
        Player("P1"),
        Player("P2"),
        Player("P3"),
        Player("P4")
    ])
    game_instance.start_game()
