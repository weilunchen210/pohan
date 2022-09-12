"""
Abstract class for the Pokemons and GlitchMon class
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 29.04.2022
"""
from abc import ABC, abstractmethod


class PokemonBase(ABC):
    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Constructor for this PokemonBase class
        :param hp: An integer for the pokemon's health
        :param poke_type: A string for the pokemon's type
        :raises TypeError: If hp is not an integer,
                           or poke_type is a string
        :raises ValueError: If hp is lesser than or equal to 0
        :pre: hp > 0
        :complexity: Best and worst is O(1) as it initialise hp and poke_type
        """
        if type(hp) != int:
            # Check if passed parameter hp is of type int.
            raise TypeError("HP must be an integer")
        elif type(poke_type) != str:
            # Check if passed parametere poke_type is of type string.
            raise TypeError("Pokemon type must be a string")
        elif hp <= 0:
            # Check if passed parameter hp is greater than 0.
            raise ValueError("HP must be above 0")
        else:
            # If all check passed, will assign the passed values to the appropriate attributes.
            self.hp = hp
            self.level = 1
            self.poke_type = poke_type

    def set_hp(self, new_health: int) -> None:
        """
        Sets the pokemon's hp to value of new_health.
        :param new_health: Value of health to be set.
        :raises TypeError: If new_health is not an integer
        :raises ValueError: If new_health is a negative number
        :pre: new_health >= 0
        :complexity: Best and worst is O(1) as it initialise hp
        """
        if type(new_health) != int:
            # Check if passed parameter new_health is of type int.
            raise TypeError("HP must be an integer")
        elif new_health < 0:
            # Check if passed parameter new_health has a value greater or equal to 0.
            raise ValueError("HP must not be a negative value")
        else:
            # If all checks passed object's hp will be set to the value of new_health.
            self.hp = new_health

    def set_level(self, new_level: int) -> None:
        """
        Sets the pokemon's level to value of new_level.
        :param new_level: Value of level to be set.
        :raises TypeError: If new_level is not an integer
        :raises ValueError: If new_level is lesser than or equal to 0
        :pre: new_health > 0
        :complexity: Best and worst is O(1) as it initialise level
        """
        if type(new_level) != int:
            # Check if passed parameter new_level if of type int.
            raise TypeError("Level must be an integer")
        elif new_level <= 0:
            # Check if passed parameter new_level has a value greater than 0.
            raise ValueError("Level must be above 0")
        else:
            # If all checks passed object's level will be set to the value of new_level.
            self.level = new_level

    def get_hp(self) -> int:
        """
        Returns the pokemons's hp value
        :return: An integer of the pokemon's health
        :raises TypeError: If self.hp is not an integer
        :raises ValueError: If self.hp is a negative number
        :complexity: Best and worst is O(1) as it returns hp value
        """
        if type(self.hp) != int:
            # Check if object's hp is of type int.
            raise TypeError("HP must be an integer")
        elif self.hp < 0:
            # Check if objects hp has a value greater or equal to 0.
            raise ValueError("HP must not be a negative value")
        else:
            # If all checks passed, object's hp will be returned.
            return self.hp

    def get_level(self) -> int:
        """
        Returns the pokemons's level value
        :return: An integer of the pokemon's level
        :raises TypeError: If self.level is not an integer
        :raises ValueError: If self.level is a negative number
        :complexity: Best and worst is O(1) as it returns level value
        """
        if type(self.level) != int:
            # Check if object's level is of type int.
            raise TypeError("Level must be an integer")
        elif self.level <= 0:
            # Check if objects level has a value greater than 0.
            raise ValueError("Level must be above 0")
        else:
            # If all checks passed, object's level will be returned.
            return self.level

    @abstractmethod
    def get_name(self) -> str:
        """
        Returns the pokemon's name
        :return: A string of the pokemon's name
        """
        pass

    @abstractmethod
    def get_speed(self) -> int:
        """
        Returns the pokemon's speed value
        :return: An integer of the pokemon's speed
        """
        pass

    @abstractmethod
    def get_attack_damage(self) -> int:
        """
        Returns the pokemon's attack damage value
        :return: An integer of the pokemon's attack damage
        """
        pass

    def get_poke_type(self) -> str:
        """
        Returns the pokemons's type
        :return: A string of the pokemon's type
        :raises TypeError: If self.poke_type isn't a string
        :complexity: Best and worst is O(1) as it returns the pokemon's type
        """
        if type(self.poke_type) != str:
            # Check if object's poke_type is of type string.
            raise TypeError("Pokemon's type must be a string")
        else:
            # If check passed object's poke_type will be returned.
            return self.poke_type

    @abstractmethod
    def get_damage(self, opponent) -> None:
        """
        Calculates the opponent's effective damage taken by the pokemon and update the pokemon's hp
        :param opponent: A pokemon object that is attacking this pokemon.
        """
        pass

    @abstractmethod
    def update_health(self, damage: float) -> None:
        """
        Updates the pokemon hp after getting damaged
        :param damage: A float number of the damage to be received
        """
        pass

    @abstractmethod
    def get_defence(self) -> int:
        """
        Returns the pokemon's defence value
        :return: An integer of the pokemon's defence
        """
        pass

    def has_fainted(self) -> bool:
        """
        Returns whether pokemon is alive
        :return: A True if the pokemon's hp is lower than 1 and False if the pokemon's hp is a positive value
        :complexity: Best and worst is O(1) as it returns a boolean after checking
        """
        if self.get_hp() > 0:
            # Check if objects hp is greater than 0, if true return false.
            return False
        else:
            # If object's hp is less than or equal to 0, true will be returned.
            return True

    def level_up(self) -> None:
        """
        Increases pokemon's level by 1
        :complexity: Best and worst is O(1) as it sets the hp + 1
        """
        self.set_level(self.get_level() + 1)

    @abstractmethod
    def has_battled(self) -> bool:
        """
        Return pokemon's battle status on whether has it been in a battle
        :return: A True if it has battled and False if it hasn't
        """
        pass

    def __str__(self) -> str:
        """
        Returns the pokemon's name, hp and level
        :return: A string of the pokemon object
        :complexity: Best and worst is O(1) as it returns the pokemon object in string format
        """
        return "{}'s HP = {} and level = {}".format(self.get_name(), self.get_hp(), self.get_level())

