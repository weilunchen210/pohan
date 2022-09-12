"""
Class where the battle between pokemons commence and a winner is selected
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 30.04.2022
"""
from pokemon_base import PokemonBase
from poke_team import PokeTeam
from sorted_list import ListItem
from array_sorted_list import ArraySortedList
from pokemon import Charmander, Bulbasaur, Squirtle
from MissingNo import MissingNo
from typing import TypeVar
T = TypeVar('T', Charmander, Bulbasaur, Squirtle, MissingNo, PokeTeam, PokemonBase, ListItem)


class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        """
        Constructor for battle class
        :param trainer_one_name: A string of the trainer's name
        :param trainer_two_name: A string of the trainer's name
        :raises TypeError: If both inputs aren't string
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        # Checks if both inputs are string or not
        if type(trainer_one_name) != str:
            raise TypeError("Trainer 1's name must be a string")
        elif type(trainer_two_name) != str:
            raise TypeError("Trainer 2's name must be a string")
        else:
            self.team1 = PokeTeam(trainer_one_name)  # Creates a Pokemon Team object for Trainer One
            self.team2 = PokeTeam(trainer_two_name)  # Creates a Pokemon Team object for Trainer Two
            self.battle_mode = None
            self.pokemon1 = None
            self.pokemon2 = None
            self.criterion_team1 = None
            self.criterion_team2 = None
            self.missingno1 = None
            self.missingno2 = None

    def set_mode_battle(self) -> str:
        """
        Sets the battle mode to 0 and have 2 pokemon teams battle
        :return: A string of the winner's name
        :complexity: Best is O(min(len(self.team1.team), len(self.team2.team)) as it will return a winner after
                     1 team is empty.
                     Worst is O(N^2) where the user input is not valid in the first try when choosing team for the
                     trainers
        """
        self.battle_mode = 0  # Sets battle mode to 0
        return self.battling()  # Start the battle between the 2 trainers

    def rotating_mode_battle(self) -> str:
        """
        Sets the battle mode to 1 and have 2 pokemon teams battle
        :return: A string of the winner's name
        :complexity: Best is O(min(len(self.team1.team), len(self.team2.team)) as it will return a winner after
                     1 team is empty.
                     Worst is O(N^2) where the user input is not valid in the first try when choosing team for the
                     trainers
        """
        self.battle_mode = 1  # Sets battle mode to 1
        return self.battling()  # Start the battle between the 2 trainers

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
        Sets the battle mode to 2 and have 2 pokemon teams battle
        :param criterion_team1: A string of the criterion chosen for team 1
        :param criterion_team2: A string of the criterion chosen for team 2
        :return: A string of the winner's name
        :raises TypeError: If both teams' criterions aren't a string
        :raises ValueError: If one/ both of the teams' criterion(s) isn't/ aren't lvl, hp, atk, def or spd
        :complexity: Best is O(min(len(self.team1.team), len(self.team2.team)). If one of the teams has only 1 pokemon
                     and it faints within the first round. The winner will be output as the other team
                     Worst is O((len(self.team1.team) + len(self.team2.team)) * N^2), where N is len(self).
                     If both teams have full team of 6, it will take (len(self.team1.team) + len(self.team2.team))
                     times for the while loop to output a winner. Within the while loop, when pokemons are added back into their
                     team, it will traverse the list placing it into array sorted list.
        """
        # Checks if both inputs are string or not
        if type(criterion_team1) != str:
            raise TypeError("Team 1's criterion must be a string")
        if type(criterion_team2) != str:
            raise TypeError("Team 2's criterion must be a string")
        else:
            self.battle_mode = 2  # Sets battle mode to 1
            criterion_list = ["lvl", "hp", "atk", "def", "spd"]

            # Checks whether input criterion for both teams are one of those in the list
            if criterion_team1 in criterion_list and criterion_team2 in criterion_list:
                self.criterion_team1 = criterion_team1  # If yes assign both to the object's variables
                self.criterion_team2 = criterion_team2
                return self.battling()  # Start the battle between the 2 trainers
            else:
                raise ValueError("Input criterion(s) is/are invalid. Choose lvl, hp, atk, def or spd")

    def battling(self) -> str:
        """
        Allows user to input pokemon teams for both trainers and battle it out
        :return: A string of the winner's name
        :raises ValueError: If battle mode set wasn't 0, 1 or 2,
                            or if winner's name is not one of the trainers
        :complexity: Best is O(min(len(self.team1.team), len(self.team2.team)). When 1 team has all its pokemon fainted,
                     it returns the winner which is the other team. So it loops until 1 team is empty.
                     Worst is O((len(self.team1.team) + len(self.team2.team)) * N^2), where N is len(self) and
                     if it's an array sorted list. If both teams have full team of 6, it will take (len(self.team1.team) + len(self.team2.team))
                     times for the while loop to output a winner. Within the while loop, when pokemons are added back into their
                     team, it will traverse the list placing it into array sorted list.
        """
        print("For", self.team1.trainer)
        # Allow user input to choose and assign the team for Trainer One
        self.team1.choose_team(self.battle_mode, self.criterion_team1)
        print("For", self.team2.trainer)
        # Allow user input to choose and assign the team for Trainer Two
        self.team2.choose_team(self.battle_mode, self.criterion_team2)

        # If one of the team is empty, loop out and proceed to the next code block.
        # Otherwise continue looping until one team is empty
        while not(self.team1.team.is_empty() or self.team2.team.is_empty()):
            round_finished = False
            # If round_finished is set to True, it goes back and checks whether if one of the team is empty to prepare
            # the battle between 2 other pokemons
            # If it's False, it means neither pokemons battling has fainted. So both return back to their respective
            # teams and allow the next battle to commence
            while not round_finished:
                self.pokemon1 = self.team1.get_pokemon(self.battle_mode)  # Choose the pokemon ready for battle from Trainer One's team
                self.pokemon2 = self.team2.get_pokemon(self.battle_mode)  # Choose the pokemon ready for battle from Trainer Two's team

                # Checks which battle mode to determine how the battling style would occur
                if self.battle_mode == 0:
                    round_finished = self.compare_speed(self.pokemon1, self.pokemon2)  # Enters battle between the 2 chosen pokemons
                elif self.battle_mode == 1:
                    round_finished = self.compare_speed(self.pokemon1, self.pokemon2)  # Enters battle between the 2 chosen pokemons
                elif self.battle_mode == 2:
                    cond1 = isinstance(self.pokemon1.value, MissingNo) and not (self.pokemon1.value.has_battled() or self.team1.team.is_empty())
                    cond2 = isinstance(self.pokemon2.value, MissingNo) and not (self.pokemon2.value.has_battled() or self.team2.team.is_empty())
                    # Checks whether is chosen pokemon from Trainer One's team a MissingNo that hasn't battled
                    # If it has battled, in an empty team or is not a MissingNo, goto the else
                    if cond1:
                        # If it is, place the MissingNo into another Array Sorted List and return the other pokemon
                        # back into Trainer Two's team
                        self.missingno1 = self.get_missingno(self.pokemon1.value, self.team1)
                        self.returning(self.pokemon2.value, 2)
                    # Checks whether is chosen pokemon from Trainer Two's team a MissingNo that hasn't battled
                    # If it has battled, in an empty team or is not a MissingNo, goto the else
                    elif cond2:
                        # If it is, place the MissingNo into another Array Sorted List and return the other pokemon
                        # back into Trainer One's team
                        self.missingno2 = self.get_missingno(self.pokemon2.value, self.team2)
                        self.returning(self.pokemon1.value, 1)
                    # Checks whether both chosen pokemons from Trainer's One team and Trainer Two's team
                    # are MissingNos that hadn't battled
                    # If both has battled, in an empty team or are not a MissingNos, goto the else
                    elif cond1 and cond2:
                        # If both are MissingNos that hadn't battled, place both MissingNo into separate Array Sorted List
                        self.missingno1 = self.get_missingno(self.pokemon1.value, self.team1)
                        self.missingno2 = self.get_missingno(self.pokemon2.value, self.team2)
                    else:
                        # Since the pokemons chosen aren't MissingNos, set their battled status to True
                        # This means that they have already battled
                        self.pokemon1.value.battled = True
                        self.pokemon2.value.battled = True
                        round_finished = self.compare_speed(self.pokemon1.value, self.pokemon2.value) # Enters battle between the 2 chosen pokemons
                else:
                    raise ValueError("Input battle mode is invalid")

        # If both teams are empty after the battle, it is a Draw
        if self.team1.team.is_empty() and self.team2.team.is_empty():
            battle_result = "Draw"
        # If Trainer One's team are empty after the battle, then Trainer Two wins
        elif self.team1.team.is_empty():
            battle_result = self.team2.trainer
        # If Trainer Two's team are empty after the battle, then Trainer One wins
        elif self.team2.team.is_empty():
            battle_result = self.team1.trainer
        else:
            raise ValueError("Winning team is invalid")
        return battle_result

    def compare_speed(self, pokemon_1: T, pokemon_2: T) -> bool:
        """
        Compares the speed of 2 battling pokemons to see who attacks first. If both have the same speed, they attack
        simultaneously
        :param pokemon_1: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param pokemon_2: A pokemon object from either classes from pokemon.py or MissingNo.py
        :return: A True or False if a pokemon has fainted
        :raises TypeError: If pokemon object isn't Charmander, Bulbasaur, Squirtle or MissingNo
        :complexity: Best is O(1) if it's a stack or circular queue. When a pokemon faints after taking the first
                     damage, it returns a boolean
                     Worst is O(N^2), where N is len(self) and  if it's an array sorted list. When MissingNo can be added back into the
                     team, it will traverse the list when obtaining MissingNo and placing it into array sorted list
        """
        # Checks if both pokemon inputs are an object derived from the PokemonBase
        if not isinstance(pokemon_1, PokemonBase):
            raise TypeError("Pokemon 1 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        elif not isinstance(pokemon_2, PokemonBase):
            raise TypeError("Pokemon 2 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        else:
            if self.battle_mode == 2:
                # Checks whether has all pokemons in Trainer One's team battled or if the Array Sorted List containing
                # MissingNo is empty
                if self.can_play(self.team1) and not(self.missingno1 is None or self.missingno1.is_empty()):
                    # If all pokemons in Trainer One's team has battled, removed MissingNo from the Array Sorted List,
                    # set its battled status and add it back into Trainer One's team
                    m = self.missingno1.withdraw()
                    m.value.battled = True
                    self.team1.team.modified_add(m)
                # Checks whether has all pokemons in Trainer Two's team battled or if the Array Sorted List containing
                # MissingNo is empty
                elif self.can_play(self.team2) and not(self.missingno2 is None or self.missingno2.is_empty()):
                    # If all pokemons in Trainer Two's team has battled, removed MissingNo from the Array Sorted List,
                    # set its battled status and add it back into Trainer Two's team
                    m = self.missingno2.withdraw()
                    m.value.battled = True
                    self.team2.team.modified_add(m)

            # Compares both pokemons speed to see who attacks first
            if pokemon_1.get_speed() > pokemon_2.get_speed():
                # If Trainer One's pokemon is faster than Trainer Two's pokemon, it attacks first
                return self.match(pokemon_1, pokemon_2, 1, 2)
            elif pokemon_2.get_speed() > pokemon_1.get_speed():
                # If Trainer Two's pokemon is faster than Trainer One's pokemon, it attacks first
                return self.match(pokemon_2, pokemon_1, 2, 1)
            else:
                # If both tainer's pokemon have the same speed, they attack simultaneously
                return self.match_same_speed(pokemon_1, pokemon_2, 1, 2)

    def match(self, fast_pokemon: T, slow_pokemon: T, faster_team: int, slower_team: int) -> bool:
        """
        Engages a battle between the 2 battling pokemon, where the fast pokemon attacks first and the slow one defends.
        If the slow pokemon faints, fast pokemon levels up. Otherwise the slow pokemon attacks and the fast one defends.
        If neither faints, both loses 1 health and return back into the team
        :param fast_pokemon: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param slow_pokemon: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param faster_team: An integer telling which team has the fast pokemon
        :param slower_team: An integer telling which team has the slow pokemon
        :return: A True or False if a pokemon has fainted
        :raises TypeError: If pokemon object isn't Charmander, Bulbasaur, Squirtle or MissingNo,
                           or if either/ both teams input aren't integers
        :raises ValueError: If either/ both teams input aren't 1 or 2
        :pre: 1 <= faster_team <= 2
        :pre: 1 <= slower_team <= 2
        :complexity: Best is O(1) if it's a stack or circular queue. The slow pokemon takes damage and faints,
                     returning a boolean.
                     Worst is O(N^2), where N is len(self) and  if it's an array sorted list. Both pokemon didn't faint and are sent back
                     into the team, where it adds the pokemon back in the first position
        """
        # Checks if both pokemon inputs are an object derived from the PokemonBase
        if not isinstance(fast_pokemon, PokemonBase):
            raise TypeError("Pokemon 1 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        elif not isinstance(slow_pokemon, PokemonBase):
            raise TypeError("Pokemon 2 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        # Checks if both team inputs are integer or not
        elif type(faster_team) != int:
            raise TypeError("Team 1's input must be integer")
        elif type(slower_team) != int:
            raise TypeError("Team 2's input must be integer")
        # Checks if both team inputs are either 1 or 2
        elif not 0 < faster_team < 3:
            raise ValueError("Choose 1 or 2 for team 1")
        elif not 0 < slower_team < 3:
            raise ValueError("Choose 1 or 2 for team 2")
        else:
            # Slow pokemon gets attacked by the fast pokemon since it's faster
            slow_pokemon.get_damage(fast_pokemon)
            # If slow pokemon faints from the attack, the fast pokemon levels up and returns to its team
            if slow_pokemon.has_fainted():
                fast_pokemon.level_up()
                # If battle mode is set to 2, update the pokemon's key criterion to what it is
                self.update_criterion(fast_pokemon, faster_team)
                self.returning(fast_pokemon, faster_team)
                return True
            else:
                # If slow pokemon doesn't faint from the attack, it attacks the fast pokemon
                fast_pokemon.get_damage(slow_pokemon)
                # If fast pokemon faints from the attack, the slow pokemon levels up and returns to its team
                if fast_pokemon.has_fainted():
                    slow_pokemon.level_up()
                    # If battle mode is set to 2, update the pokemon's key criterion to what it is
                    self.update_criterion(slow_pokemon, slower_team)
                    self.returning(slow_pokemon, slower_team)
                    return True
                else:
                    # If fast pokemon doesn't faint from the attack, both pokemons lose 1 HP
                    fast_pokemon.set_hp(fast_pokemon.get_hp() - 1)
                    slow_pokemon.set_hp(slow_pokemon.get_hp() - 1)
                    # If both pokemons faint from losing HP
                    if fast_pokemon.has_fainted() and slow_pokemon.has_fainted():
                        return True
                    # If slow pokemon faints from losing HP and the fast pokemon remains alive,
                    # the fast pokemon levels up and returns to its team
                    elif slow_pokemon.has_fainted():
                        fast_pokemon.level_up()
                        # If battle mode is set to 2, update the pokemon's key criterion to what it is
                        self.update_criterion(fast_pokemon, faster_team)
                        self.returning(fast_pokemon, faster_team)
                        return True
                    # If fast pokemon faints from losing HP and the fast pokemon remains alive,
                    # the slow pokemon levels up and returns to its team
                    elif fast_pokemon.has_fainted():
                        slow_pokemon.level_up()
                        # If battle mode is set to 2, update the pokemon's key criterion to what it is
                        self.update_criterion(slow_pokemon, slower_team)
                        self.returning(slow_pokemon, slower_team)
                        return True
                    # If neither faints from losing HP, they return to their respective teams
                    else:
                        # If battle mode is set to 2, update both pokemons' key criterions to what it is
                        self.update_criterion(fast_pokemon, faster_team)
                        self.update_criterion(slow_pokemon, slower_team)
                        self.returning(fast_pokemon, faster_team)
                        self.returning(slow_pokemon, slower_team)
                        return False

    def match_same_speed(self, pokemon_1: T, pokemon_2: T, team_1: int, team_2: int) -> bool:
        """
        Engages a battle between the 2 battling pokemon, where both pokemon attack and defend simultaneously.
        If one pokemon faints, the other one levels up. If neither faints, both loses 1 health and return
        to their teams
        :param pokemon_1: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param pokemon_2: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param team_1: An integer telling which team has the first pokemon
        :param team_2: An integer telling which team has the second pokemon
        :return: A True or False if a pokemon has fainted
        :raises TypeError: If pokemon object isn't Charmander, Bulbasaur, Squirtle or MissingNo,
                           or if either/ both teams input aren't integers
        :raises ValueError: If either/ both teams input aren't 1 or 2
        :pre: 1 <= team_1 <= 2
        :pre: 1 <= team_2 <= 2
        :complexity: Best is O(1) if it's a stack or circular queue. Both pokemon takes damage and faints,
                     returning a boolean
                     Worst is O(N^2), where N is len(self) and  if it's an array sorted list. Both pokemon didn't faint and are sent back
                     into the team, where it adds the pokemon back in the first position
        """
        # Checks if both pokemon inputs are an object derived from the PokemonBase
        if not isinstance(pokemon_1, PokemonBase):
            raise TypeError("Pokemon 1 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        elif not isinstance(pokemon_2, PokemonBase):
            raise TypeError("Pokemon 2 is not Charmander, Bulbasaur, Squirtle or MissingNo")
        # Checks if both team inputs are integer or not
        elif type(team_1) != int:
            raise TypeError("Team 1's input must be integer")
        elif type(team_2) != int:
            raise TypeError("Team 2's input must be integer")
        # Checks if both team inputs are either 1 or 2
        elif not 0 < team_1 < 3:
            raise ValueError("Choose 1 or 2 for team 1")
        elif not 0 < team_2 < 3:
            raise ValueError("Choose 1 or 2 for team 2")
        else:
            # Both pokemons deal damage to each other as both have same speed
            pokemon_1.get_damage(pokemon_2)
            pokemon_2.get_damage(pokemon_1)
            # If both pokemons faint from the attacks
            if pokemon_1.has_fainted() and pokemon_2.has_fainted():
                return True
            # If Trainer One's pokemon faint from the attacks and Trainer Two's pokemon remain alive,
            # Trainer Two's pokemon levels up and returns to its team
            elif pokemon_1.has_fainted():
                pokemon_2.level_up()
                # If battle mode is set to 2, update the pokemon's key criterion to what it is
                self.update_criterion(pokemon_2, team_2)
                self.returning(pokemon_2, team_2)
                return True
            # If Trainer Two's pokemon faint from the attacks and Trainer One's pokemon remain alive,
            # Trainer One's pokemon levels up and returns to its team
            elif pokemon_2.has_fainted():
                pokemon_1.level_up()
                # If battle mode is set to 2, update the pokemon's key criterion to what it is
                self.update_criterion(pokemon_1, team_1)
                self.returning(pokemon_1, team_1)
                return True
            else:
                # If neither pokemons faint from the attack, both pokemons lose 1 HP
                pokemon_1.set_hp(pokemon_1.get_hp() - 1)
                pokemon_2.set_hp(pokemon_2.get_hp() - 1)
                # If both pokemons faint from losing HP
                if pokemon_1.has_fainted() and pokemon_2.has_fainted():
                    return True
                # If Trainer One's pokemon faint from losing HP and Trainer Two's pokemon remain alive,
                # Trainer Two's pokemon levels up and returns to its team
                elif pokemon_1.has_fainted():
                    pokemon_2.level_up()
                    # If battle mode is set to 2, update the pokemon's key criterion to what it is
                    self.update_criterion(pokemon_2, team_2)
                    self.returning(pokemon_2, team_2)
                    return True
                # If Trainer Two's pokemon faint from losing HP and Trainer One's pokemon remain alive,
                # Trainer One's pokemon levels up and returns to its team
                elif pokemon_2.has_fainted():
                    pokemon_1.level_up()
                    # If battle mode is set to 2, update the pokemon's key criterion to what it is
                    self.update_criterion(pokemon_1, team_1)
                    self.returning(pokemon_1, team_1)
                    return True
                # If neither pokemon faints from losing HP, both return to their respective teams
                else:
                    # If battle mode is set to 2, update both pokemons' key criterions to what it is
                    self.update_criterion(pokemon_1, team_1)
                    self.update_criterion(pokemon_2, team_2)
                    self.returning(pokemon_1, team_1)
                    self.returning(pokemon_2, team_2)
                    return False

    def returning(self, pokemon: T, team: int) -> None:
        """
        Returns the pokemon back into their respective team after a battle against their opponent
        :param pokemon: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param team: An integer telling which team is the pokemon returning to
        :raises TypeError: If pokemon object isn't Charmander, Bulbasaur, Squirtle or MissingNo
                           or if team input isn't integer
        :raises ValueError: If team input aren't 1 or 2,
                            or if battle mode isn't set to 0, 1 or 2
        :pre: 1 <= team <= 2
        :complexity: Best is O(1) if it's a stack or circular queue as it adds back the element.
                     Worst is O(N^2), where N is len(self) and if it's an array sorted list. When item's key is not unique,
                     will have to loop through sorted list during search to derive index position to append
                     and if position is first
        """
        # Checks if pokemon input are an object derived from the PokemonBase and team input is an integer
        if not isinstance(pokemon, PokemonBase):
            raise TypeError("Pokemon is not Charmander, Bulbasaur, Squirtle or MissingNo")
        elif type(team) != int:
            raise TypeError("Each of the input team must be integer")
        # Checks if team input is either 1 or 2
        elif not 0 < team < 3:
            raise ValueError("Choose 1 or 2 for input team")
        # Checks which battle mode to determine the method used to add the pokemon back to its team
        else:
            # Use push() as it is a stack
            if self.battle_mode == 0:
                if team == 1:
                    self.team1.team.push(pokemon)
                elif team == 2:
                    self.team2.team.push(pokemon)
            # Use append() as it is a circular queue
            elif self.battle_mode == 1:
                if team == 1:
                    self.team1.team.append(pokemon)
                elif team == 2:
                    self.team2.team.append(pokemon)
            # Use modified_add() as it is an array sorted list
            elif self.battle_mode == 2:
                if team == 1:
                    self.team1.team.modified_add(self.pokemon1)
                elif team == 2:
                    self.team2.team.modified_add(self.pokemon2)
            else:
                raise ValueError("Input battle mode is invalid")

    def update_criterion(self, pokemon: T, team: int) -> None:
        """
        Sets and updates the pokemon's key so the Array Sorted List will sort the pokemons according to its
        criterion
        :param pokemon: A pokemon object from either classes from pokemon.py or MissingNo.py
        :param team: An integer telling which team the pokemon is in
        :raises TypeError: If pokemon object isn't Charmander, Bulbasaur, Squirtle or MissingNo,
                           or if team input isn't an integer
        :raises ValueError: If team input aren't 1 or 2
        :pre: 1 <= team <= 2
        :complexity: Best and Worst is O(1) as it sets the pokemon's key to an updated value
        """
        # Checks if pokemon input are an object derived from the PokemonBase and team input is an integer
        if not isinstance(pokemon, PokemonBase):
            raise TypeError("Pokemon is not Charmander, Bulbasaur, Squirtle or MissingNo")
        elif type(team) != int:
            raise TypeError("Each of the input team must be integer")
        # Checks if team input is either 1 or 2
        elif not 0 < team < 3:
            raise ValueError("Choose 1 or 2 for input team")
        else:
            # Gets the key criterion of the pokemon and set it to its key on the Array Sorted List item
            if self.battle_mode == 2:
                if team == 1:
                    self.pokemon1.key = self.team1.get_criterion(pokemon, self.criterion_team1)
                elif team == 2:
                    self.pokemon2.key = self.team2.get_criterion(pokemon, self.criterion_team2)
            else:
                pass

    def can_play(self, team: T) -> bool:
        """
        Checks whether all pokemon in the team has already been sent out to battle or not
        :param team: A PokeTeam object that contains the Pokemon objects
        :return: A True if every pokemon int the has battled or False if one pokemon hasn't battled
        :raises TypeError: If the input isn't a PokeTeam object
        :complexity: Best is O(1) if the first pokemon in the array sorted list hasn't battled.
                     Worst is O(len(self)) if all pokemons in the array sorted has battled
        """
        # Checks if team input is an object from the PokeTeam
        if not isinstance(team, PokeTeam):
            raise TypeError("Input is not a PokeTeam object")
        else:
            i = 0
            is_valid = True
            while is_valid and i < len(team.team):  # Loops through the pokemon team and break out if one hasn't battled
                if not team.team[i].value.has_battled():  # Checks if a pokemon has already battled or not
                    is_valid = False
                i += 1
            return is_valid

    def get_missingno(self, pokemon: T, team: T) -> ArraySortedList:
        """
        Creates a new Array Sorted List and adds MissingNo into the list
        :param pokemon: A MissingNo object
        :param team: A PokeTeam object that contains the Pokemon objects
        :return: An Array Sorted List containing the MissingNo object removed from its team
        :raises TypeError: If the input isn't a MissingNo object or PokeTeam object
        :complexity: Best and worst is O(len(self)) as it has to traverse len(self) to insert an element
        """
        # Checks if pokemon input is a MissingNo object and team input is an object from the PokeTeam
        if not isinstance(pokemon, MissingNo):
            raise TypeError("Input pokemon is not a MissingNo object")
        elif not isinstance(team, PokeTeam):
            raise TypeError("Input team is not a PokeTeam object")
        else:
            sorted_lst = ArraySortedList(1)  # Create a new array sorted list with length of 1

            # Adds the chosen pokemon into the list
            sorted_lst.add(ListItem(pokemon, team.get_criterion(pokemon, self.criterion_team1)))
            return sorted_lst
