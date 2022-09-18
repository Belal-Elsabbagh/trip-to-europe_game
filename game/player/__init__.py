"""The player package"""


class Player:
    """
    The player class

    Attributes:
        __position (int): The player's position.
        __id (str): The player's id
    """
    __position: int = 0

    def __init__(self, player_id: str):
        self.__id = player_id

    def __repr__(self):
        return f"{self.__id}: {self.__position}"

    def __str__(self):
        return f"{self.__id}: {self.__position}"

    def get_id(self) -> str:
        """
        Gets player id

        Returns:
            str: The player's id
        """
        return self.__id

    def set_position(self, value: int):
        """
        Sets the player's position
        Args:
            value (int): The player's position.

        Returns:
            None: no return
        """
        self.__position = value

    def get_current_position(self) -> int:
        return self.__position

    def move_player(self, value):
        self.__position += value
