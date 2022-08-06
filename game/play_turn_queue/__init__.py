from game import player


class PlayersQueue:
    __players_list: list[player.Player] = []
    current_player_index = 0

    def __init__(self, players_list):
        self.__players_list = players_list

    def __str__(self):
        return f"{self.__players_list}"

    def get_current_player(self):
        return self.__players_list[self.current_player_index]

    def get_all_players(self):
        return self.__players_list

    def get_list_of_positions(self):
        return [i.get_current_position() for i in self.__players_list]

    def update_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.__players_list)
