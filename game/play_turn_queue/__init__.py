import copy

from game.player import Player


class PlayersQueue:
    __turn_count: int = 0
    __skip_list: list[bool] = []
    __queue: list[Player] = []

    def __init__(self, players_list):
        self.__queue = copy.deepcopy(players_list)
        self.__skip_list = [True for i in range(len(players_list))]

    def __str__(self):
        return f"Queue: {self.__queue}"

    def __repr__(self):
        return f"Queue: {self.__queue}"

    def __get_player_turn_index(self):
        return self.__turn_count % len(self.__queue)

    def __get_player_index_in_queue(self, player_object):
        return self.__queue.index(player_object)

    def disable_player_next_turn(self, player_object):
        player_index = self.__get_player_index_in_queue(player_object)
        self.__skip_list[player_index] = False

    def get_current_player(self):
        return self.__queue[self.__get_player_turn_index()]

    def get_player_status(self, player_object):
        player_index = self.__get_player_index_in_queue(player_object)
        return self.__skip_list[player_index]

    def get_all_players(self):
        return self.__queue

    def get_list_of_positions(self):
        return [i.get_position() for i in self.__queue]

    def update_turn(self):
        while True:
            self.__turn_count += 1
            if self.__skip_list[self.__get_player_turn_index()] is False:
                continue
            return

    def activate_player(self, player_object):
        player_index = self.__get_player_index_in_queue(player_object)
        self.__skip_list[player_index] = True
