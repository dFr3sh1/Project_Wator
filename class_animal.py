from Class_Grille import  ma_grille

import random

# #Obtenir le contenu de la case du nord :
# def north_case(grid, x, y):
#     # if y == 0:
#     #     return grid[-1][x]
#     # else:
#         return grid[y-1][x]

# print(north_case(ma_grille.grille, 1, 0))


class Animal:
    
    def __init__(self, nom, grid):
        self.nom = nom
        self.grid = grid
        
    def placer_animal(self,):
        x = random.randint(0, len(self.grid.grille)-1)
        y = random.randint(0, len(self.grid.grille[0])-1)
        while self.grid.grille[x][y]!= 0 :
            x = random.randint(0, len(self.grid.grille)-1)
            y = random.randint(0, len(self.grid.grille[0])-1)
        self.grid.grille[x][y] = self.nom
        
    def mouving_animal(self,):
      
      pass


thon = Animal("T", ma_grille)
requin = Animal("S", ma_grille)
for animal in range (20):
  thon.placer_animal()
for animal in range (10):
  requin.placer_animal()


ma_grille.affiche_grille()