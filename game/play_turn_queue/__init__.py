import copy

from game.player import Player


class PlayersQueue:
    __turn_index: int = 0
    __skip_list: list[int] = []
    __queue: list[Player] = []

    def __init__(self, players_list):
        self.__queue = copy.deepcopy(players_list)

    def __str__(self):
        return f"Queue: {self.__queue}"

    def get_current_player(self):
        return self.__queue[self.__turn_index % len(self.__queue)]

    def get_all_players(self):
        return self.__queue

    def get_list_of_positions(self):
        return [i.get_current_position() for i in self.__queue]

    def update_turn(self):
        self.__turn_index += 1

