__author__ = "Kenneth Vun, Raunaq Nawar, Prateek Tripathi, Muhammad Abdullah Akif"

from array_sorted_list import ArraySortedList
from pokemon import Charmander
from pokemon import Bulbasaur
from pokemon import Squirtle
from pokemon import GlitchMon
from queue_adt import CircularQueue
from sorted_list import ListItem
from stack_adt import ArrayStack


class PokeTeam:
    """
        Class created to assemble the Pokemon Team.
        Several constraints are also introduced for users to
        consider while creating a team.
    """
    LIMIT = 6       #All teams can only have a maximum of 6
    GLITCHMON_LIMIT = 1     #limit for the new mysterious pokemon
    def __init__(self, name: str):  #Initializes 'battle_mode', 'name' and 'team' for 'self'
        """Receives a string input to give the pokemon a name."""
        self.battle_mode = 0    #sets the 'self.battle_mode' to 0
        self.name = name        #sets the 'self.name' to the input in paramater 'name'
        self.team = None        #sets 'self.team' as None
        self.criterion = None   #sets 'self.criterion' as None
        
    def choose_team(self, battle_mode: int, criterion: str = None):     #accepts input for 'battle_mode' and 'criterion' for 'self'
        """
            First receives an int input for battle_mode to be passed
            through an 'if' condition to check if the user gives an
            input matching a given constraint, otherwise ValueError
            will be raised.

            If it passes, a message will be printed and prompts the
            user to input 3 int values separated by an empty space
            and taken as c,b and s. Another 'if' condition will check
            if the sum of c+b+s exceeds the limit of 6. If not, the user
            will be prompted again to input 3 int values again, and this
            will continue until the limit is not exceeded.

            Lastly, it will then call the 'assign_team' function using
            c, b and s as its input parameters.

            :pre: battle_mode input within 0-2
            :raises ValueError: if battle_mode input not within 0-2
            :complexity:O(n)
        """
        self.criterion = criterion          #sets self.criterion as input criterion
        self.battle_mode = battle_mode      #sets self.battle_mode as input battlemode
        if battle_mode not in [0, 1, 2]:    #checks if input value doesn't match the given range of 0 to 2
            raise ValueError("invalid value")   #raises ValueError if conditions are met
        print("Howdy Trainer! Choose your team as C B S")
        print("where C is the number of Charmanders")
        print("      B is the number of Bulbasaurs")
        print("      S is the number of Squirtles")
        c, b, s, g = input().split()            #accepts input separated with ""
        a = int(c) + int(b) + int(s) + int(g)   #'a' as sum total of c+b+s+g
        b = int(g)                              #'b' represents input g
        while (int(a) > int(self.LIMIT) or int(b) > int(self.GLITCHMON_LIMIT)): #checks that 'while' 'a' or 'b' exceeds the respective limit, prompts the user again until a does not exceed it
            print("Howdy Trainer! Choose your team as C B S")
            print("where C is the number of Charmanders")
            print("      B is the number of Bulbasaurs")
            print("      S is the number of Squirtles")
            c, b, s, g = input().split()
            a = int(c) + int(b) + int(s) + int(g)
        PokeTeam.assign_team(self, int(c), int(b), int(s), int(g)) #provides the 'assign_team' function with c, b, and s input for 'self'
                        
    def assign_team(self, charm: int, bulb:int, squir: int, glitch: int):
        """
            Will receive 3 int inputs to 'push' a specific number of
            Charmanders, Bulbasaurs or Squirtles into the ArrayStack
            labeled 'team'. These Pokemon will be pushed depending on
            the respective int values.

            :pre: sum of int input for charm+bulb+squir <= 6
            :complexity:O(n)
        """
        if self.battle_mode == 0:   #checks if 'self.battle_mode' is given the value 0
            self.team = ArrayStack(charm + bulb + squir + glitch) #sets 'self.team' as an Arraystack of a size equivalent to sum total of charm+bulb+squir+glitch
            c1 = Charmander()
            b1 = Bulbasaur()
            s1 = Squirtle()
            g1 = GlitchMon()
            
            for l in range(glitch): #pushes g1 into the stack for 'glitch' times
                self.team.push(g1)
            for k in range(squir):  #pushes s1 into the stack for 'squir' times
                self.team.push(s1)
            for j in range(bulb):   #pushes b1 into the stack for 'bulb' times
                self.team.push(b1)
            for i in range(charm):  #pushes c1 into the stack for 'charm' times
                self.team.push(c1)
        elif self.battle_mode == 1: #checks if battle_mode = 1
            self.team = CircularQueue(charm + bulb + squir + glitch)    #gives CircularQueue the size equivalent to the sum total of charm+bulb+squir+glitch
            c1 = Charmander()
            b1 = Bulbasaur()
            s1 = Squirtle()
            g1 = GlitchMon()
            
            for i in range(charm):      #appends charmanders for 'charm' times
                self.team.append(c1)
            for j in range(bulb):       #appends bulbasaurs for 'bulb' times
                self.team.append(b1)
            for k in range(squir):      #appends squirtles for 'squir' times
                self.team.append(s1)
            for l in range(glitch):     #appends glitchmons for 'glitch' times
                self.team.append(g1)
        elif self.battle_mode == 2: #checks if batlle_mode = 2
            self.team = ArraySortedList(charm + bulb + squir + glitch)  #gives ArraySortedList the size equivalent to sum total of charm+bulb+squir+glitch
            c1 = Charmander()
            b1 = Bulbasaur()
            s1 = Squirtle()
            item = ""
            
            for k in range(squir):  #for squirtles            
                if self.criterion == "lvl":
                    item = ListItem(s1, s1.get_level()) #inserts the pokemon level inside the list
                elif self.criterion == "hp":
                    item = ListItem(s1, s1.get_hp())    #inserts the pokemon hp inside the list
                elif self.criterion == "attack":        
                    item = ListItem(s1, s1.get_attack())    #inserts the pokemon attack power inside the list
                elif self.criterion == "def":           
                    item = ListItem(s1, s1.get_defence())   #inserts the pokemon defence inside the list
                elif self.criterion == "speed":
                    if s1.get_speed() == self.team.__getitem__(len(self.team)-1):
                        item = ListItem(s1, s1.get_speed()) #inserts the pokemon speed inside the list
                    else:
                        item = ListItem(s1, s1.get_speed())
                self.team.add(item) #adds the pokemon along with its info into the array
            for j in range(bulb):   #for bulbasaurs
                if self.criterion == "lvl": 
                    item = ListItem(b1, b1.get_level()) #inserts the pokemon level inside the list
                elif self.criterion == "hp":
                    item = ListItem(b1, b1.get_hp())    #inserts the pokemon hp inside the list
                elif self.criterion == "attack":
                    item = ListItem(b1, b1.get_attack())    #inserts the pokemon attack power inside the list
                elif self.criterion == "def":
                    item = ListItem(b1, b1.get_defence())   #inserts the pokemon defence inside the list
                elif self.criterion == "speed":
                    item = ListItem(b1, b1.get_speed()) #inserts the pokemon speed inside the list
                self.team.add(item) #adds the pokemon along with its info into the array
            for i in range(charm):  #for charmanders
                if self.criterion == "lvl": 
                    item = ListItem(c1, c1.get_level()) #inserts the pokemon level inside the list
                elif self.criterion == "hp":
                    item = ListItem(c1, c1.get_hp())    #inserts the pokemon hp inside the list
                elif self.criterion == "attack":
                    item = ListItem(c1, c1.get_attack())    #inserts the pokemon attack power inside the list
                elif self.criterion == "def":
                    item = ListItem(c1, c1.get_defence())   #inserts the pokemon defence inside the list
                elif self.criterion == "speed":
                    item = ListItem(c1, c1.get_speed()) #inserts the pokemon speed inside the list
                self.team.add(item) #adds the pokemon along with its info into the array

    def __str__(self) -> str:
        return str(self.team)
        
if __name__ == "__main__":
    t1 = PokeTeam("Abdullah")
    a = t1.choose_team(2, None)
    print (a)
