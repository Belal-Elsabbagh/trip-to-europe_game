import game
from game import player

if __name__ == '__main__':
    game_instance = game.Game([
        player.Player("Belal"),
        player.Player("Yaseen")
    ])
    game_instance.run_game()
