"""
This module contains constant values of perks.

position perks:
    contains a dictionary of positions that transfer a player to another position.

disable_players_perks:
    contains an array of positions that disable the player's next turn.

play_again_perks:
    contains an array of positions where a player would play again in their turn.
"""

position_perks: dict[int, int] = {
    3: 0,
    10: 6,
    14: 18,
    17: 20,
    30: 33,
    38: 42,
    44: 45,
    48: 28,
}

endgame_positions: dict[int,int] = {
    52: 50,
    53: 49,
    54: 48,
    55: 47,
    56: 46
}

disable_players_perks = [12, 16, 27, 41]
play_again_perks = [8, 19, 41]
