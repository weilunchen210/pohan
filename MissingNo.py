"""
Class for a MissingNo object with its stats and methods from the GlitchMon and PokeBase classes
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 29.04.2022
"""
from GlitchMon import GlitchMon
from pokemon_base import PokemonBase
from random import randint

dsdsdsdsdsds #gaysdsdsdsdsdsdsds
class MissingNo(GlitchMon):
    NAME = "MissingNo"

    def __init__(self):
        """
        Constructor for MissingNo class
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        # values of hp, attack, defence and speed derieves from the average of the 3 classes, Charmander, Squirtle, Bulbasaur.
        GlitchMon.__init__(self, (7+9+8)//3, "None")
        self.attack = int((6 + self.get_level() + 5 + 4 + self.get_level() // 2) / 3)
        self.defence = int((4 + 5 + 6 + self.get_level()) / 3)
        self.speed = int((7 + self.get_level() + 7 + 7 + self.get_level() // 2) / 3)
        self.battled = False

    def get_name(self) -> str:
        """
        Returns the pokemon's name
        :return: A string of the pokemon's name
        :complexity: Best and worst is O(1) as it returns the pokemon's name
        """
        return MissingNo.NAME

    def get_speed(self) -> int:
        """
        Returns the pokemon's speed value
        :return: An integer of the pokemon's speed
        :complexity: Best and worst is O(1) as it returns the speed value
        """
        return self.speed + self.get_level() - 1

    def get_attack_damage(self) -> int:
        """
        Returns the pokemon's attack damage value
        :return: An integer of the pokemon's attack damage
        :complexity: Best and worst is O(1) as it returns the attack damage value
        """
        return self.attack + self.get_level() - 1

    def get_defence(self) -> int:
        """
        Returns the pokemon's defence value
        :return: An integer of the pokemon's defence
        :complexity: Best and worst is O(1) as it returns the defence value
        """
        return self.defence + self.get_level() - 1

    def has_battled(self) -> bool:
        """
        Return pokemon's battle status on whether has it been in a battle
        :return: A True if it has battled and False if it hasn't
        :complexity: Best and worst is O(1) as it returns a boolean value
        """
        return self.battled

    def get_damage(self, opponent: PokemonBase) -> None:
        """
        Calculates the opponent's effective damage taken by the pokemon and update the pokemon's hp and calls for
        a superpower when defending.
        :param opponent: A pokemon object that is attacking this pokemon.
        :raises TypeError: If opponent isn't a Charmander, Bulbasaur, Squirtle or MissingNo
        :complexity: Best and worst is O(1) following the update_health() method
        """
        if not isinstance(opponent, PokemonBase):
            # Check if passed parameter opponent is of type PokemonBase.
            raise TypeError("The opponent must be a Pokemon object")
        else:
            # Check passed.
            self.superpower() # Calls MissingNo superpower
            damage = opponent.get_attack_damage() # Opponents attack damage.
            effective_damage = damage * 1
            self.update_health(float(effective_damage)) # Updates MissingNo object's health.

    def update_health(self, damage: float) -> None:
        """
        Updates this pokemon's hp after getting damaged.
        Effective damage on this pokemon depends upon a selected defence scenario from the 3 pokemon it derives from
        :param damage: A float number of the damage to be received
        :raises TypeError: If damage is not a float
        :raises ValueError: If damage is a negative number
        :pre: damage >= 0
        :complexity: Best and worst is O(1) as it checks whether damage taken is greater than pokemon's defence and
                     sets the pokemon's hp
        """
        if type(damage) != float:
            # Check if passed parameter damage is of type float.
            raise TypeError("Damage is not a float")
        elif damage < 0:
            # Check if passed parameter damage is greater or equal to 0.
            raise ValueError("Damage cannot be a negative value")
        else:
            # If all checks passed.
            chance = randint(0,2)
            # Generate random num between 0 to 2 inclusive.
            # Utilised in deciding the defence scenario in which this MissingNo object will utilise for its current battle.
            if chance == 0:
                # If generated num is 0. Defence scenario to be utilized will be Charmander's
                if damage > (self.get_defence()):
                    # If damage to be dealt to this Charmander object is greater than its defence.
                    if self.get_hp() - damage < 0:
                        # If this Charmander objects's hp is less than 0 after receiving damage, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Charmander objects's hp to its current hp subtracted by the damage to be dealt.
                        self.set_hp(int(self.get_hp() - damage))
                else:
                    # If damage to be dealt to this Charmander object is less than its defence.
                    if self.get_hp() - damage // 2 < 0:
                        # If this Charmander objects's hp is less than 0 after receiving damage // 2, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Charmander objects's hp to its current hp subtracted by the damage// 2 to be dealt.
                        self.set_hp(int(self.get_hp() - damage // 2))
            elif chance == 1:
                # If generated num is 1. Defence scenario to be utilized will be Bulbasaur's
                if damage > (self.get_defence() + 5):
                    # If damage to be dealt to this Bulbasaur object is greater than its defence + 5.
                    if self.get_hp() - damage < 0:
                        # If this Bulbasaur objects's hp is less than 0 after receiving damage, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Bulbasaur objects's hp to its current hp subtracted by the damage to be dealt.
                        self.set_hp(int(self.get_hp() - damage))
                else:
                    # If damage to be dealt to this Bulbasaur object is less than its defence + 5.
                    if self.get_hp() - damage // 2 < 0:
                        # If this Bulbasaur objects's hp is less than 0 after receiving damage // 2, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Bulbasaur objects's hp to its current hp subtracted by the damage// 2 to be dealt.
                        self.set_hp(int(self.get_hp() - damage // 2))
            else:
                # Else defence scenario to be utilized will be Squirtle's
                if damage > (self.get_defence() * 2):
                    # If damage to be dealt to this Squirtle object is greater than its defence * 2.
                    if self.get_hp() - damage < 0:
                        # If this Squirtle objects's hp is less than 0 after receiving damage, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Squirtle objects's hp to its current hp subtracted by the damage to be dealt.
                        self.set_hp(int(self.get_hp() - damage))
                else:
                    # If damage to be dealt to this Squirtle object is less than its defence * 2.
                    if self.get_hp() - damage // 2 < 0:
                        # If this Squirlte objects's hp is less than 0 after receiving damage // 2, set its hp to 0.
                        self.set_hp(0)
                    else:
                        # Else set this Squirtle objects's hp to its current hp subtracted by the damage// 2 to be dealt.
                        self.set_hp(int(self.get_hp() - damage // 2))
