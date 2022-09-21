"""
This module includes the class that runs the game.
"""

from random import randint

from game import perks
from game.play_turn_queue import PlayersQueue
from game.player import Player


class Game:
    """
    The game runner.

    Attributes:
        __players_queue (PlayersQueue): The player queue to run.
        game_log (list): The game sequence.
    """

    def __init__(self, players_list: PlayersQueue) -> None:
        """
        Args:
            players_list (PlayersQueue): The queue that stores the players and controls their turns.
        """
        self.game_log = []
        self.__players_queue = PlayersQueue(players_list)

    def __log_turn(self, roll):
        f = open("log.txt", "a")
        f.write(f"{roll} - {self.__players_queue.__str__()}\n")
        f.close()

    @staticmethod
    def __roll_dice() -> int:
        """
        Simulates a die roll.

        Returns:
            int: A random number between 1 and 6.
        """

        return randint(1, 6)

    def __run_position_perk(self, perked_player: Player) -> None:
        """
        Runs position perk for a given player
        Args:
            perked_player (Player): The current player to run the position perk on.

        Returns:
            None: no return
        """
        current_player_position = perked_player.get_position()
        if current_player_position == 23:
            self.__all_players_go_back_3(perked_player)
            return
        if current_player_position in perks.position_perks:
            self.__move_player_to(perked_player, perks.position_perks[current_player_position])

    def __move_player_to(self, current_player: Player, pos):
        if pos in perks.endgame_positions:
            pos = perks.endgame_positions[pos]
        for i in self.__players_queue.get_all_players():
            occupant_position = i.get_position()
            if occupant_position is pos and occupant_position > 0:
                self.__move_player_to(i, occupant_position - 1)
        current_player.set_position(pos)
        if pos in perks.disable_players_perks:
            self.__players_queue.activate_player(current_player)

    def __run_position_perk_for_all_players(self):
        """
        Methods:
            __run_position_perk
        Returns:
            None: no return
        """
        [self.__run_position_perk(i) for i in self.__players_queue.get_all_players()]

    def __all_players_go_back_3(self, except_player: Player):
        original_position = except_player.get_position()
        for i in self.__players_queue.get_all_players():
            player_position = i.get_position()
            if player_position < 3:
                self.__move_player_to(i, 0)
                continue
            self.__move_player_to(i, player_position - 3)
        self.__move_player_to(except_player, original_position)

    def __run_turn_perk_for_player(self, current_player: Player):
        player_position = current_player.get_position()
        if player_position in perks.play_again_perks:
            self.__run_turn(current_player)
            return
        if self.__players_queue.get_player_status(current_player) is False:
            self.__players_queue.activate_player(current_player)
            return
        if player_position in perks.disable_players_perks:
            self.__players_queue.disable_player_next_turn(current_player)

    def __run_turn_perks(self):
        [self.__run_turn_perk_for_player(i) for i in self.__players_queue.get_all_players()]

    def __run_turn(self, current_player: Player) -> None:
        """
        Runs turn for the given player.

        Args:
            current_player (Player): The player given to run the turn for.

        Returns:
            None: no return
        """

        current_dice_roll = Game.__roll_dice()
        if current_player.get_position() == 21 and current_dice_roll not in [1, 6]:
            return
        next_position = current_player.get_position() + current_dice_roll
        self.__move_player_to(current_player, next_position)
        self.__run_position_perk_for_all_players()
        self.__run_turn_perks()
        self.__log_turn(f"{current_player.get_id()} rolls {current_dice_roll}")

    def __run_game(self) -> None:
        """
        Runs and updates turns. Prints the game.

        Returns:
            None: no return
        """
        while max(self.__players_queue.get_list_of_positions()) != 51:
            self.__run_turn(self.__players_queue.get_current_player())
            self.__players_queue.update_turn()

    def start_game(self) -> None:
        """
        Starts running the game.

        Returns:
            None: no return
        """
        try:
            self.__run_game()
        except ValueError as e:
            print(e)
