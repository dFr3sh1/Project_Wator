from classes import Shark, Fish, Grid
import random as rd

class Game:
    def _init_(self, x_len, y_len, fish_number, shark_number, shark_nmb_of_rounds_for_reproduction, fish_nmb_of_rounds_for_reproduction, energy_by_fish, start_energy):
        self.x_len = x_len
        self.y_len = y_len
        self.fish_number = fish_number
        self.shark_number = shark_number
        self.fish_nmb_of_rounds_for_reproduction = fish_nmb_of_rounds_for_reproduction
        self.shark_nmb_of_rounds_for_reproduction = shark_nmb_of_rounds_for_reproduction
        self.energy_by_fish = energy_by_fish
        self.start_energy = start_energy
        self.my_grid = Grid(x_len, y_len)
        
    def create_animal_list(self):
        my_set = set()
        while len(my_set) < self.fish_number + self.shark_number:
            x = rd.randint(0, self.x_len-1)
            y = rd.randint(0, self.y_len-1)
            coord = (x, y)
            my_set.add(coord)
            
            
            self.fish_list = []
            self.shark_list = []
            
            
            for coord in list(my_set)[0, self.fish_number]:
                self.fish_list.append( Fish(coord[0], coord[1]))
                
            for coord in list(my_set)[self.fish_number : ]:
                self.shark_list.append( Shark(coord[0], coord[1]))
                
    def game_initialisation(self):
        Shark.nmb_of_rounds_for_reproduction = self.shark_nmb_of_rounds_for_reproduction
        Shark.energy_by_fish = self.energy_by_fish
        Shark.start_energy = self.start_energy
        Fish.nmb_of_rounds_for_reproduction = self.fish_nmb_of_rounds_for_reproduction
        
        self.create_animal_list()
        
        self.my_grid.update(self.fish_list, self.shark_list)
        
        print("----Initialisation -----")
        print("Sharks", len(self.shark_list))
        print("Fishes", len(self.fish_list))
        print(self.my_grid)
        
    def game_start(self):
        self.game_initialisation()
        
        
    
    #####################THE ROUNDS
        game_playing = True
        
        self.round_nb = 0
        while game_playing:
            
            baby_shark_list = []
            for shark in self.shark_list:
                shark.move(self.my_grid,self.fish_list, baby_shark_list, self.shark_list)
                jonction_shark = self.shark_list + baby_shark_list
                self.my_grid.update(self.fish_list,jonction_shark)
                
            self.shark_list.extend(baby_shark_list)
            
            baby_fish_list=[]
            for fish in self.fish_list:  
                fish.move(self.my_grid, baby_fish_list)
                jonction_fish = self.fish_list + baby_fish_list
                self.my_grid.update(jonction_fish, self.fish_list)
                
            self.fish_list.extend(baby_fish_list)
            
            self.round_nb +=1
            print("------ Round n -------", self.round_nb)
            print(self.my_grid)
            ### End game analysis:

            if len(self.fish_list) == 0:
                print("Tous les poissons sont morts, le jeu est fini")
                print (" Tour ", self.round_nb)
                game_playing = False
            elif len(self.shark_list) == 0:
                print("Tous les requins sont morts")
                print (" Tour ", self.round_nb)
                game_playing = False
            elif self.round_nb == 150:
                print("Vous avez atteint le tour 150, cest un bel équilibre")
                game_playing = False