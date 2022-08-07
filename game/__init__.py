from random import randint

from game import perks
from game.player import Player
from game.play_turn_queue import PlayersQueue


class Game:
    __players_queue: PlayersQueue = PlayersQueue([])

    def __init__(self, players_list):
        self.__players_queue = PlayersQueue(players_list)

    @staticmethod
    def __roll_dice() -> int:
        return randint(1, 6)

    def __run_position_perk(self, current_player: Player):
        current_player_position = current_player.get_current_position()
        if current_player_position in perks.position_perks:
            self.__move_player_to(current_player, perks.position_perks[current_player_position])

    def __move_player_to(self, current_player: Player, pos):
        self.__move_occupants(pos)
        current_player.set_position(pos)
        self.__run_position_perk_for_all_players()

    def __move_occupants(self, next_position):
        for i in self.__players_queue.get_all_players():
            occupant_position = i.get_current_position()
            if occupant_position is next_position and occupant_position > 0:
                self.__move_player_to(i, occupant_position - 1)
                return

    def __run_position_perk_for_all_players(self):
        [self.__run_position_perk(i) for i in self.__players_queue.get_all_players()]

    def __run_turn_perk_for_player(self, current_player: Player):
        current_player_position = current_player.get_current_position()
        if current_player_position == 23:
            perks.all_players_go_back_3(self.__players_queue.get_all_players())
            return
        if current_player_position in perks.play_again_perks:
            self.__run_turn(current_player)
            return

    def __run_turn_perks(self):
        [self.__run_turn_perk_for_player(i) for i in self.__players_queue.get_all_players()]

    def __run_turn(self, current_player: Player):
        current_dice_roll = Game.__roll_dice()
        print(f"{current_player.get_name()} rolls {current_dice_roll}")
        next_position = current_player.get_current_position() + current_dice_roll
        self.__move_player_to(current_player, next_position)
        self.__run_position_perk(current_player)
        self.__run_turn_perks()

    def __run_game(self) -> None:
        while max(self.__players_queue.get_list_of_positions()) < 51:
            self.__run_turn(self.__players_queue.get_current_player())
            print(self.__players_queue)
            print("----------------------")
            self.__players_queue.update_turn()

    def start_game(self):
        self.__run_game()
