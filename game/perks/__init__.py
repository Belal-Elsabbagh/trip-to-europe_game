from game.player import Player
position_perks = {
    3: 0,
    10: 6,
    14: 18,
    17: 20,
    30: 33,
    38: 42,
    44: 45,
    48: 28
}
disable_players_turn_perks = [12, 16, 27, 41]
play_again_perks = [8, 19, 41]


def all_players_go_back_3(players_list: list[Player]):
    [play.move_player(-3) for play in players_list]
