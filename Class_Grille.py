class World:
    def __init__(self, nb_lines = 10 , nb_colones = 10):
        self.grille = [[0 for _ in range(nb_lines)] for _ in range(nb_colones)]
        
    def affiche_grille(self):
        for elt in self.grille:
            print(elt)
        print()
        
ma_grille = World()
print(ma_grille.affiche_grille())