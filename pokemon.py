__author__ = "Kenneth Vun, Raunaq Nawar, Prateek Tripathi, Muhammad Abdullah Akif"

import random
from pokemon_base import PokemonBase

class Charmander(PokemonBase):
    """
        Pokemon class to define Charmander
    """
    NAME = "Charmander" #name of the pokemon
    BASE_LEVEL = 1      #base level of the Charmander
    BASE_ATTACK = 6     #base attack of the Charmander
    BASE_DEFENCE = 4    #base defence of the Charmander
    BASE_SPEED = 7      #base speed of the Charmander
    TYPE_EFFECTIVENESS = [1, 0.5, 2]    #Charmanders type effectiveness multiplier
    def __init__(self):     #initializes the HP and type for Charmander
        PokemonBase.__init__(self, 7, "FIRE")
        
    def get_speed(self):                            #provides the speed and its increment for Charmander
        return self.BASE_SPEED + self.get_level()   #returns 'self.BASE_SPEED' after increasing it with 'self.get_level()'

    def get_attack(self):                           #provides the attack stat and its increment for Charmander
        return self.BASE_ATTACK + self.get_level()  #returns 'self.BASE_ATTACK' after increasing it with 'self.get_level()'
    
    def get_defence(self):          #provides the defence stat for Charmander
        return self.BASE_DEFENCE    #returns 'self.BASE_DEFENCE'
    
    def damage(self, damage, poke_type):        #provides the damage taken by Charmander
        if damage > int(self.get_defence()):    #checks if damage exceeds Charmander defence
            if poke_type == "FIRE":             #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - damage      #reduces hp by subtracting it with damage
            elif poke_type == "GRASS":                                      #checks if the attacking pokemon is a GRASS type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[1])   #reduces hp by subtracting it with damage*type_effectiveness
            elif poke_type == "WATER":                                      #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[2])   #reduces hp by subtracting it with damage*type_effectiveness
        else:
            if poke_type == "FIRE":                                             #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - (damage//2)                                 #reduces hp by subtracting it with damage//2
            elif poke_type == "GRASS":                                          #checks if the attacking pokemon is a GRASS type                               
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[1])//2)  #reduces hp by subtracting it with damage*type_effectiveness//2
            elif poke_type == "WATER":                                          #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[2])//2)  #reduces hp by subtracting it with damage*type_effectiveness//2

class Bulbasaur(PokemonBase):
    """
        Pokemon class to define Bulbasaur
    """
    NAME = "Bulbasaur"  #name of the pokemon
    BASE_LEVEL = 1      #base level of the Bulbasaur
    BASE_ATTACK = 5     #base attack of the Bulbasaur
    BASE_DEFENCE = 5    #base defence of the Bulbasaur
    BASE_SPEED = 7      #base speed of the Bulbasaur
    TYPE_EFFECTIVENESS = [0.5, 2, 1]    #Bulbasaur type effectiveness multiplier
    def __init__(self):     #initializes the HP and type for Bulbasaur
        PokemonBase.__init__(self, 9, "GRASS")
        
    def get_speed(self):                                #provides the speed and its increment for Bulbasaur
        return self.BASE_SPEED + (self.get_level()//2)  #returns 'self.BASE_SPEED' after increasing it with 'self.get_level()'//2

    def get_attack(self):       #provides the attack stat for Bulbasaur
        return self.BASE_ATTACK #returns 'self.BASE_ATTACK'
    
    def get_defence(self):          #provides the defence stat for Bulbasaur
        return self.BASE_DEFENCE    #returns 'self.BASE_DEFENCE'
    
    def damage(self, damage, poke_type):            #provides the damage taken by Bulbasaur
        if damage > (int(self.get_defence()) + 5):  #checks if damage exceeds Bulbasaur defence+5
            if poke_type == "FIRE":                 #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[1])   #reduces hp by subtracting it with damage*type_effectiveness
            elif poke_type == "GRASS":                                      #checks if the attacking pokemon is a GRASS type
                self.hp = self.hp - damage                                  #reduces hp by subtracting it with damage
            elif poke_type == "WATER":                                      #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[0])   #reduces hp by subtracting it with damage*type_effectiveness
            elif poke_type == "NEUTRAL":        #checks if the attacking pokemon is a NEUTRAL type
                self.hp = self.hp - damage      #reduces hp by subtracting it with damage
        else:
            if poke_type == "FIRE":                                             #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[1])//2)  #reduces hp by subtracting it with damage*type_effectiveness//2
            elif poke_type == "GRASS":                                          #checks if the attacking pokemon is a GRASS type
                self.hp = self.hp - (damage//2)                                 #reduces hp by subtracting it with damage//2
            elif poke_type == "WATER":                                          #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[0])//2)  #reduces hp by subtracting it with damage*type_effectiveness

class Squirtle(PokemonBase):
    """
        Pokemon class to define Squirtle
    """
    NAME = "Squirtle"		#name of the pokemon
    BASE_LEVEL = 1		#base level of the Squirtle
    BASE_ATTACK = 4		#base attack of the Squirtle
    BASE_DEFENCE = 6		#base defence of the Squirtle
    BASE_SPEED = 7		#base speed of the Squirtle
    TYPE_EFFECTIVENESS = [2, 1, 0.5]    #Squirtle type effectiveness multiplier
    def __init__(self):		#initializes the HP and type for Squirtle
        PokemonBase.__init__(self, 8, "WATER")   
      
    def get_speed(self):		#provides the speed for Squirtle
        return self.BASE_SPEED   #returns 'self.BASE_SPEED'
 
    def get_attack(self):	                        #provides the attack stat and its increment for Squirtle
        return self.BASE_ATTACK + self.get_level()//2    #returns 'self.BASE_ATTACK' after increasing it with 'self.get_level()'//2
    
    def get_defence(self):  			        #provides the defence stat and its increment for Squirtle
        return self.BASE_DEFENCE + self.get_level()      #returns 'self.BASE_DEFENCE' after increasing it with 'self.get_level()'
    
    def damage(self, damage, poke_type):        #provides the damage taken by Squirtle
        if damage > (int(self.get_defence()) * 2):  #checks if damage exceeds Squirtle defence*2
            if poke_type == "FIRE":                                         #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[2])   #reduces hp by subtracting it with damage*type_effectiveness
            elif poke_type == "GRASS":                                      #checks if the attacking pokemon is a GRASS type
                self.hp = self.hp - ((damage)*self.TYPE_EFFECTIVENESS[0])   #reduces hp by subtracting it with damage*type_effectiveness
            elif poke_type == "Water":                                      #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - damage                                  #reduces hp by subtracting it with damage
            elif poke_type == "NEUTRAL":    #checks if the attacking pokemon is a NEUTTRAL type
                self.hp = self.hp - damage  #reduces hp by subtracting it with damage
        else:
            if poke_type == "FIRE":                                             #checks if the attacking pokemon is a FIRE type
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[2])//2)  #reduces hp by subtracting it with damage*type_effectiveness//2
            elif poke_type == "GRASS":                                          #checks if the attacking pokemon is a GRASS type
                self.hp = self.hp - (((damage)*self.TYPE_EFFECTIVENESS[0])//2)  #reduces hp by subtracting it with damage*type_effectiveness//2
            elif poke_type == "WATER":                                          #checks if the attacking pokemon is a WATER type
                self.hp = self.hp - (damage//2)                                 #reduces hp by subtracting it with damage
            
class GlitchMon(PokemonBase):
    """
        Pokemon class to define GlitchMon
    """
    NAME = "MissingNo"  #name of the pokemon
    BASE_LEVEL = 1      #base level of the MissingNo
    BASE_ATTACK = 5     #base attack of the MissingNo
    BASE_DEFENCE = 5    #base defence of the MissingNo
    BASE_SPEED = 7      #base speed of the MissingNo
    TYPE_EFFECTIVENESS = [1, 1, 1]  #MissingNo type effectiveness multiplier
    def __init__(self):     #initializes the HP and type for MissingNo
        PokemonBase.__init__(self, 8, "NEUTRAL")
        
    def get_speed(self):    #provides the speed for GlitchMon
        x = 0
        if self.level > 1:  #checks if level of GlitchMon is > 1
            x = self.level - 1
        return self.BASE_SPEED + x  #returns GlitchMon speed + (level - 1)

    def get_attack(self):   #provides the attack power for GlitchMon
        x = 0
        if self.level > 1:  #checks if level of GlitchMon is > 1
            x = self.level - 1
        return self.BASE_ATTACK + x #returns GlitchMon attack power + (level - 1)
            
    def get_defence(self):  #provides defence of GlitchMon
        x = 0
        if self.level > 1:  #checks if level of GlitchMon is > 1
            x = self.level - 1
        return self.BASE_DEFENCE + x    #returns GlitchMon defence + (level - 1)
    
    def damage(self, damage, poke_type):    #provides the damage taken by GlitchMon
        """when attacked, will have a chance to gain a random superpower"""
        list = []
        list = range(1,5)
        choice = random.choice(list)
        if choice == 3:
            self.superpower()       #provides a superpower 
        self.hp = self.hp - damage  #reduces hp by subtracting it with damage
            
    def increase_hp(self, hp):  #increases hp
        self.hp += hp           
        
    def superpower(self):
        """Provides GlitchMon with superpowers"""
        superpower_list = ["level", "hp", "level&hp"]
        choice = random.choice(superpower_list)
        if choice == "level":   #increases level by 1
            self.level += 1
        elif choice == "hp":    #increases hp by 1
            self.hp += 1
        elif choice == "level&hp":  #increases both level and hp by 1
            self.level += 1
            self.hp += 1
