__author__ = "Muhammad Abdullah Akif, Kenneth Vun, Raunaq Nawar, Prateek Tripathi"

from poke_team import PokeTeam
 
class Battle:
    def __init__(self, trainer_one_name: str, trainer_two_name: str):   #initializes the 2 Pokemon trainers in the battle
        self.team1 = PokeTeam(trainer_one_name)     #provides the name for the trainer in the first team
        self.team2 = PokeTeam(trainer_two_name)     #provides the name for the trainer in the seconds team
        self.battle_mode = None         #battle_mode set to None
      
    def set_mode_battle(self) -> str:       #receives user input and sets up a battle order
        """
            Sets up a battle between two teams of pokemon where pokemons fight until
            they faint.

            :pre: both stacks are not empty
            :post: One or more stacks are empty
            :Time complexity:O(n^3)
        """
        self.team1.choose_team(0, None)     #calling 'choose_team' function using the given input 
        self.team2.choose_team(0, None)
        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:  #checks if any one of the teams are empty
            a1 = self.team1.team.pop()      #selects the pokemon of the last index in team1
            a2 = self.team2.team.pop()      #selects the pokemon of the last index in team2
          
            if a1.get_speed() > a2.get_speed():                     #checks if pokemon a1 is faster than pokemon a2
                a2.damage(a1.get_attack(), a1.get_poke_type())      #calls the damage function for pokemon a2, with input provided by functions get_attack and poke_type for pokemon a1
                if a2.is_fainted() == False:                        #checks if a2 has not fainted
                    a1.damage(a2.get_attack(), a2.get_poke_type())  #if a2 has not fainted, damage function will be called for a1, with input from get_attack and poke_type of a2
            
            elif a1.get_speed() < a2.get_speed():                   #checks if pokemon a2 is faster than pokemon a2
                a1.damage(a2.get_attack(), a2.get_poke_type())      #calls the damage function for a1, with input provided by functions get_attack and poke_type for a2
                if a1.is_fainted() == False:                        #checks if a1 has not fainted
                    a2.damage(a1.get_attack(), a1.get_poke_type())  #if not, damage function will be called for a2, with input from get_attack and poke_type of a1
         
            elif a1.get_speed() == a2.get_speed():                  #checks if a1 and a2 has the same speed
                a1.get_attack()                                     #obtains the attack power of a1
                a2.get_attack()                                     #obtains the attack power of a2
                a1.damage(a2.get_attack(), a2.get_poke_type())      #calls the damage function for a1 with input from functions get_attack and poke_type for a2
                a2.damage(a1.get_attack(), a1.get_poke_type())      #calls the damage function for a2 with input from functions get_attack and poke_type for a1
              
            if a2.is_fainted() == True and a1.is_fainted() == False:    #checks if a2 fainted while a1 hasn't
                a1.level_up()                           #a1 level increases
                if a1.get_poke_name() == "MissingNo":   #checks if the pokemon is GlitchMon
                    a1.increase_hp(1)                   #increases its hp by 1 
                self.team1.team.push(a1)                #pushes a1 into its team array
            elif a1.is_fainted() == True and a2.is_fainted() == False:  #checks if a1 fainted while a2 hasn't
                a2.level_up()                               #a2 level increases
                if a2.get_poke_name() == "MissingNo":       #checks if the pokemon is GlitchMon
                    a2.increase_hp(1)                       #increases its hp by 1 
                self.team2.team.push(a2)                    #pushes a2 into its team array
            elif a1.is_fainted() == False and a2.is_fainted() == False: #checks if both a1 and a2 didn't faint
                a1.set_hp((a1.get_hp())-1)              #decreases current hp of a1 by 1
                if a1.is_fainted() == False:            #checks if a1 did not faint
                    self.team1.team.push(a1)            #pushes a1 back into team array
                elif a1.is_fainted() == True:           #checks if a1 fainted
                    a2.level_up()                       #increases a2 level by 1
                    if a2.get_poke_name() == "MissingNo":   #checks if the pokemon is GlitchMon           
                        a2.increase_hp(1)                   #increases its hp by 1    
                a2.set_hp((a2.get_hp())-1)      #decreases current hp of a2 by 1
                if a2.is_fainted() == False:    #checks if a2 did not faint
                    self.team2.team.push(a2)    #pushes a2 back into team array
                elif a2.is_fainted() == True:   #checks if a2 fainted
                    a1.level_up()               #increases a1 level by 1
                    if a1.get_poke_name() == "MissingNo":   #checks if the pokemon is GlitchMon 
                       a1.increase_hp(1)    #increases its hp by 1        
                  
        if self.team1.team.is_empty() == False and self.team2.team.is_empty() == True:      #checks if team1 array isn't empty while team2 array is empty
            return self.team1.name                                                          #returns the output of the name function for team1
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == False:    #checks if team2 array isn't empty while team1 array is empty
            return self.team2.name                                                          #returns the output of the name function for team2
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == True:     #checks if both team1 and team2 arrays are empty
            return "Draw"                                                                   #returns string "Draw"
   
    def rotating_mode_battle(self) -> str:          #asks user input to set up rotating battle mode
        """
            Sets up a battle where each pokemon fights one round then returns
            to their team.

            :pre: both queue are not empty
            :post: One or more queues are empty
            :Time Complexity:O(n^3)
        """
        self.team1.choose_team(1, None)             #sets battle_mode as 1 and criterion as None for team1
        self.team2.choose_team(1, None)             #sets battle_mode as 1 and criterion as None for team2
        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:      #checks if both team array are not empty
            a1 = self.team1.team.serve()            
            a2 = self.team2.team.serve()
        
            if a1.get_speed() > a2.get_speed():                     #checks if a1 is faster than a2
                a2.damage(a1.get_attack(), a1.get_poke_type())      #calls the damage function for a2, with input provided by functions get_attack and poke_type for a1
                if a2.is_fainted() == False:                        #checks if a2 has not fainted
                    a1.damage(a2.get_attack(), a2.get_poke_type())  #if a2 has not fainted, damage function will be called for a1, with input from get_attack and poke_type of a2
            
            elif a1.get_speed() < a2.get_speed():                   #checks if a2 is faster than a1
                a1.damage(a2.get_attack(), a2.get_poke_type())      #calls the damage function for a1, with input provided by functions get_attack and poke_type for a2
                if a1.is_fainted() == False:                        #checks if a1 has not fainted
                    a2.damage(a1.get_attack(), a1.get_poke_type())  #if a1 has not fainted, damage function will be called for a1, with input from get_attack and poke_type of a1
         
            elif a1.get_speed() == a2.get_speed():              #checks if a1 and a2 has the same speed
                a1.damage(a2.get_attack(), a2.get_poke_type())  #calls the damage function for a1 with input from functions get_attack and poke_type for a2
                a2.damage(a1.get_attack(), a1.get_poke_type())  #calls the damage function for a2 with input from functions get_attack and poke_type for a1
              
            if a2.is_fainted() == True and a1.is_fainted() == False: #checks if a2 fainted while a1 hasn't
                a1.level_up()                            #a1 level increases
                if a1.get_poke_name() == "MissingNo":    #checks if the pokemon is GlitchMon
                    a1.increase_hp(1)                    #increases its hp by 1
                self.team1.team.append(a1)               #appends a1 into the team array
            elif a1.is_fainted() == True and a2.is_fainted() == False:   #checks if a1 fainted while a2 hasn't
                a2.level_up()                            #a2 level increases
                if a2.get_poke_name() == "MissingNo":    #checks if the pokemon is GlitchMon
                    a2.increase_hp(1)                    #increases its hp by 1
                self.team2.team.append(a2)               #appends a2 into the team array
            elif a1.is_fainted() == False and a2.is_fainted() == False:  #checks if both a1 and a2 haven't fainted
                a1.set_hp((a1.get_hp())-1)   #decreases the current hp of a1 by 1
                a2.set_hp((a2.get_hp())-1)   #decreases the current hp of a2 by 1
                if a1.is_fainted() == False and a2.is_fainted() == False:    #checks if both a1 and a2 haven't fainted
                    self.team1.team.append(a1)   #appends a1 into the team array
                    self.team2.team.append(a2)   #appends a2 into the team array
                elif a1.is_fainted() == True and a2.is_fainted() == False:   #checks if a1 fainted while a2 didn't
                    a2.level_up()                            #a2 level increases by 1
                    if a2.get_poke_name() == "MissingNo":    #checks if the pokemon is GlitchMon
                        a2.increase_hp(1)                    #increases its hp by 1
                    self.team2.team.append(a2)               #appends a2 into the team array
                elif a2.is_fainted() == True and a1.is_fainted() == False:   #checks if a2 fainted while a1 didn't
                    a1.level_up()                            #a1 level increases by 1
                    if a1.get_poke_name() == "MissingNo":    #checks if the pokemon is GlitchMon
                        a1.increase_hp(1)                    #increases its hp by 1
                    self.team1.team.append(a1)               #appends a1 into the team array
              
        if self.team1.team.is_empty() == False and self.team2.team.is_empty() == True:      #checks if team1 is not empty while team2 is empty
            return self.team1.name                                                          #returns the output of the name function for team1
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == False:    #checks if team2 is not empty while team1 is empty
            return self.team2.name                                                          #returns the output of the name function for team2
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == True:     #checks if both teams are empty
            return "Draw"                                                                   #returns the string "Draw"
    
    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        """
            Sets up a battle where pokemons in the battle in non-increasing order of
            the chosen attribute by the user

            :pre: both lists are not empty
            :post: One or more lists are empty
            :Time Complexity: O(n^3)
        """
        self.team1.choose_team(2, criterion_team1)  #sets battle_mode as 2 and criterion as criterion_team1 for team1
        self.team2.choose_team(2, criterion_team2)  #sets battle_mode as 2 and criterion as criterion_team2 for team2
        while self.team1.team.is_empty() == False and self.team2.team.is_empty() == False:  #checks if both team1 and team2 are empty #O(n)
            a1 = self.team1.team.__getitem__(0) #retrieves the pokemon of the first index
            self.team1.team.delete_at_index(0)  #deletes the pokemon from the index
            a2 = self.team2.team.__getitem__(0) #retrieves the pokemon of the first index
            self.team2.team.delete_at_index(0)  #deletes the pokemon from the index
            
            if a1.value.get_speed() > a2.value.get_speed():                         #checks if the speed  of a1 > a2
                a2.value.damage(a1.value.get_attack(), a1.value.get_poke_type())    #computes the damage taken by a2
                if a2.value.is_fainted() == False:                                  #checks if a2 didn't faint
                   a1.value.damage(a2.value.get_attack(), a2.value.get_poke_type()) #computes the damage taken by a1
              
            elif a1.value.get_speed() < a2.value.get_speed():                           #checks if the speed  of a1 < a2
                a1.value.damage(a2.value.get_attack(), a2.value.get_poke_type())        #computes the damage taken by a1
                if a1.value.is_fainted() == False:                                      #checks if a1 didn't faint
                   a2.value.damage(a1.value.get_attack(), a1.value.get_poke_type())     #computes the damage taken by a2
           
            elif a1.value.get_speed() == a2.value.get_speed():                      #checks if the speed of a1 == a2
                a1.value.damage(a2.value.get_attack(), a2.value.get_poke_type())    #computes the damage taken by a1
                a2.value.damage(a1.value.get_attack(), a1.value.get_poke_type())    #computes the damage taken by a2
              
            if a2.value.is_fainted() == True and a1.value.is_fainted() == False:    #checks if a2 fainted while a1 didn't
                a1.value.level_up()                             #a1 levels up
                if a1.value.get_poke_name() == "MissingNo":     #checks if a1 is GlitchMon
                       a1.value.increase_hp(1)                  #increases hp by 1
                self.team1.team.add(a1)                         #adds a1 back into the team
            elif a1.value.is_fainted() == True and a2.value.is_fainted() == False:  #checks if a1 fainted while a2 didn't
                a2.value.level_up()                             #a2 levels up
                if a2.value.get_poke_name() == "MissingNo":     #checks if a2 is GlitchMon
                       a2.value.increase_hp(1)                  #increases hp by 1
                self.team2.team.add(a2)                         #adds a2 back into the team
            elif a1.value.is_fainted() == False and a2.value.is_fainted() == False:     #checks if both a1 and a2 didn't faint
                a1.value.set_hp((a1.value.get_hp())-1)      #reduces the hp of a1 by 1
                a2.value.set_hp((a2.value.get_hp())-1)      #reduces the hp of a2 by 1
                if a1.value.is_fainted() == False and a2.value.is_fainted() == False:   #checks if both a1 and a2 didn't faint
                    self.team1.team.add(a1)     #adds a1 back into the team
                    self.team2.team.add(a2)     #adds a2 back into the team
                elif a1.value.is_fainted() == True and a2.value.is_fainted() == False:  #checks if a1 fainted while a2 didn't
                    a2.value.level_up()                         #a2 levels up
                    if a2.value.get_poke_name() == "MissingNo": #checks if a2 is GlitchMon
                           a2.value.increase_hp(1)              #hp increases by 1
                    self.team2.team.add(a2)                     #adds a2 back into the team
                elif a2.value.is_fainted() == True and a1.value.is_fainted() == False:  #checks if a2 fainted while a1 didn't
                    a1.value.level_up()                             #a1 levels up
                    if a1.value.get_poke_name() == "MissingNo":     #checks if a1 is GlitchMon
                           a1.value.increase_hp(1)                  #hp increases by 1
                    self.team1.team.add(a1)                         #adds a1 back into the team
              
        if self.team1.team.is_empty() == False and self.team2.team.is_empty() == True:      #checks if team1 is not empty while team2 is empty
            return self.team1.name                                                          #returns the output of the name function for team1
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == False:    #checks if team2 is not empty while team1 is empty
            return self.team2.name                                                          #returns the output of the name function for team2
        elif self.team1.team.is_empty() == True and self.team2.team.is_empty() == True:     #checks if both teams are empty
            return "Draw"                                                                   #returns the string "Draw"
    

