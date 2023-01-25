class World:
    def __init__(self, nb_lines = 10 , nb_colones = 10):
        self.grille = [[0 for _ in range(nb_lines)] for _ in range(nb_colones)]
        
    def affiche_grille(self):
        for line in self.grille:
            for elt in line:
                print(elt, end='\t')
            print()
        
ma_grille = World()
#ma_grille.affiche_grille()