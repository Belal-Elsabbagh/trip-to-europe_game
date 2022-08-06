class Player:
    __current_player_position: int = 0
    __player_id: str = None

    def __init__(self, player_id: str):
        self.__player_id = player_id

    def __repr__(self):
        return f"{self.__player_id}: {self.__current_player_position}"

    def __str__(self):
        return f"{self.__player_id}: {self.__current_player_position}"

    def get_name(self):
        return self.__player_id

    def set_position(self, value: int):
        self.__current_player_position = value

    def get_current_position(self) -> int:
        return self.__current_player_position

    def move_player(self, value):
        self.__current_player_position += value
