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
    
    def __init__(self, nom):
        self.nom = nom
        
    def placer_animal(self, grid):
        x = random.randint(0, len(grid.grille)-1)
        y = random.randint(0, len(grid.grille[0])-1)
        while grid.grille[x][y]!= 0 :
            x = random.randint(0, len(grid.grille)-1)
            y = random.randint(0, len(grid.grille[0])-1)
        grid.grille[x][y] = self.nom


thon = Animal("T")
requin = Animal("S")
for animal in range (20):
  thon.placer_animal(ma_grille)
for animal in range (10):
  requin.placer_animal(ma_grille)


ma_grille.affiche_grille()