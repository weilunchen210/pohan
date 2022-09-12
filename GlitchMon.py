"""
Class for a glitch pokemon object with its stats and methods
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 29.04.2022
"""
from pokemon_base import PokemonBase
from random import randint


class GlitchMon(PokemonBase):
    def __init__(self, hp: int, poke_type: str) -> None:
        """
        Constructor for GlitchMon class
        :param hp: An integer of GlitchMon's HP value
        :param poke_type: A string of GlitchMon's pokemon type
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        PokemonBase.__init__(self, hp, poke_type)

    def increase_health(self, health: int) -> None:
        """
        Increases pokomon's health by passed value
        :param health: An integer to increase pokemon's health by
        :raises TypeError: If health isn't an integer
        :pre: health value > 0
        :complexity: Best and worst is O(1) as it sets the pokemon's hp when it's alive
        """
        if type(health) != int:
            # Check if passed parameter health is of tpe int.
            raise TypeError("Health has to be an integer")
        else:
            # Check passed
            if health > 0:
                # Check if passed parameter helath is greater than 0.
                # If true, this object's hp will be set to its current hp + the passed parameter health
                self.set_hp(self.get_hp() + health)
            else:
                # Else no modification to this object's hp.
                pass

    def superpower(self) -> str:
        """
        Decides whether pokemon benefits from its superpower
        :return: A string description of gained benefits
        :complexity: Best and worst is O(1) as it randomises, selects an effect then increases a level, hp or not
        """
        if randint(1, 100) <= 25:
            # Check if this pokemon benefits from its superpower.
            # Generate value between 1 and 100, if less or equal to 25. This pokemon will benefit from its superpower.
            effect = randint(0, 2)
            # Generate a random number between 0 and 2.
            # Utilized in deciding the effect the pokemon will benefit from.
            if effect == 0:
                # If generated value is 0, pokemon will benefit from an increase in its level by 1.
                self.set_level(self.get_level() + 1)
                result = "It leveled up"
            elif effect == 1:
                # If generated value is 1, pokemon will benefit from an increase in its hp by 1.
                self.increase_health(1)
                result = "It gained 1 HP"
            else:
                # Else, for any other value, pokemon will benefit from an increase in its level and hp by 1.
                self.increase_health(1)
                self.set_level(self.get_level() + 1)
                result = "It gained 1 HP and leveled up"
            return result # A string description of gained benefits
        else:
            # If pokemon did not benefit from its superpower.
            return "Superpower not achieved" # A string description of the pokemon's failure to utilize superpower.
