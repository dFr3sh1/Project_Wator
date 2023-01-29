import random as rd

class Grid:

    def __init__(self,x_len,y_len):
        self.x_len = x_len  # Hauteur (commence en haut à 0) le nombre de liste
        self.y_len = y_len  # Largeur (commence à gauche à 0) le nombre d'élement dans chaque liste
        self.grid = self.create_grid()

    # Method to create the board
    def create_grid(self)->list:
        
        grid=[]
        row = []
        
        for j in range(self.y_len):
            row.append("O")
        
        for i in range(self.x_len):
            grid.append(row.copy())
        
        return grid
    
    # Method to update the grid for each tour

    def update(self,fish_list,shark_list):
        
        self.grid = self.create_grid()

        for fish in fish_list:
            self.grid[fish.x][fish.y] = "F"

        for shark in shark_list:
            self.grid[shark.x][shark.y] = "S"

    def __repr__ (self):

        display_grid = " "
        for line in range(self.x_len):
            display_grid += "\n" 
            for column in range(self.y_len):
                display_grid += " " +self.grid[line][column]+ " "
        return display_grid

class Fish:

    nmb_of_rounds_for_reproduction = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.old_x = x
        self.old_y = y

        self.counter = 0
        
    def reproduction(self, baby_list, fish_class):
        if self.counter == self.nmb_of_rounds_for_reproduction:
            # new baby fish
            baby = fish_class(self.old_x, self.old_y)
            
            baby_list.append(baby)
            
            self.counter = 0
            
    def pick_target_and_move(self, neighbor_list):
        target = rd.choice(neighbor_list)
        # Make move the shark to this target
        self.old_x = self.x
        self.old_y = self.y
        
        self.x = target[0]
        self.y = target[1]
        
    # Method for finding empty cells around
    def neighbor_coord (self,grid):
        
        up = (self.x-1,self.y) if self.x !=0 else (grid.x_len-1,self.y) 
        
        down = (self.x+1,self.y) if self.x !=grid.x_len-1 else (0,self.y)

        left = (self.x,self.y-1) if self.y !=0 else (self.x,grid.y_len-1)
        
        right = (self.x,self.y+1) if self.y !=grid.y_len-1 else (self.x,0)
        
        
        neighbor_coord_dictionary = {
            "up":up,
            "down":down,
            "right":right,
            "left":left
        }
        return neighbor_coord_dictionary
        
        # Method to move animals
    def move(self,grid,baby_fish_list):

            # A turn takes place for shark
            self.counter += 1

            # Looking for neighbot coordinates
            neighbor_coord_dict = self.neighbor_coord(grid)


            # sorting of neighbor coord in whether fill or empty cells
            empty_cells_list = []


            for i , j in neighbor_coord_dict.values():
                if grid.grid[i][j] == "O":
                    empty_cells_list.append((i,j))

            if len(empty_cells_list)>0:
                
                self.pick_target_and_move(empty_cells_list)
                
                # Animal reproduction
                self.reproduction(baby_fish_list, Fish)

class Shark(Fish):
    
    energy_by_fish = 0
    start_energy = 0
        
    def __init__(self,x,y):
        super().__init__(x,y)

        self.energy = self.start_energy
    
    def eat(self, fish_list):
    # Increase/Decresae shark energy
        self.energy += self.energy_by_fish
        
    # Take the target out of the list
        for fish in fish_list:
            if fish.x == self.x and fish.y == self.y:
                fish_list.remove(fish)
    
    def death(self, shark_list):
        if self.energy == 0:
            shark_list.remove(self)
    
    def move(self, grid:Grid, fish_list, baby_shark_list, shark_list):
        
        # A round takes places for shark, get old and looses energy
        self.counter+=1
        self.energy -+1
        
        # Looking for neighbor coordinates
        neighbor_coord_dict = self.neighbor_coord(grid)
        
        # sorting of neighbor coord in whether fill or empty cells
        cell_fish_list = []
        empty_cells_list = []
        
        for i , j in neighbor_coord_dict.values():
            if grid.grid[i][j] == "F":
                cell_fish_list.append((i,j))
            elif grid.grid[i][j] == "O":
                empty_cells_list.append((i,j))
                
        ########### If one of the nieghbors is a fish
        if len(cell_fish_list)>0:
        # Choice one of neighbors as a target
            self.pick_target_and_move(cell_fish_list)
            
        # Increase/Decresae shark energy
            self.eat(fish_list)
            
            self.reproduction(baby_shark_list, Shark)
            
        elif len(empty_cells_list)>0:
            
        #Move to empy cell
            self.pick_target_and_move(empty_cells_list)
            
        # Shark dies
            self.death(shark_list)
        
        # Shark reproduces
            self.reproduction(baby_shark_list, Shark)
        
        else:
            self.death(shark_list)
            
import random as rd


def create_animal_lists(x_len,y_len,fish_number,shark_number):
    my_set = set()
    while len(my_set) < fish_number + shark_number:
        x = rd.randint(0,x_len - 1)
        y = rd.randint(0,y_len - 1)
        coord = (x,y)
        my_set.add(coord)


    fish_list = []
    shark_list = []
    
    for coord in list(my_set)[0 : fish_number]:
        fish_list.append(Fish(coord[0],coord[1]))

    for coord in list(my_set)[fish_number :  ]:
        shark_list.append( Shark(coord[0],coord[1]))

    return fish_list, shark_list


# print(len(list(my_set)[fish_number : len(my_set)]))