import random as rd

class World:
    def __init__(self, nb_lines = 10 , nb_colones = 10):
        self.grille = [[0 for _ in range(nb_lines)] for _ in range(nb_colones)]
        
    def affiche_grille(self):
        for line in self.grille:
            for elt in line:
                print(elt, end='\t')
            print()
    
    
        



class Animal:
    
    
    def __init__(self, grille , abscisse: int, ordonnee: int, nom):
      self.abscisse = abscisse
      self.ordonnee = ordonnee
      self.grille = grille
      self.nom = nom 
      self.compteur_action = 0

    def placer_animal(self):
        if self.grille[self.abscisse][self.ordonnee] == 0:
            self.grille[self.abscisse][self.ordonnee] = self.nom
        
        
    def deplacer_animal(self):
        list_abscisse_voisines_vide = []
        list_ordonnee_voisines_vide = []
        
        abscisse_droite = self.abscisse + 1
        if abscisse_droite > 9 :
            abscisse_droite = 0
        list_abscisse_voisines = [abscisse_droite, self.abscisse - 1 ]
        ordonnee_bas = self.ordonnee + 1
        if ordonnee_bas > 9 :
             ordonnee_bas = 0
        list_ordonnee_voisines = [ordonnee_bas, self.ordonnee - 1 ]
        
        
        for elt in list_abscisse_voisines:
            if self.grille[elt][self.ordonnee] == 0:
              list_abscisse_voisines_vide.append(elt)
        for elt in list_ordonnee_voisines:
            if self.grille[self.abscisse][elt] == 0:
              list_ordonnee_voisines_vide.append(elt) 
                  
              
              
        self.grille[self.abscisse][self.ordonnee] = 0 
         
        # modifie les coordonnées de l'animal
        if len(list_abscisse_voisines_vide) > 0:
            self.abscisse = rd.choice(list_abscisse_voisines_vide)
        elif len(list_ordonnee_voisines_vide)>0 : 
            self.ordonnee = rd.choice(list_ordonnee_voisines_vide)
        self.compteur_action +=1
        print("compteur action: " ,self.compteur_action)
        self.grille[self.abscisse][self.ordonnee] = self.nom
        
       
        
        
        
        
        
                
        
        
 
         
ma_grille = World()

for _ in range(55):
    x = rd.randint(0,9)
    y = rd.randint(0,9)
    while ma_grille.grille[x][y] !=0:
        x = rd.randint(0,9)
        y = rd.randint(0,9)  
    thon = Animal(ma_grille.grille, x  , y ,"T")
    thon.placer_animal()
    thon.deplacer_animal()
for _ in range(40):
    x = rd.randint(0,9)
    y = rd.randint(0,9)
    while ma_grille.grille[x][y] !=0:
        x = rd.randint(0,9)
        y = rd.randint(0,9) 
    requin = Animal(ma_grille.grille, x , y ,"R")
    requin.placer_animal()
    requin.deplacer_animal()


# thon1 = Animal(ma_grille.grille, 2 , 3 ,"T")
# thon1.placer_animal()
#thon1.deplacer_animal()

ma_grille.affiche_grille()
