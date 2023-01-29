import random as rd
rd.seed(3)
class World:
    def __init__(self, nb_lines = 3 , nb_colones = 6 ):
        self.grille = [[0 for _ in range(nb_colones)] for _ in range(nb_lines)]
        
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

    def placer_animal(self):
        if self.grille[self.abscisse][self.ordonnee] == 0:
            self.grille[self.abscisse][self.ordonnee] = self.nom
            
    def deplacer_animal(self, v = 0):
       # je crée une liste pour les voisins vides
        list_voisines_vide = []
        # je gère le bord
        list_abscisse_voisines = [(self.abscisse - 1) % 3, (self.abscisse + 1) % 3 ]
        list_ordonnee_voisines = [(self.ordonnee - 1) % 6, (self.ordonnee + 1) % 6 ]
        # je cherche des voisins vides et je les rajoute sur ma liste
        for elt in list_abscisse_voisines:
            if self.grille[elt][self.ordonnee] == 0:
                list_voisines_vide.append((elt,self.ordonnee))
        for elt in list_ordonnee_voisines:
            if self.grille[self.abscisse][elt] == 0:
                list_voisines_vide.append((self.abscisse,elt)) 
        print(list_voisines_vide)
        # je modifie les coordonnées de l'animal
        if len(list_voisines_vide) > 0:
            self.grille[self.abscisse][self.ordonnee] = v
            (self.abscisse,self.ordonnee) = rd.choice(list_voisines_vide)						
        self.grille[self.abscisse][self.ordonnee] = self.nom
        
class Requin(Animal):
    
	def __init__(self, energie , grille , abscisse: int, ordonnee: int, nom = "R"):
		self.abscisse = abscisse
		self.ordonnee = ordonnee
		self.grille = grille
		self.nom = nom 
		self.energie = energie
    
	def deplacer_requin(self, v=0):
		# je crée 2 listes de voisins (vide et thon)
		list_voisines_thon = [] 
		list_voisines_vides = [] 
   		# je gère le bord
		
		list_abscisse_voisines = [(self.abscisse - 1) % 3, (self.abscisse + 1) % 3 ]
		list_ordonnee_voisines = [(self.ordonnee - 1) % 6, (self.ordonnee + 1) % 6 ]
		
		for elt in list_abscisse_voisines:
			if self.grille[elt][self.ordonnee] == "T" :
				list_voisines_thon.append((elt , self.ordonnee))
			if self.grille[elt][self.ordonnee] == 0 :
				list_voisines_vides.append((elt , self.ordonnee))
		for elt in list_ordonnee_voisines:
			if self.grille[self.abscisse][elt] == "T" :
				list_voisines_thon.append((self.abscisse , elt))
			if self.grille[self.abscisse][elt] == 0 :
				list_voisines_vides.append((self.abscisse , elt))     
        # je modifie les coordonnées de Requin et je lui donne la priorité pour manger un thon que deplacer vers une case vide
		if len(list_voisines_thon) > 0 :
			#self.energie += 2
			self.grille[self.abscisse][self.ordonnee] = v 
			(self.abscisse , self.ordonnee) = rd.choice(list_voisines_thon) 
			self.grille[self.abscisse][self.ordonnee] = self.nom
			#print("energie de requin ", self.energie)
		else:
			if len(list_voisines_vides) > 0 :
			#self.energie -= 1
				self.grille[self.abscisse][self.ordonnee] = v # if self.energie > 0 else 0
				(self.abscisse, self.ordonnee) = rd.choice(list_voisines_vides)
				self.grille[self.abscisse][self.ordonnee] = self.nom
			#print("energie de requin ", self.energie)
		#else:
		#	self.energie -= 1
		#	print("energie de requin ", self.energie)
		#if self.energie <= 0:
		#	self.grille[self.abscisse][self.ordonnee] = 0
		#self.grille[self.abscisse][self.ordonnee] = self.nom
              
####################################################################################################             
ma_grille = World()
# je stoque les thons et les requins
list_thon = []
list_requin = []
# je lance aléa 2 thons dans le grille vide
for _ in range(2):
    x = rd.randint(0,2)
    y = rd.randint(0,5)
    while ma_grille.grille[x][y] !=0:
        x = rd.randint(0,2)
        y = rd.randint(0,5)  
    thon = Animal(ma_grille.grille, x  , y ,"T")
    thon.placer_animal()
    list_thon.append(thon)
# je mets aléa un requin
for _ in range(2):
    x = rd.randint(0,2)
    y = rd.randint(0,5)
    while ma_grille.grille[x][y] !=0:
        x = rd.randint(0,2)
        y = rd.randint(0,5) 
    requin = Requin(3, ma_grille.grille, x , y ,"R")
    requin.placer_animal()
    list_requin.append(requin)
ma_grille.affiche_grille()          
############################################################################
# je fais la boucle for pour parcourir et je crée un compteur d'actions pour la reproduction
compteur_action = 0
for _ in range(8): 
	compteur_action += 1
	if compteur_action <= 10 :
		for elt in list_requin :
			elt.deplacer_requin(0) 
	else : 
		for elt in list_requin :
			elt.deplacer_requin("R")
	if compteur_action <= 10 :
		for elt in list_thon:   
			elt.deplacer_animal(0)  
	else :
		for elt in list_thon: 
			elt.deplacer_animal("T") 
			compteur_action = 0
	ma_grille.affiche_grille()
	print("compteur action", compteur_action)

# il me reste de faire fonctionner l'energie de requin.
