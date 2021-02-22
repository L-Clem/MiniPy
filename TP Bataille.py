'''
TP Bataille de cartes.
---------------------
Groupe 2, composé de :
  LAFON Clément
  LAUNAY Quentin
  LOGEAIS Ian
  FERRY Hugo
'''



# Importation des modules et méthodes requises :
# ---------------------------------------------


from random import shuffle



# Déclaration des variables et séquences de base du jeu : 
# ------------------------------------------------------


# Liste représantant le paquet de 32 cartes, sous la forme : [ 'Couleur/Famille', ['Valeur litérale', Valeur numérique] ].
paquet = [['Trèfle', ['Sept', 7]], ['Trèfle', ['Huit', 8]], ['Trèfle', ['Neuf', 9]], ['Trèfle', ['Dix', 10]], ['Trèfle', ['Valet', 11]], ['Trèfle', ['Dame', 12]], ['Trèfle', ['Roi', 13]],['Trèfle', ['As', 14]],['Carreau', ['Sept', 7]], ['Carreau', ['Huit', 8]], ['Carreau', ['Neuf', 9]], ['Carreau', ['Dix', 10]], ['Carreau', ['Valet', 11]], ['Carreau', ['Dame', 12]], ['Carreau', ['Roi', 13]], ['Carreau', ['As', 14]],['Coeur', ['Sept', 7]], ['Coeur', ['Huit', 8]], ['Coeur', ['Neuf', 9]], ['Coeur', ['Dix', 10]], ['Coeur', ['Valet', 11]], ['Coeur', ['Dame', 12]], ['Coeur', ['Roi', 13]],['Coeur', ['As', 14]],['Pique', ['Sept', 7]], ['Pique', ['Huit', 8]], ['Pique', ['Neuf', 9]], ['Pique', ['Dix', 10]], ['Pique', ['Valet', 11]], ['Pique', ['Dame', 12]], ['Pique', ['Roi', 13]],['Pique', ['As', 14]]]

# La liste tas représente les cartes joués lors d'une bataille (en cas d'égalité de valeur).
tas = [] 



# Phase de mélange et de distribution du paquet :
# ----------------------------------------------


# Mélange le paquet
shuffle(paquet)

# Assigne la première moitié du paquet au joueur A.
main_a = paquet[0:16]

# Assigne la seconde moitié du paquet au joueur B.
main_b = paquet [16:32]



# Definition des fonctions :
# -------------------------


# La fonction bataille() permet de verifier si une bataille vient de se terminer.
def bataille(x) :
  # Si le tas est supérieur à 0 alors cela veut dire qu'une bataille vient de se terminer. Sinon c'est qu'au tour précédent il n'y a pas eu de bataille.
  if len(tas) > 0 :
    # Permet d'utiliser le paramètre "x" de la fonction à la place du "a" ou "b" du nom de la variable "main_a"/"main_b" (exemple: "x = 'b'" alors "main_joueur = main_b").
    main_joueur = 'main_' + x
    # Permet de vider le tas à la fin de la main du joueur "x".
    globals()[main_joueur].extend(tas)
    tas.clear()
  else :
    return

# La fonction comparateur() compare les valeurs des cartes posées par les joueurs.
def comparateur(a, b) :
  # Si la carte du joueur a est supérieur au joueur B.
  if a > b :
    # Permet de prendre la première carte des joueurs A&B (en somme, les cartes posées) et de les ajouter à la fin de la main du joueur A.
    main_a.append(main_a.pop(0))
    main_a.append(main_b.pop(0))
    # Va vérfier si une bataille était en cours au dernier tour (car vu que la carte de A>B la bataille vient forcément de se terminer).
    bataille('a')
    # Renvoie 'A' pour vérification.
    return 'A'
    
  # Si la carte du joueur B est supérieur au joueur A.
  elif b > a : 
    # Permet de prendre la première carte des joueurs A&B (en somme, les cartes posés) et de les ajouter à la fin de la main du joueur B.
    main_b.append(main_b.pop(0))
    main_b.append(main_a.pop(0))
    # Va vérfier si une bataille était en cours au dernier tour (car vu que la carte de B>A la bataille vient forcément de se terminer).
    bataille('b')
    # Renvoie 'B' pour vérification.
    return 'B'
    
  # Si égalité.
  else : 
    # Permet de prendre la première carte des joueurs A&B (en somme, les cartes posés) et de les ajouter à la fin du tas.
    tas.append(main_a.pop(0))
    tas.append(main_b.pop(0))
    # Renvoie 'egalite' pour vérification.
    return 'egalite'



# Début du jeu :
# ------------- 


# Rentre dans la boucle de jeu forcée, tant que les deux joueurs ont une main supérieure à 0 cartes.
while len(main_a) and len(main_b) > 0 :
  # Affiche : Joueur A : 'Chiffre' de 'Famille'  Joueur B : 'Chiffre' de 'Famille'.
  print("Joueur A :", main_a[0][1][0], "de", main_a[0][0], "\t", "Joueur B :", main_b[0][1][0], "de", main_b[0][0])
  # L'appel de la fonction comparateur() est équivalent à la pose des premières cartes de chaque mains de chaque joueur, et à la comparaison de leurs valeurs.
  # Le résultat de la fonction comparateur() (soit : 'A'/'B'/'egalite') et ensuite assigné à la variable "gagnant".
  gagnant = comparateur(main_a[0][1][1], main_b[0][1][1])
  # Si ce résultat vaut autre chose que 'egalite' (c'est-à-dire soit 'A' ou 'B').
  if gagnant != 'egalite' :
    print ("Le joueur", gagnant, "remporte les cartes.", "\n")
    # Décommenter pour empêcher le jeu de se dérouler automatiquement. 
    input("... \n")
  else :
    # Si le résultat vaut 'egalite', alors il faut sortir de la boucle et la répéter pour continuer la bataille.
    continue

# Détermine le gagnant de la partie en fonction de la taille de la main du joueur A (le joueur perdant aura forcément une main de taille 0).
print("Le joueur", 'B' if len(main_a) == 0 else 'A', 'remporte la partie')
