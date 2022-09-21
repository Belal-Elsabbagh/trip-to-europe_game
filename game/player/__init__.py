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

        Raises:
            ValueError: if the player's new position value is invalid

        Returns:
            None: no return
        """
        if value < 0 or value > 51:
            raise ValueError(f"Only values between 0 and 51 are allowed. Value sent: {value}")
        self.__position = value

    def get_position(self) -> int:
        """

        Returns:
            int: The player's current position.
        """
        return self.__position

    def move_player(self, value):
        """

        Args:
            value (int): The value to increment/decrement the player's position.

        Returns:
            None: no return
        """
        self.set_position(self.get_position() + value)
