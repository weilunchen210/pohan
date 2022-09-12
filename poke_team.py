"""
Class where pokemon teams are created and pokemons are assigned to their teams
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 30.04.2022
"""
from stack_adt import ArrayStack
from pokemon import Charmander, Bulbasaur, Squirtle
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList
from sorted_list import ListItem
from pokemon_base import PokemonBase
from MissingNo import MissingNo
from typing import TypeVar

T = TypeVar('T', Charmander, Bulbasaur, Squirtle, MissingNo, PokemonBase)


class PokeTeam(Charmander, Squirtle, Bulbasaur):
    LIMIT = 6
    MISSINGNO_MAX = 1

    def __init__(self, trainer: str) -> None:
        """
        Constructor for Poke_team
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        self.criterion = None
        self.battle_mode = 0
        self.team = None
        self.trainer = trainer

    def get_team_limit(self) -> int:
        """
        Returns the maximum number of pokemons allowed in a team
        :return: An integer of all team's limit
        :complexity: Best and worst is O(1) as it returns the team's limit value
        """
        return PokeTeam.LIMIT

    def get_missingno_max(self) -> int:
        """
        Returns the maximum number of MissingNo allowed in a team
        :return: An integer of how many MissingNo is allowed in a team
        :complexity: Best and worst is O(1) as it returns the maximum number of MissingNo allowed in a team
        """
        return PokeTeam.MISSINGNO_MAX

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """
        Selects a team of Charmander, Bulbasaur, Squirtle, and MissingNo.
        Team is only succeccfully selected if certain criterias are met.
        :param battle_mode: An integer that determines the type of battle
        :param criterion: A string or None that determines the order in which each pokemon in the team will battle
        :raises TypeError: If battle_mode isn't an integer,
                           or criterion is not a string when inputted
        :raises ValueError: If battle_mode isn't 0, 1 or 2
        :pre: 0 <= battle_mode <= 2
        :complexity: Best O(N), occurs if user_input is valid in the first try.
                    Worst O(N^2) where user input is not valid in the first try.
        """
        if type(battle_mode) != int:
            # Check if passed parameter battle_mode is of type int.
            raise TypeError("Battle mode input must be an integer")
        elif criterion is not None and type(criterion) != str:
            # Check if passed parameter criterion is of type string.
            raise TypeError("Criterion input must be a string")
        elif not 0 <= battle_mode <= 2:
            # Check if passed parameter battle mode is of between values 0 and 2 inclusive.
            raise ValueError("Battle mode input must be 0, 1 or 2")
        else:
            # All checks passed.
            self.battle_mode = battle_mode
            self.criterion = criterion
            is_valid = False

            message = "Howdy Trainer! Choose your team as C B S or C B S M\n" + \
                      "where C is the number of Charmanders\n" + \
                      "\t  B is the number of Bulbasaurs\n" + \
                      "\t  S is the number of Squirtles\n" + \
                      "\t  M is the number of MissingNo"
            print(message)

            while not is_valid:
                # Will loop till user_input is valid
                user_input = str(input())
                pokemon_head_count = [int(entry) for entry in user_input.split()]  # Stores user input as a list.
                # Length of list will represent the number of type of pokemons user will utilise to form their team.
                # Each element in the list will represent the number of desired pokemon type.
                if len(pokemon_head_count) == 3:
                    # Checks if user has inputted for a team with 3 type of pokemons.
                    if 0 < sum(pokemon_head_count) <= self.get_team_limit():
                        # Check if total number of entered pokemons for the team is less than or equal to the team_limit and greater than 0.
                        is_valid = True
                        self.assign_team(pokemon_head_count[0], pokemon_head_count[1], pokemon_head_count[
                            2])  # Forms the team with the desired num of pokemons for each pokemon type
                    else:
                        # Else, print appropriate message, regarding the total pokemons entered exceeding the limit.
                        print("Please enter a valid input\n" + message)
                elif len(pokemon_head_count) == 4:
                    # Checks if user has inputted for a team with 4 type of pokemons.
                    if 0 < sum(pokemon_head_count) <= self.get_team_limit() and pokemon_head_count[3] == self.get_missingno_max():
                        # Check if total number of entered pokemons for the team is less than or equal to the team_limit and greater than 0.
                        # As well as checking if the number of MissingNo pokemons is equal to 1.
                        is_valid = True
                        self.assign_team(pokemon_head_count[0], pokemon_head_count[1], pokemon_head_count[2],
                                         pokemon_head_count[
                                             3])  # Forms the team with the desired num of pokemons for each pokemon type
                    else:
                        # Else, print appropriate message, regarding the total pokemons entered exceeding the limit.
                        print("Please enter a valid input\n" + message)

    def assign_team(self, charm: int, bulb: int, squir: int, missi: int = 0) -> None:
        """
        Forms a team of Charmander, Bulbasaur, Squirtle, and MissingNo.
        Order of attacking determined by battle_mode.

        :param charm: An integer of how many Charmanders to be added to the team
        :param bulb:  An integer of how many Bulbasaurs to be added to the team
        :param squir:  An integer of how many Squirtles to be added to the team
        :param missi:  An integer of how many MissingNo to be added to the team
        :raises TypeError: If either/ all the inputs aren't integers
        :raises ValueError: If either/ all the inputs are negative values
        :pre: charm + bulb + squir + missi <= 7
        :pre: 0 <= battle_mode <= 2
        :complexity: Best O(team_size), where battle mode = 0 or battle mode = 1.
                     Worst O(team_size*log n), where battle mode = 2.
        """
        if type(charm) != int:
            # Check if passed parameter charm is of type int.
            raise TypeError("Charmander's input must be an integer")
        elif type(bulb) != int:
            # Check if passed parameter bulb is of type int.
            raise TypeError("Bulbasaur's input must be an integer")
        elif type(squir) != int:
            # Check if passed parameter squir is of type int.
            raise TypeError("Squirtle's input must be an integer")
        elif type(missi) != int:
            # Check if passed parameter missi is of type int.
            raise TypeError("MissingNo's input must be an integer")
        elif charm < 0:
            # Check if passed parameter charm is greater or equal to 0.
            raise ValueError("Charmander's input must not be a negative value")
        elif bulb < 0:
            # Check if passed parameter bulb is greater or equal to 0.
            raise ValueError("Bulbasaur's input must not be a negative value")
        elif squir < 0:
            # Check if passed parameter squir is greater or equal to 0.
            raise ValueError("Squirtle's input must not be a negative value")
        elif missi < 0:
            # Check if passed parameter missi is greater or equal to 0.
            raise ValueError("MissingNo's input must not be a negative value")
        else:
            team_size = charm + bulb + squir + missi
            if self.battle_mode == 0:
                # Check if battle_mode == 0. Will decide method of forming team.
                self.team = ArrayStack(team_size)  # team will be of type ArrayStack with length of team size.
                for i in range(missi):
                    self.team.push(MissingNo())  # Pushes a new MissingNo object to the ArrayStak.
                for i in range(squir):
                    self.team.push(Squirtle())  # Pushes a new Squirtle object to the ArrayStak.
                for i in range(bulb):
                    self.team.push(Bulbasaur())  # Pushes a new Bulbasaur object to the ArrayStak.
                for i in range(charm):
                    self.team.push(Charmander())  # Pushes a new Charmander object to the ArrayStak.
            elif self.battle_mode == 1:
                # Check if battle_mode == 1. Will decide method of forming team.
                self.team = CircularQueue(team_size)  # team will be of type CircularQueue with length of team size.
                for i in range(charm):
                    self.team.append(Charmander())  # Appends a new Charmander object to the CircularQueue.
                for i in range(bulb):
                    self.team.append(Bulbasaur())  # Appends a new Bulbasaur object to the CircularQueue.
                for i in range(squir):
                    self.team.append(Squirtle())  # Appends a new Squirtle object to the CircularQueue.
                for i in range(missi):
                    self.team.append(MissingNo())  # Appends a new MissingNo object to the CircularQueue.
            elif self.battle_mode == 2:
                # Check if battle_mode == 1. Will decide method of forming team.
                self.team = ArraySortedList(team_size)  # team will be of type ArraySortedList with length of team size.
                for i in range(charm):
                    c = Charmander()
                    self.team.modified_add(ListItem(c, self.get_criterion(c, self.criterion)))  # Adds a ListItem with value Charmander and key as the passed criterion to the ArraySortedList.
                for i in range(bulb):
                    b = Bulbasaur()
                    self.team.modified_add(ListItem(b, self.get_criterion(b, self.criterion)))  # Adds a ListItem with value Bulbasaur and key as the passed criterion to the ArraySortedList.
                for i in range(squir):
                    s = Squirtle()
                    self.team.modified_add(ListItem(s, self.get_criterion(s, self.criterion)))  # Adds a ListItem with value Squirtle and key as the passed criterion to the ArraySortedList.
                for i in range(missi):
                    m = MissingNo()
                    self.team.modified_add(ListItem(m, self.get_criterion(m,self.criterion)))  # Adds a ListItem with value MissingNo and key as the passed criterion to the ArraySortedList.
            else:
                raise Exception("Input battle mode is invalid")

    def get_criterion(self, pokemon: T, criterion: str) -> int:
        """
        Returns key value of passed pokemon.
        Key Value will depend on the set criteria. Only utilized when battle_mode = 2
        :param pokemon: A pokemon object of whose key to be retrieved
        :param criterion: A string of the criterion
        :return: An integer of the pokemon's key
        :raises TypeError: If pokemon isn't Charmander, Bulbasaur, Squirtle, or MissingNo,
                           or criterion isn't a string when inputted
        :raises ValueError: If criterion isn't lvl, hp, atk, def or spd
        :complexity: Best and Worst is O(1) as it checks for the required criterion, obtains it and returns it
        """
        if not isinstance(pokemon, PokemonBase):
            # Check if passed parameter pokemon is of type PokemonBase
            raise TypeError("Pokemon input must be a pokemon object")
        elif criterion is not None and type(criterion) != str:
            # Check if passed parameter criterion is not None and is of type string.
            raise TypeError("Criterion input must be a string")
        else:
            if criterion is None:
                # Check If criterion is None, no action will be performed.
                pass
            elif criterion == "lvl":
                # Check is criterion is lvl. If true, return the passed pokemon level.
                return pokemon.get_level()
            elif criterion == "hp":
                # Check is criterion is hp. If true, return the passed pokemon hp.
                return pokemon.get_hp()
            elif criterion == "atk":
                # Check is criterion is atk. If true, return the passed pokemon attack damage.
                return pokemon.get_attack_damage()
            elif criterion == "def":
                # Check is criterion is def. If true, return the passed pokemon defence.
                return pokemon.get_defence()
            elif criterion == "spd":
                # Check is criterion is spd. If true, return the passed pokemon speed.
                return pokemon.get_speed()
            else:
                raise ValueError("Input criterion is invalid")

    def get_pokemon(self, battle_mode: int) -> T:
        """
        Retrieves the pokemon in self.team that will soon battle by depending on the battle mode value
        :param battle_mode: An integer of the battle mode setted
        :return: A pokemon object retrieved from self.team
        :raises TypeError: If battle_mode isn't an integer value
        :raises ValueError: If battle_mode is not 0, 1 or 2
        :pre: 0 <= battle_mode <= 2
        :complexity: Best is O(1) if it's a stack or circular queue as it access the element from the top or front.
                     Worst is O(len(self)) if it's an array sorted list as it has to traverse to len(self) and obtain
                     the element
        """
        if type(battle_mode) != int:
            # Check if passed parameter battle_mode is of type int.
            raise TypeError("Battle mode input must be an integer")
        elif not 0 <= battle_mode <= 2:
            # Check is passed parameter battle_mode is between values 0 to 2 inclusive.
            raise ValueError("Battle mode input must be 0, 1 or 2")
        else:
            if battle_mode == 0:
                # If battle mode 0. Pop pokemon from ArrayStack.
                return self.team.pop()
            elif battle_mode == 1:
                # If battle mode 1. Serve pokemon from CircularQueue.
                return self.team.serve()
            elif battle_mode == 2:
                # If battle mode 2. Withdraw ListItem from ArraySortedList.
                return self.team.withdraw()

    def __str__(self) -> str:
        """
        Returns all pokemon in team
        :return: A string of the pokemon team with its members
        :complexity: Best and worst is O(length) as it returns the PokeTeam object (stack, circular queue or array
                     sorted list) in string format
        """
        return str(self.team)
