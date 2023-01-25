import random as rd

class World:
    def __init__(self, nb_lines = 10 , nb_colones = 10):
        self.grille = [[0 for _ in range(nb_lines)] for _ in range(nb_colones)]
        
    def affiche_grille(self):
        for elt in self.grille:
            print(elt)
        print()
    
    
        



class Animal:
    def __init__(self, grille , abscisse: int, ordonnee: int, nom):
      self.abscisse = abscisse
      self.ordonnee = ordonnee
      self.grille = grille
      self.nom = nom 

    def placer_animal(self):
        self.grille[self.abscisse][self.ordonnee] = self.nom
        
        
    def deplacer_animal(self):
        list_abscisse_voisines_vide = []
        list_ordonnee_voisines_vide = []
        list_abscisse_voisines = [self.abscisse + 1, self.abscisse - 1 ]
        list_ordonnee_voisines = [self.ordonnee + 1, self.ordonnee - 1 ]
        
        
        for elt in list_abscisse_voisines:
            if self.grille[elt][self.ordonnee] == 0:
              list_abscisse_voisines_vide.append(elt)
        for elt in list_ordonnee_voisines:
            if self.grille[self.abscisse][elt] == 0:
              list_ordonnee_voisines_vide.append(elt)     
              
              
        self.grille[self.abscisse][self.ordonnee] = "R"  
         
        # modifie les coordonnées de l'animal
        if len(list_abscisse_voisines_vide) > 0:
            self.abscisse = rd.choice(list_abscisse_voisines_vide)
        elif len(list_ordonnee_voisines_vide)>0 : 
            self.ordonnee = rd.choice(list_ordonnee_voisines_vide)
        self.grille[self.abscisse][self.ordonnee] = self.nom
        #self.ordonnee = rd.choice(list_ordonnee_voisines_vide)
        
        
        
        
        
                
        
        
 
         
ma_grille = World()
thon = Animal(ma_grille.grille, 5 , 5 ,"T")
thon.placer_animal()
thon.deplacer_animal()
ma_grille.affiche_grille()