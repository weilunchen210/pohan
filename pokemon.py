"""
Classes for a pokemon object with its stats and methods
Author: Wah Yang Tan, Po Han Tay, Jun Heng Tan, Guan Yan Tan
Last Modified: 29.04.2022
"""
from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    NAME = "Charmander"
    ATTACK = 6
    DEFENCE = 4
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor for Charmander Class
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        PokemonBase.__init__(self, 7, "Fire")
        self.battled = False

    def get_name(self) -> str:
        """
        Returns the pokemon's name
        :return: A string of the pokemon's name
        :complexity: Best and worst is O(1) as it returns the pokemon's name
        """
        return Charmander.NAME

    def get_speed(self) -> int:
        """
        Returns the pokemon's speed value that scales with its level
        :return: An integer of the pokemon's speed
        :complexity: Best and worst is O(1) as it returns the speed value
        """
        return Charmander.SPEED + self.level

    def get_attack_damage(self) -> int:
        """
        Returns the pokemon's attack damage value that scales with its level
        :return: An integer of the pokemon's attack damage
        :complexity: Best and worst is O(1) as it returns the attack damage value
        """
        return Charmander.ATTACK + self.level

    def get_defence(self) -> int:
        """
        Returns the pokemon's defence value
        :return: An integer of the pokemon's defence
        :complexity: Best and worst is O(1) as it returns the defence value
        """
        return Charmander.DEFENCE

    def has_battled(self) -> bool:
        """
        Return pokemon's battle status on whether has it been in a battle
        :return: A True if it has battled and False if it hasn't
        :complexity: Best and worst is O(1) as it returns a boolean value
        """
        return self.battled

    def get_damage(self, opponent: PokemonBase) -> None:
        """
        Calculates the opponent's effective damage taken by the pokemon and update the pokemon's hp
        :param opponent: A pokemon object that is attacking this pokemon.
        :raises TypeError: If opponent isn't a Charmander, Bulbasaur, Squirtle or MissingNo
        :complexity: Best and worst is O(1) following the update_health() method
        """
        if not isinstance(opponent, PokemonBase):
            # Check if passed parameter opponent is of type PokemonBase
            raise TypeError("The opponent must be a Pokemon object")
        else:
            # Check passed.
            damage = opponent.get_attack_damage() # opponent's attack damage
            if opponent.get_poke_type() == "Grass":
                # Check if opponent is of type Grass. If true, damage to be dealt to this Charmander object will be halved.
                effective_damage = damage * 0.5
                self.update_health(effective_damage)
            elif opponent.get_poke_type() == "Water":
                # Check if opponent is of type Water. If true, damage to be dealt to this Charmander object will be doubled.
                effective_damage = damage * 2
                self.update_health(float(effective_damage))
            else:
                # Else damage to be dealt to this Charmander object will remain the same.
                effective_damage = damage * 1
                self.update_health(float(effective_damage))

    def update_health(self, damage: float) -> None:
        """
        Updates the pokemon hp after getting damaged
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
            # Check if passed parameter damage has a value greater or equal to 0.
            raise ValueError("Damage cannot be a negative value")
        else:
            # If all checks passed.
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


class Bulbasaur(PokemonBase):
    NAME = "Bulbasaur"
    ATTACK = 5
    DEFENCE = 5
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor for Bulbasaur class
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        PokemonBase.__init__(self, 9, "Grass")
        self.battled = False

    def get_name(self) -> str:
        """
        Returns the pokemon's name
        :return: A string of the pokemon's name
        :complexity: Best and worst is O(1) as it returns the pokemon's name
        """
        return Bulbasaur.NAME

    def get_speed(self) -> int:
        """
        Returns the pokemon's speed that scales with the floor value of it's level halved
        :return: An integer of the pokemon's speed
        :complexity: Best and worst is O(1) as it returns the speed value
        """
        return Bulbasaur.SPEED + self.level // 2

    def get_attack_damage(self) -> int:
        """
        Returns the pokemon's attack damage
        :return: An integer of the pokemon's attack damage
        :complexity: Best and worst is O(1) as it returns the attack damage value
        """
        return Bulbasaur.ATTACK

    def get_defence(self) -> int:
        """
        Returns the pokemon's defence value
        :return: An integer of the pokemon's defence
        :complexity: Best and worst is O(1) as it returns the defence value
        """
        return Bulbasaur.DEFENCE

    def has_battled(self) -> bool:
        """
        Return pokemon's battle status on whether has it been in a battle
        :return: A True if it has battled and False if it hasn't
        :complexity: Best and worst is O(1) as it returns a boolean value
        """
        return self.battled

    def get_damage(self, opponent: PokemonBase) -> None:
        """
        Calculates the opponent's effective damage taken by the pokemon and update the pokemon's hp.
        :param opponent: A pokemon object that is attacking this pokemon.
        :raises TypeError: If opponent isn't a Charmander, Bulbasaur, Squirtle or MissingNo
        :complexity: Best and worst is O(1) following the update_health() method
        """
        if not isinstance(opponent, PokemonBase):
            # Check if passed parameter opponent is of type PokemonBase
            raise TypeError("The opponent must be a Pokemon object")
        else:
            # Check passed.
            damage = opponent.get_attack_damage() # opponent's attack damage
            if opponent.get_poke_type() == "Water":
                # Check if opponent is of type Water. If true, damage to be dealt to this Bulbasaur object will be halved.
                effective_damage = damage * 0.5
                self.update_health(effective_damage)
            elif opponent.get_poke_type() == "Fire":
                # Check if opponent is of type Fire. If true, damage to be dealt to this Bulbasaur object will be doubled.
                effective_damage = damage * 2
                self.update_health(float(effective_damage))
            else:
                # Else damage to be dealt to this Bulbasaur object will remain the same.
                effective_damage = damage * 1
                self.update_health(float(effective_damage))

    def update_health(self, damage: float) -> None:
        """Updates the pokemon hp after getting damaged.
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
            # Check if passed parameter damage has a value greater or equal to 0.
            raise ValueError("Damage cannot be a negative value")
        else:
            # If all checks passed.
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


class Squirtle(PokemonBase):
    NAME = "Squirtle"
    ATTACK = 4
    DEFENCE = 6
    SPEED = 7

    def __init__(self) -> None:
        """
        Constructor for Squirtle class
        :complexity: Best and worst is O(1) as local variables are initialised
        """
        PokemonBase.__init__(self, 8, "Water")
        self.battled = False

    def get_name(self) -> str:
        """
        Returns the pokemon's name
        :return: A string of the pokemon's name
        :complexity: Best and worst is O(1) as it returns the pokemon's name
        """
        return Squirtle.NAME

    def get_speed(self) -> int:
        """
        Returns the pokemon's speed
        :return: An integer of the pokemon's speed
        :complexity: Best and worst is O(1) as it returns the speed value
        """
        return Squirtle.SPEED

    def get_attack_damage(self) -> int:
        """
        Returns the pokemon's attack damage that scales with the floor value of it's level halved
        :return: An integer of the pokemon's attack damage
        :complexity: Best and worst is O(1) as it returns the attack damage value
        """
        return Squirtle.ATTACK + self.level // 2

    def get_defence(self) -> int:
        """
        Returns the pokemon's defence value that scales with its level
        :return: An integer of the pokemon's defence
        :complexity: Best and worst is O(1) as it returns the defence value
        """
        return Squirtle.DEFENCE + self.level

    def has_battled(self) -> bool:
        """
        Return pokemon's battle status on whether has it been in a battle
        :return: A True if it has battled and False if it hasn't
        :complexity: Best and worst is O(1) as it returns a boolean value
        """
        return self.battled

    def get_damage(self, opponent: PokemonBase) -> None:
        """
        Calculates the opponent's effective damage taken by the pokemon and update the pokemon's hp.
        :param opponent: A pokemon object that is attacking this pokemon.
        :raises TypeError: If opponent isn't a Charmander, Bulbasaur, Squirtle or MissingNo
        :complexity: Best and worst is O(1) following the update_health() method
        """
        if not isinstance(opponent, PokemonBase):
            # Check if passed parameter opponent is of type PokemonBase
            raise TypeError("The opponent must be a Pokemon object")
        else:
            # Check passed.
            damage = opponent.get_attack_damage() # opponent's attack damage
            if opponent.get_poke_type() == "Fire":
                # Check if opponent is of type Fire. If true, damage to be dealt to this Squirtle object will be halved.
                effective_damage = damage * 0.5
                self.update_health(effective_damage)
            elif opponent.get_poke_type() == "Grass":
                # Check if opponent is of type Grass. If true, damage to be dealt to this Squirtle object will be doubled.
                effective_damage = damage * 2
                self.update_health(float(effective_damage))
            else:
                # Else damage to be dealt to this Squirtle object will remain the same.
                effective_damage = damage * 1
                self.update_health(float(effective_damage))

    def update_health(self, damage: float) -> None:
        """
        Updates the pokemon hp after getting damaged.
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
            # Check if passed parameter damage has a value greater or equal to 0.
            raise ValueError("Damage cannot be a negative value")
        else:
            # If all checks passed.
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
