__author__ = "Kenneth Vun, Raunaq Nawar, Prateek Tripathi, Muhammad Abdullah Akif"

from abc import ABC, abstractmethod

class PokemonBase(ABC):
    # An example of a base value for a stat
    # BASE_LEVEL = 1
    """
        Abstract class PokemonBase with three variables hp, level,
        and poke_type. The user will provide the hp and poke_type
        while creating the object, and various methods are added
        to provide the functionality to the class.
    """
    def __init__(self, hp: int, poke_type: str):    #Initializes the HP and type of the pokemon
        """
            Receives int value for hp and string for poke_type
        """
        self.hp = hp			#sets 'self.hp' to hp  
        self.poke_type = poke_type      #sets 'self.poke_type' to poke_type
        self.level = 1                  #sets 'self.level' to 1
 
    def get_hp(self):		#provides the pokemon’s HP
        """returns the hp for a pokemon"""
        return self.hp          #returns self.hp
  
    def set_hp(self, hp):	#sets the hp for 'self'
        """sets the hp of a pokemon"""
        self.hp = hp            #sets 'self.hp' to parameter hp
 
    def get_level(self):	#provides the level of the pokemon
        """returns the level of a pokemon"""
        return self.level       #sets 'self.level'
 
    def get_poke_type(self):		#provides the type of the pokemon
        """returns the pokemon's type"""
        return self.poke_type
 
    def is_fainted(self):		#checks if the pokemon has fainted
        """returns True if hp of the pokemon <= 0

           :pre: stack is not empty
           :complexity: O(1)
        """
        if self.hp <= 0:
            return True
        else:
            return False
 
    def level_up(self):		#increments the pokemon’s level
        """increments the level of the pokemon"""
        self.level += 1
 
    @abstractmethod		#indicates the method below is abstract and not implemented.
    def get_speed(self):	#obtains the speed of the pokemon
        """obtains the speed of the pokemon"""
        pass
 
    @abstractmethod
    def get_attack(self):	#obtains the attack power of the pokemon
        """obtains the attack power of the pokemon"""
        pass
 
    @abstractmethod
    def get_defence(self):	#obtains the defence of the pokemon
        """obtains the defence of the pokemon"""
        pass
 
    @abstractmethod
    def damage(self, damage: int):	#calculates the damage the pokemon receives
        """calculates the damage received by the pokrmon"""
        pass
 
    def get_poke_name(self):	    #obtains the name of the pokemon
        """obtains the name of the pokemon"""
        self.NAME
 
    def __str__(self):		#prints the string statement
        return "{}'s HP = {} and level = {}" .format(self.NAME, self.hp, self.level)
