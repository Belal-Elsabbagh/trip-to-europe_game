import game
from game import player

if __name__ == '__main__':
    game_instance = game.Game([
        player.Player("P1"),
        player.Player("P2")
    ])
    game_instance.start_game()
