#############################################
# groupe 1 l1MIASHS TD1
# Beatriz ANTON ARTAZA
# Alae KARTOUT
# Basma BAGNAH AMADOU
# Yacine
# Victor NEGRU
# Daniel Pawlaczyk
#https://github.com/bea-anton/robot_ricochet.git
##############################################

# import des librairies

import tkinter as tk
import random as rd

#############################################


COULEUR_FOND1 = "sandybrown"
COULEUR_FOND2 = "wheat"
COULEUR_OBSTACLE = "maroon"
LARGEUR = 640
HAUTEUR = 640
COTE = 40


liste_tuile = []     # liste des 256 tuiles
coordonnees = []
liste1 = []# liste des numéros de tuiles quart haut gauche du plateau
liste2 = []   # liste des numéros de tuiles quart haut droit du plateau
liste3 = []    # liste des numéros de tuiles quart bas gauche du plateau
liste4 = []    # liste des numéros de tuiles quart bas droit du plateau
tuile_robot = 0  # numero de la tuile sur laquelle le robot sera placé
tuiles_utilisees = [119,  120,  135,  136]               #    [119,  120,  135, 136]   tuiles du carré  central
liste_tuile_obstacle = []    # liste des obstacles avec leurs voisines   (évite 'avoir edux obstacle qui se touchent )
liste_tuile_obstacle1 = []         # liste des obstacles sans les cases voisines

tuile_robot_rouge = 0
score_rouge = 0
score_bleu = 0
score_vert = 0
score_jaune = 0
bloque_bind = 0


def reinitialiser_variables():
   global liste_tuile, coordonnees, liste1, liste2,  liste3, liste4,  tuile_robot,  tuiles_utilisees,  liste_tuile_obstacle, liste_tuile_obstacle1, tuile_robot_rouge, score, bloque_bind, score_rouge,score_bleu, score_vert, score_jaune
   liste_tuile = [] 
   coordonnees = []
   liste1 = []
   liste2 = []              
   liste3 = []
   liste4 = []
   tuiles_utilisees = [119,  120,  135,  136]              
   liste_tuile_obstacle = []   
   liste_tuile_obstacle1 = []         
   tuile_robot_rouge, score_rouge,score_bleu, score_vert, score_jaune, bloque_bind,  tuile_robot  = 0, 0, 0, 0, 0, 0, 0
   


def cadre_du_jeu():
    """fenêtre du plateau du jeu"""
    global cadre_robot,  canvas, text_score_rouge, text_score_bleu, text_score_vert, text_score_jaune
    cadre_robot = tk.Frame(racine, bg=COULEUR_FOND1, width=LARGEUR, height = HAUTEUR+30)   #cadre pour placer les différents éléments du décor du jeu 
    cadre_robot.grid()
    canvas = tk.Canvas(cadre_robot, width=LARGEUR, height=HAUTEUR, bg = COULEUR_FOND1)
    canvas.grid(row = 2,  columnspan=4)
    text_score_rouge = tk.Label(cadre_robot, text="Score: "+str(score_rouge),  font = (20),  bg = "red")   #   écrit le score dans le canvas
    text_score_rouge.grid(column = 0, row = 0)
    text_score_bleu = tk.Label(cadre_robot, text="Score: "+str(score_bleu),  font = (20),  bg="blue")   #   écrit le score dans le canvas
    text_score_bleu.grid(column = 1, row = 0) 
    text_score_vert = tk.Label(cadre_robot, text="Score: "+str(score_vert),  font = (20),  bg="green")   #   écrit le score dans le canvas
    text_score_vert.grid(column = 2, row = 0) 
    text_score_jaune = tk.Label(cadre_robot, text="Score: "+str(score_jaune),  font = (20),  bg="yellow")   #   écrit le score dans le canvas
    text_score_jaune.grid(column=3, row=0)
    
    tuiles()
    


def tuiles():
    """ Créé les tuiles du plateau"""
    global liste_tuile,  canvas
    x0,  y0,  x1,  y1 = 0,  0,  COTE,  COTE
    for i in range (0,  HAUTEUR//COTE+0):
        for j in range (0,  LARGEUR//COTE+0):
            canvas.create_rectangle( x0,y0,x1 , y1, fill=COULEUR_FOND1)
            liste_tuile.append([i, j, 0, 0, 0, 0])       #   i ligne et j colonne  ( coordonées de la tuile )      0, 0, 0, 0  haut, droite, bas, gauche  ( pas de muret )
            canvas.create_rectangle(x0+7, y0+7, x1-7, y1-7,  fill =COULEUR_FOND2, outline=COULEUR_FOND2)
            canvas.create_rectangle(x0+15, y0+15, x1-15,  y1-15, fill =COULEUR_FOND1, outline=COULEUR_FOND1)
            x0 = x0+COTE     
            x1 = x1+COTE
        y0, y1 = y0+COTE,  y1+COTE
        x0, x1 = 0, COTE
        
    coordonnees_bordure()
 
def coordonnees_bordure():    # mise à 1 des différentes coordonées des bordures
    """Change la valeur de la bordure en 1 pour les tuiles entourant le plateau et cases centrales"""
    global liste_tuile
    for i in range (0, len(liste_tuile)):
        if liste_tuile[i][0] == 0:           # bord haute       
            liste_tuile[i][2] = 1              # indice [2]  bord haute d'une tuile
        if liste_tuile[i][1] == 15:       # bord droite
            liste_tuile[i][3] = 1   
        if liste_tuile[i][0] ==15 :         # bord basse
            liste_tuile[i][4] = 1            
        if liste_tuile[i][1] == 0 :          # bordure  gauche
            liste_tuile[i][5] =1             
    for i in (119, 120, 135, 136):
        for j in (2, 3, 4, 5):
            liste_tuile[i][j]=1  
            
    obstacle_bordure()
                                

def obstacle_bordure():
    """ Choisi et change la  valeur en 1 pour les tuile de la bordure ( 2 pour chaque côtés)"""
    global liste_tuile_obstacle,  liste_tuile_obstacle1
    #obstacle bordure haute
    obstacle_x1 = rd.randint(1, 6)    # choisi un numero de colonne dans la première moitié gauche du  plateau
    obstacle_x2 = rd.randint(8, 13)        # choisi un numéron de colonne dans la moitiée droite du plateau
    for i in range (0, len(liste_tuile)):    # liste toutes les tuiles 
        if liste_tuile[i][0]==0 :       #   si une tuile dont l'indice de la ligne est O ( première ligne du plateau )
            if liste_tuile[i][1]==obstacle_x1 or liste_tuile[i][1]==obstacle_x2 :    # et si sont indice de colonne corespond à l'indice tiré au sort
                    liste_tuile[i][3] = 1       # alors on pace l'indice du bord haut de la tuile à 1
                    liste_tuile_obstacle.append(i), liste_tuile_obstacle.append(i+16),  liste_tuile_obstacle.append(i+17)              # ajoute le numéro de la tuile et ses voisines à la liste des obstacles      
                    liste_tuile_obstacle1.append(i)
    # obstacle bordure basse
    obstacle_x1 = rd.randint(1, 6)
    obstacle_x2 = rd.randint(8, 13)
    for i in range (0, len(liste_tuile)):
        if liste_tuile[i][0]==15 :           #  obstacle bordure  basse
            if liste_tuile[i][1]==obstacle_x1 or liste_tuile[i][1]==obstacle_x2 : 
                    liste_tuile[i][5] = 1 
                    liste_tuile_obstacle.append(i),  liste_tuile_obstacle.append(i-16),  liste_tuile_obstacle.append(i-17) 
                    liste_tuile_obstacle1.append(i)                
    #obstacle bordure gauche               
    obstacle_y1 = rd.randint(1, 6)
    obstacle_y2 = rd.randint(8, 13)
    for i in range (0, len(liste_tuile)):
        if liste_tuile[i][1]==0 :           #  obstacle bordure  droite
            if liste_tuile[i][0]==obstacle_y1 or liste_tuile[i][0]==obstacle_y2 : 
                    liste_tuile[i][2] = 1 
                    liste_tuile_obstacle.append(i), liste_tuile_obstacle.append(i+1),  liste_tuile_obstacle.append(i-15)
                    liste_tuile_obstacle1.append(i)
     #obstacle bordure droite                
    obstacle_y1 = rd.randint(1, 6)
    obstacle_y2 = rd.randint(8, 13)       
    for i in range (0, len(liste_tuile)):
        if liste_tuile[i][1]==15 :           #  obstacle bordure  gauche
            if liste_tuile[i][0]==obstacle_y1 or liste_tuile[i][0]==obstacle_y2 : 
                    liste_tuile[i][4] = 1
                    liste_tuile_obstacle.append(i), liste_tuile_obstacle.append(i-1),  liste_tuile_obstacle.append(i+17)
                    liste_tuile_obstacle1.append(i)
                            
    liste_tuiles_plateau(0, 8)       #   Argument (0, 8 ) ( permettra dans la fonction liste_tuiles_plateau de lister les tuile de 0 à 7,   puis de 16 à 23,  puis 32 à 39      ect......)
    liste_tuiles_plateau(8, 16)    #   Argument (8, 16 ) ( permettra dans la fonction liste_tuiles_plateau de lister les tuile de 8 à 15,   puis de 24 à 31,  puis 40 à 47      ect......)
    liste_tuiles_plateau (128, 136)
    liste_tuiles_plateau(136,  144)  
        
# liste les numéros de tuiles par quart de plateau                    
def liste_tuiles_plateau(nb1, nb2):    
    """  Le plateau sera découpé en quatre parties     liste1(quart haut gauche),   liste2(quart haut droit)   liste3(quart bas gauche)   liste4(quart bas droit )"""
    global liste1, liste2, liste3, liste4
    a = 0
    for i in range (nb1, nb2):                                   #   création d'une liste contenant le numéro des tuiles du quart gauche du plateau
        for i in range(nb1+a*16, nb2+a*16):
            if nb1==0 and nb2==8 :                  
                if liste_tuile[i][0] != 0 :                 # liste dans laquelle les tuiles de la bordure du haut ne sont pas mises ( ne met pas les tuile de la ligne 0 )
                    if liste_tuile[i][0] !=7 :               #  ( ne met pas les tuiles dela ligne 7 )
                        if liste_tuile[i][1]!=0 :                #   et celles de la bordure de  gauche non plus (ne met pas les tuile de la colonne 0)
                            liste1.append(i)
                            if i ==103:                       # appelle la fonction quand la liste est complète (dernier numéro de tuile de la liste)
                                liste1.remove(102),  liste1.remove(103)     # tuile voisine du carré central
                                obstacle_plateau(liste1)    # appelle la fonction obstacle_plateau pour la liste1          
                                
            if nb1==8 and nb2==16 :
                if liste_tuile[i][0] !=0 :
                    if liste_tuile[i][1] != 8 :                        
                        if liste_tuile[i][1] != 15 :
                            liste2.append(i)
                            if i == 126:
                                liste2.remove(105),  liste2.remove(121)
                                obstacle_plateau(liste2)
                                
            if nb1==128 and nb2==136 :
                if liste_tuile[i][0] !=15 :
                    if liste_tuile[i][1] !=0:
                        if liste_tuile[i][1] != 7 :                        
                            liste3.append(i)                        
                            if i == 230:
                                liste3.remove(134),  liste3.remove(150)
                                obstacle_plateau(liste3)
                                
            if nb1 ==136 and nb2==144 :
                if liste_tuile[i][0]!=8 :
                    if liste_tuile[i][1] != 15:
                        if liste_tuile[i][1]!=15 :
                            liste4.append(i)
                            if i == 238:
                                liste4.remove(152),  liste4.remove(153)
                                obstacle_plateau(liste4)
        a=a+1


def obstacle_plateau(liste):
    """pour chaque liste ( liste des tuiles par quart de plateau ) choisi une tuile, change la valeur de certaines bordures pour en faire des obstacles...... puis enlève cette tuiles et ses voisines de la liste pour qu'elle ne soit plus choisi"""
    global liste_tuile_obstacle
    la_tuile=0
    for i in (liste_tuile_obstacle):
        try :        
            liste.remove(i)
        except ValueError :
            pass
    for i in range (0,4):    
        la_tuile=rd.choice(liste)      # choisi une tuile au hasard dans la liste
        liste_tuile_obstacle.append(la_tuile)
        for j in (-17, -16,  -15, -1 , 0, 1,15,  16,  17):   # retire de la liste la tuile et celles qui l'entourent
            try:
                liste.remove (la_tuile-j)        #  suppression des tuiles voisines de celle tirée au sort
            except  ValueError :
                pass
                
        parois_horiz=rd.choice([2,  4] )   #    
        parois_vert=rd.choice([3, 5] )
        
        liste_tuile[la_tuile][parois_horiz]=1
        liste_tuile[la_tuile][parois_vert]=1
   
    if liste==liste4:     #  n'execute les fonctions obstacle et robot que quand la liste4 est passé en argument, ( sinon les fonctions robot et obstacle sont executer à chaque appel de la fonction obstacle plateau )
       obstacle()
       robot('red'),  robot('blue'),  robot("green"), robot('yellow')       
             

def obstacle():
    """ Dessine les obstacles ( bordure et obstacle du plateau )"""
    for i in range (0, len(liste_tuile)):
        if  liste_tuile[i][2] == 1 :         #   obstacle haute d'une tuile
            canvas.create_rectangle (liste_tuile[i][1]*40, liste_tuile[i][0]*40-3, (liste_tuile[i][1]+1)*40,  liste_tuile[i][0]*40 +3,  fill=COULEUR_OBSTACLE)            
        if liste_tuile[i][3] == 1 :                #    obstacle droite  d'une tuile
            canvas.create_rectangle ((liste_tuile[i][1]+1)*40-3, liste_tuile[i][0]*40, (liste_tuile[i][1]+1)*40+3, (liste_tuile[i][0]+1)*40,  fill= COULEUR_OBSTACLE)            
        if liste_tuile[i][4] == 1 :           #   obstacle  basse  d'une tuile          
            canvas.create_rectangle (liste_tuile[i][1]*40, (liste_tuile[i][0]+1)*40-3, liste_tuile[i][1]*40+40, (liste_tuile[i][0]+1)*40+3,  fill= COULEUR_OBSTACLE )            
        if liste_tuile[i][5] ==1 :                 #    obstacle gauche d'une tuile
            canvas.create_rectangle (liste_tuile[i][1]*40-3, liste_tuile[i][0]*40, liste_tuile[i][1]*40+3, (liste_tuile[i][0]+1)*40,  fill= COULEUR_OBSTACLE )            
        canvas.create_rectangle (LARGEUR//2-40,  HAUTEUR//2-40,  LARGEUR//2+40,  LARGEUR//2+40,  fill=COULEUR_OBSTACLE)    # obstacle central
        canvas.create_rectangle (LARGEUR//2-30,  HAUTEUR//2-30,  LARGEUR//2+30,  LARGEUR//2+30,  fill=COULEUR_FOND1)


def robot(couleur):
    """place les robots au hasard sur le plateau (en évitant les cases centarles et les cases utilisées par les autres robots )"""
    global robot_rouge,  robot_vert,  robot_bleu,  robot_jaune,  tuiles_utilisees,  tuile_robot_rouge,  tuile_robot_bleu,  tuile_robot_vert,  tuile_robot_jaune
    tuile_robot = rd.randint(0,  255)   # choix d'un chiffre entre 0 et 255 inclus
    while  tuile_robot  in tuiles_utilisees :
        tuile_robot = rd.randint(0,  255)        
    tuiles_utilisees.append(tuile_robot)        
    ligne_robot = liste_tuile[tuile_robot][0]
    colonne_robot =liste_tuile[tuile_robot][1]        
    if couleur=='red' :
        cible(couleur)
        robot_rouge=canvas.create_oval(colonne_robot*40 +5, ligne_robot*40 +5,  colonne_robot*40+35,ligne_robot * 40+35, fill=couleur)   #   on met colonne_robot pour l'axe des x car ça corespond à un déplacement horizontal
                                                                                                                                                                                                        # on met  ligne_robot pour l'axe des y car ça correspond à un déplacement vertical
        tuile_robot_rouge = tuile_robot
    if couleur=='blue':
        robot_bleu=canvas.create_oval(colonne_robot*40 +5, ligne_robot*40 +5,  colonne_robot*40+35,ligne_robot * 40+35, fill=couleur)
        tuile_robot_bleu=tuile_robot
    if couleur=='green':
        robot_vert=canvas.create_oval(colonne_robot*40 +5, ligne_robot*40 +5,  colonne_robot*40+35,ligne_robot * 40+35, fill=couleur)
        tuile_robot_vert=tuile_robot
    if couleur=='yellow':
        robot_jaune=canvas.create_oval(colonne_robot*40 +5, ligne_robot*40 +5,  colonne_robot*40+35,ligne_robot * 40+35,  fill=couleur)
        tuile_robot_jaune=tuile_robot 
        


def cible(couleur):
    """place la cible contre un obstacle"""
    global tuile_cible,  cible,  ligne_cible,  colonne_cible,  cible_rouge
    tuile_cible=0
    tuile_cible = rd.choice(liste_tuile_obstacle1)    # tire au hazard une tuile au hasard parmis la liste des obstacles
    ligne_cible = liste_tuile[tuile_cible][0]           #  recupère le numéro de ligne de la tuile choisi
    colonne_cible =liste_tuile[tuile_cible][1]          #récupère le numéro de la colonne de la tuile choisie
    cible_rouge = canvas.create_rectangle(colonne_cible*40 +10, ligne_cible*40 +10,  colonne_cible*40+30, ligne_cible * 40+30,  fill=couleur)


def deplacement_rouge_droit():
    """ déplacement du robot rouge"""
    global tuile_robot_rouge,  bloque_bind
    bloque_bind=1                # empèche  l'appel des fonctions de déplacement 
    tuile_robot_rouge= tuile_robot_rouge +1       # indrémentation de la tuile où se trouve le robot ( tuile siuvante dans le sens de déplacement )
                                                                             # les lignes suivantes vérifient que la tuile suivante n'a pas d'obstatacle au déplacement du robot
    if liste_tuile[tuile_robot_rouge][3]==1 and liste_tuile[tuile_robot_rouge][5]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 40, 0)                 # si la tuile suivante n'a pas de robot et a un obstacle à droite, un seul déplacement est effectué
        bloque_bind=0                                               # permet le rappel des fonctions de déplacement
    if liste_tuile[tuile_robot_rouge][5]==0 and liste_tuile[tuile_robot_rouge][3]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 40, 0)            # si la tuile suivante n'a ni  robot, ni obstacle un déplacement est effectué, et la fontion deplacement_rouge_rappelé
        canvas.after(100, deplacement_rouge_droit)       
    if liste_tuile[tuile_robot_rouge][3]==1 and liste_tuile[tuile_robot_rouge][5]==1 or liste_tuile[tuile_robot_rouge][3]==0 and liste_tuile[tuile_robot_rouge][5]==1 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_rouge == tuile_robot_vert or tuile_robot_rouge == tuile_robot_jaune:
        tuile_robot_rouge= tuile_robot_rouge -1        #   si la tuile suivante à un obstacle gauche ou deux obstacles ( droit, gauche ), pas de déplacement 
        bloque_bind=0                   #  permet le rappel des fonctions de déplacement
    if liste_tuile[tuile_robot_rouge][0]==ligne_cible and liste_tuile[tuile_robot_rouge][1]==colonne_cible:    #  Si la ligne et la colonne sont les même pour le robot et la cible alors le joueur à gagné
        bloque_bind=1           #   bloque les mouvement des flèches du clavier
        fin_de_partie("rouge")  # appelle la fonction fin_de_partie pour inscrire le score
          
def deplacement_rouge_gauche():
    global tuile_robot_rouge,  bloque_bind
    tuile_robot_rouge= tuile_robot_rouge -1    
    bloque_bind=1
    if liste_tuile[tuile_robot_rouge][3]==0 and liste_tuile[tuile_robot_rouge][5]==1 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, -40, 0)
        bloque_bind=0
    if liste_tuile[tuile_robot_rouge][5]==0 and liste_tuile[tuile_robot_rouge][3]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, -40, 0)
        canvas.after(100, deplacement_rouge_gauche)     
    if liste_tuile[tuile_robot_rouge][3]==1 and liste_tuile[tuile_robot_rouge][5]==1 or liste_tuile[tuile_robot_rouge][3]==1 and liste_tuile[tuile_robot_rouge][5]==0 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_rouge == tuile_robot_vert or tuile_robot_rouge == tuile_robot_jaune:
        tuile_robot_rouge= tuile_robot_rouge +1
        bloque_bind=0
    if liste_tuile[tuile_robot_rouge][0]==ligne_cible and liste_tuile[tuile_robot_rouge][1]==colonne_cible:
        bloque_bind=1
        fin_de_partie("rouge")
           
def deplacement_rouge_haut():
    global tuile_robot_rouge,  bloque_bind
    bloque_bind=1
    tuile_robot_rouge= tuile_robot_rouge -16
    if liste_tuile[tuile_robot_rouge][4]==0 and liste_tuile[tuile_robot_rouge][2]==1 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 0, -40)
        bloque_bind=0
    if liste_tuile[tuile_robot_rouge][2]==0 and liste_tuile[tuile_robot_rouge][4]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 0, -40)
        canvas.after(100, deplacement_rouge_haut)    
    if liste_tuile[tuile_robot_rouge][4]==1 and liste_tuile[tuile_robot_rouge][2]==1 or liste_tuile[tuile_robot_rouge][4]==1 and liste_tuile[tuile_robot_rouge][2]==0 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_rouge == tuile_robot_vert or tuile_robot_rouge == tuile_robot_jaune:
        tuile_robot_rouge= tuile_robot_rouge +16
        bloque_bind=0
    if liste_tuile[tuile_robot_rouge][0]==ligne_cible and liste_tuile[tuile_robot_rouge][1]==colonne_cible:
        bloque_bind=1
        fin_de_partie("rouge")

def deplacement_rouge_bas():
    global tuile_robot_rouge,  bloque_bind
    bloque_bind=1
    tuile_robot_rouge= tuile_robot_rouge +16 
    if liste_tuile[tuile_robot_rouge][4]==1 and liste_tuile[tuile_robot_rouge][2]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 0, 40)
        bloque_bind=0
    if liste_tuile[tuile_robot_rouge][2]==0 and liste_tuile[tuile_robot_rouge][4]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_rouge != tuile_robot_vert and tuile_robot_rouge != tuile_robot_jaune:
        canvas.move(robot_rouge, 0, 40)
        canvas.after(100, deplacement_rouge_bas)              
    if liste_tuile[tuile_robot_rouge][4]==1 and liste_tuile[tuile_robot_rouge][2]==1 and liste_tuile[tuile_robot_rouge][4]==0 or liste_tuile[tuile_robot_rouge][2]==1 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_rouge == tuile_robot_vert or tuile_robot_rouge == tuile_robot_jaune:
        bloque_bind=0
        tuile_robot_rouge= tuile_robot_rouge -16
    if liste_tuile[tuile_robot_rouge][0]==ligne_cible and liste_tuile[tuile_robot_rouge][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("rouge")
        

def deplacement_bleu_droit():
    """ déplacement du robot bleu"""
    global tuile_robot_bleu,  bloque_bind
    bloque_bind=1                
    tuile_robot_bleu= tuile_robot_bleu +1                                                                               
    if liste_tuile[tuile_robot_bleu][3]==1 and liste_tuile[tuile_robot_bleu][5]==0 and tuile_robot_bleu != tuile_robot_rouge and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 40, 0)                
        bloque_bind=0                                              
    if liste_tuile[tuile_robot_bleu][5]==0 and liste_tuile[tuile_robot_bleu][3]==0 and tuile_robot_bleu != tuile_robot_rouge and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 40, 0)
        canvas.after(100, deplacement_bleu_droit)       
    if liste_tuile[tuile_robot_bleu][3]==1 and liste_tuile[tuile_robot_bleu][5]==1 or liste_tuile[tuile_robot_bleu][3]==0 and liste_tuile[tuile_robot_bleu][5]==1 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_bleu == tuile_robot_vert or tuile_robot_bleu == tuile_robot_jaune:
        tuile_robot_bleu= tuile_robot_bleu -1
        bloque_bind=0
    if liste_tuile[tuile_robot_bleu][0]==ligne_cible and liste_tuile[tuile_robot_bleu][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("bleu")
          
def deplacement_bleu_gauche():
    global tuile_robot_bleu,  bloque_bind
    tuile_robot_bleu= tuile_robot_bleu -1    
    bloque_bind=1
    if liste_tuile[tuile_robot_bleu][3]==0 and liste_tuile[tuile_robot_bleu][5]==1 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, -40, 0)
        bloque_bind=0
    if liste_tuile[tuile_robot_bleu][5]==0 and liste_tuile[tuile_robot_bleu][3]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, -40, 0)
        canvas.after(100, deplacement_bleu_gauche)     
    if liste_tuile[tuile_robot_bleu][3]==1 and liste_tuile[tuile_robot_bleu][5]==1 or liste_tuile[tuile_robot_bleu][3]==1 and liste_tuile[tuile_robot_bleu][5]==0 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_bleu == tuile_robot_vert or tuile_robot_bleu == tuile_robot_jaune:
        tuile_robot_bleu= tuile_robot_bleu +1
        bloque_bind=0
    if liste_tuile[tuile_robot_bleu][0]==ligne_cible and liste_tuile[tuile_robot_bleu][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("bleu")
           
def deplacement_bleu_haut():
    global tuile_robot_bleu,  bloque_bind
    bloque_bind=1
    tuile_robot_bleu= tuile_robot_bleu -16
    if liste_tuile[tuile_robot_bleu][4]==0 and liste_tuile[tuile_robot_bleu][2]==1 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 0, -40)
        bloque_bind=0
    if liste_tuile[tuile_robot_bleu][2]==0 and liste_tuile[tuile_robot_bleu][4]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 0, -40)
        canvas.after(100, deplacement_bleu_haut)    
    if liste_tuile[tuile_robot_bleu][4]==1 and liste_tuile[tuile_robot_bleu][2]==1 or liste_tuile[tuile_robot_bleu][4]==1 and liste_tuile[tuile_robot_bleu][2]==0 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_bleu == tuile_robot_vert or tuile_robot_bleu == tuile_robot_jaune:
        tuile_robot_bleu= tuile_robot_bleu +16
        bloque_bind=0        
    if liste_tuile[tuile_robot_bleu][0]==ligne_cible and liste_tuile[tuile_robot_bleu][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("bleu")

def deplacement_bleu_bas():
    global tuile_robot_bleu,  bloque_bind
    bloque_bind=1
    tuile_robot_bleu= tuile_robot_bleu +16 
    if liste_tuile[tuile_robot_bleu][4]==1 and liste_tuile[tuile_robot_bleu][2]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 0, 40)
        bloque_bind=0
    if liste_tuile[tuile_robot_bleu][2]==0 and liste_tuile[tuile_robot_bleu][4]==0 and tuile_robot_rouge != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_bleu != tuile_robot_jaune:
        canvas.move(robot_bleu, 0, 40)
        canvas.after(100, deplacement_bleu_bas)              
    if liste_tuile[tuile_robot_bleu][4]==1 and liste_tuile[tuile_robot_bleu][2]==1 and liste_tuile[tuile_robot_bleu][4]==0 or liste_tuile[tuile_robot_bleu][2]==1 or tuile_robot_rouge == tuile_robot_bleu or tuile_robot_bleu == tuile_robot_vert or tuile_robot_bleu == tuile_robot_jaune:
        bloque_bind=0
        tuile_robot_bleu= tuile_robot_bleu -16
    if liste_tuile[tuile_robot_bleu][0]==ligne_cible and liste_tuile[tuile_robot_bleu][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("bleu")


def deplacement_vert_droit():
    """déplacement du robot vert"""
    global tuile_robot_vert,  bloque_bind
    bloque_bind=1                 
    tuile_robot_vert= tuile_robot_vert +1                                                                                    
    if liste_tuile[tuile_robot_vert][3]==1 and liste_tuile[tuile_robot_vert][5]==0 and tuile_robot_vert != tuile_robot_rouge and tuile_robot_vert != tuile_robot_bleu and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 40, 0)                 
        bloque_bind=0                                              
    if liste_tuile[tuile_robot_vert][5]==0 and liste_tuile[tuile_robot_vert][3]==0 and tuile_robot_vert != tuile_robot_rouge and tuile_robot_vert != tuile_robot_bleu and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 40, 0)
        canvas.after(100, deplacement_vert_droit)       
    if liste_tuile[tuile_robot_vert][3]==1 and liste_tuile[tuile_robot_vert][5]==1 or liste_tuile[tuile_robot_vert][3]==0 and liste_tuile[tuile_robot_vert][5]==1 or tuile_robot_rouge == tuile_robot_vert or tuile_robot_bleu == tuile_robot_vert or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_vert= tuile_robot_vert -1
        bloque_bind=0 
    if liste_tuile[tuile_robot_vert][0]==ligne_cible and liste_tuile[tuile_robot_vert][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("vert")
          
def deplacement_vert_gauche():
    global tuile_robot_vert,  bloque_bind
    tuile_robot_vert= tuile_robot_vert -1    
    bloque_bind=1
    if liste_tuile[tuile_robot_vert][3]==0 and liste_tuile[tuile_robot_vert][5]==1 and tuile_robot_vert != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, -40, 0)
        bloque_bind=0
    if liste_tuile[tuile_robot_vert][5]==0 and liste_tuile[tuile_robot_vert][3]==0 and tuile_robot_vert != tuile_robot_bleu and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, -40, 0)
        canvas.after(100, deplacement_vert_gauche)     
    if liste_tuile[tuile_robot_vert][3]==1 and liste_tuile[tuile_robot_vert][5]==1 or liste_tuile[tuile_robot_vert][3]==1 and liste_tuile[tuile_robot_vert][5]==0 or tuile_robot_rouge == tuile_robot_vert or tuile_robot_bleu == tuile_robot_vert or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_vert= tuile_robot_vert +1
        bloque_bind=0 
    if liste_tuile[tuile_robot_vert][0]==ligne_cible and liste_tuile[tuile_robot_vert][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("vert")
           
def deplacement_vert_haut():
    global tuile_robot_vert,  bloque_bind
    bloque_bind=1
    tuile_robot_vert= tuile_robot_vert -16

    if liste_tuile[tuile_robot_vert][4]==0 and liste_tuile[tuile_robot_vert][2]==1 and tuile_robot_rouge != tuile_robot_vert and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 0, -40)
        bloque_bind=0
    if liste_tuile[tuile_robot_vert][2]==0 and liste_tuile[tuile_robot_vert][4]==0 and tuile_robot_rouge != tuile_robot_vert and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 0, -40)
        canvas.after(100, deplacement_vert_haut)    
    if liste_tuile[tuile_robot_vert][4]==1 and liste_tuile[tuile_robot_vert][2]==1 or liste_tuile[tuile_robot_vert][4]==1 and liste_tuile[tuile_robot_vert][2]==0 or tuile_robot_rouge == tuile_robot_vert or tuile_robot_bleu == tuile_robot_vert or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_vert= tuile_robot_vert +16
        bloque_bind=0  
    if liste_tuile[tuile_robot_vert][0]==ligne_cible and liste_tuile[tuile_robot_vert][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("vert")        

def deplacement_vert_bas():
    global tuile_robot_vert,  bloque_bind
    bloque_bind=1
    tuile_robot_vert= tuile_robot_vert +16 
    if liste_tuile[tuile_robot_vert][4]==1 and liste_tuile[tuile_robot_vert][2]==0 and tuile_robot_rouge != tuile_robot_vert and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 0, 40)
        bloque_bind=0
    if liste_tuile[tuile_robot_vert][2]==0 and liste_tuile[tuile_robot_vert][4]==0 and tuile_robot_rouge != tuile_robot_vert and tuile_robot_bleu != tuile_robot_vert and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_vert, 0, 40)
        canvas.after(100, deplacement_vert_bas)              
    if liste_tuile[tuile_robot_vert][4]==1 and liste_tuile[tuile_robot_vert][2]==1 and liste_tuile[tuile_robot_vert][4]==0 or liste_tuile[tuile_robot_vert][2]==1 or tuile_robot_rouge == tuile_robot_vert or tuile_robot_bleu == tuile_robot_vert or tuile_robot_vert == tuile_robot_jaune:
        bloque_bind=0
        tuile_robot_vert= tuile_robot_vert -16
    if liste_tuile[tuile_robot_vert][0]==ligne_cible and liste_tuile[tuile_robot_vert][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("vert")
        

def deplacement_jaune_droit():
    """ déplacement du robot jaune"""
    global tuile_robot_jaune,  bloque_bind
    bloque_bind=1               
    tuile_robot_jaune= tuile_robot_jaune +1                                                                                
    if liste_tuile[tuile_robot_jaune][3]==1 and liste_tuile[tuile_robot_jaune][5]==0 and tuile_robot_jaune != tuile_robot_rouge and tuile_robot_jaune != tuile_robot_bleu and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 40, 0)                
        bloque_bind=0                                              
    if liste_tuile[tuile_robot_jaune][5]==0 and liste_tuile[tuile_robot_jaune][3]==0 and tuile_robot_jaune != tuile_robot_rouge and tuile_robot_jaune != tuile_robot_bleu and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 40, 0)
        canvas.after(100, deplacement_jaune_droit)       
    if liste_tuile[tuile_robot_jaune][3]==1 and liste_tuile[tuile_robot_jaune][5]==1 or liste_tuile[tuile_robot_jaune][3]==0 and liste_tuile[tuile_robot_jaune][5]==1 or tuile_robot_rouge == tuile_robot_jaune or tuile_robot_bleu == tuile_robot_jaune or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_jaune= tuile_robot_jaune -1
        bloque_bind=0
    if liste_tuile[tuile_robot_jaune][0]==ligne_cible and liste_tuile[tuile_robot_jaune][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("jaune")
          
def deplacement_jaune_gauche():
    global tuile_robot_jaune,  bloque_bind
    tuile_robot_jaune= tuile_robot_jaune -1    
    bloque_bind=1
    if liste_tuile[tuile_robot_jaune][3]==0 and liste_tuile[tuile_robot_jaune][5]==1 and tuile_robot_jaune != tuile_robot_rouge and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, -40, 0)
        bloque_bind=0
    if liste_tuile[tuile_robot_jaune][5]==0 and liste_tuile[tuile_robot_jaune][3]==0 and tuile_robot_jaune != tuile_robot_rouge and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, -40, 0)
        canvas.after(100, deplacement_jaune_gauche)     
    if liste_tuile[tuile_robot_jaune][3]==1 and liste_tuile[tuile_robot_jaune][5]==1 or liste_tuile[tuile_robot_jaune][3]==1 and liste_tuile[tuile_robot_jaune][5]==0 or tuile_robot_rouge == tuile_robot_jaune or tuile_robot_bleu == tuile_robot_jaune or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_jaune= tuile_robot_jaune +1
        bloque_bind=0    
           
def deplacement_jaune_haut():
    global tuile_robot_jaune,  bloque_bind
    bloque_bind=1
    tuile_robot_jaune= tuile_robot_jaune -16
    if liste_tuile[tuile_robot_jaune][4]==0 and liste_tuile[tuile_robot_jaune][2]==1 and tuile_robot_rouge != tuile_robot_jaune and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 0, -40)
        bloque_bind=0
    if liste_tuile[tuile_robot_jaune][2]==0 and liste_tuile[tuile_robot_jaune][4]==0 and tuile_robot_rouge != tuile_robot_jaune and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 0, -40)
        canvas.after(100, deplacement_jaune_haut)    
    if liste_tuile[tuile_robot_jaune][4]==1 and liste_tuile[tuile_robot_jaune][2]==1 or liste_tuile[tuile_robot_jaune][4]==1 and liste_tuile[tuile_robot_jaune][2]==0 or tuile_robot_rouge == tuile_robot_jaune or tuile_robot_bleu == tuile_robot_jaune or tuile_robot_vert == tuile_robot_jaune:
        tuile_robot_jaune= tuile_robot_jaune +16
        bloque_bind=0
    if liste_tuile[tuile_robot_jaune][0]==ligne_cible and liste_tuile[tuile_robot_jaune][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("jaune")        

def deplacement_jaune_bas():
    global tuile_robot_jaune,  bloque_bind
    bloque_bind=1
    tuile_robot_jaune= tuile_robot_jaune +16 
    if liste_tuile[tuile_robot_jaune][4]==1 and liste_tuile[tuile_robot_jaune][2]==0 and tuile_robot_rouge != tuile_robot_jaune and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 0, 40)
        bloque_bind=0
    if liste_tuile[tuile_robot_jaune][2]==0 and liste_tuile[tuile_robot_jaune][4]==0 and tuile_robot_rouge != tuile_robot_jaune and tuile_robot_bleu != tuile_robot_jaune and tuile_robot_vert != tuile_robot_jaune:
        canvas.move(robot_jaune, 0, 40)
        canvas.after(150, deplacement_jaune_bas)              
    if liste_tuile[tuile_robot_jaune][4]==1 and liste_tuile[tuile_robot_jaune][2]==1 and liste_tuile[tuile_robot_jaune][4]==0 or liste_tuile[tuile_robot_jaune][2]==1 or tuile_robot_rouge == tuile_robot_jaune or tuile_robot_bleu == tuile_robot_jaune or tuile_robot_vert == tuile_robot_jaune:
        bloque_bind=0
        tuile_robot_jaune= tuile_robot_jaune -16
    if liste_tuile[tuile_robot_jaune][0]==ligne_cible and liste_tuile[tuile_robot_jaune][1]==colonne_cible:        
        bloque_bind=1
        fin_de_partie("jaune")

        


def choix_robot(couleur):
    """ Choix du robot"""
    global choix_couleur_robot
    choix_couleur_robot=couleur    
        
       

def deplacement_droite(event):        
    """Fonctions appelant le déplacement du robot rouge, fonction lancée quand un evenement survient sur la flèche du haut  """
    if bloque_bind==0:                                                  #    empèche de rappeler lune des fonctions de déplacement du robot rouge, si la fonction de déplacement du robot n'est pas finit
        if choix_couleur_robot=='rouge':
            if  liste_tuile[tuile_robot_rouge][3]!=1:        #  autorise le déplacement que si la tuile suivante n'a pas d'obstacle à gauche
                deplacement_rouge_droit()
                affiche_score('rouge')
        if choix_couleur_robot=='bleu':
            if  liste_tuile[tuile_robot_bleu][3]!=1:        
                deplacement_bleu_droit()
                affiche_score('bleu')
        if choix_couleur_robot=='vert':
            if  liste_tuile[tuile_robot_vert][3]!=1:        
                deplacement_vert_droit()
                affiche_score('vert')
        if choix_couleur_robot=='jaune':
            if  liste_tuile[tuile_robot_jaune][3]!=1:        
                deplacement_jaune_droit()
                affiche_score('jaune')
                
def deplacement_gauche(event):
    if bloque_bind==0:
        if choix_couleur_robot=='rouge':
            if  liste_tuile[tuile_robot_rouge][5]!=1:
                deplacement_rouge_gauche()
                affiche_score('rouge')
        if choix_couleur_robot=='bleu':
            if  liste_tuile[tuile_robot_bleu][5]!=1:
                deplacement_bleu_gauche()
                affiche_score('bleu')
        if choix_couleur_robot=='vert':
            if  liste_tuile[tuile_robot_vert][5]!=1:
                deplacement_vert_gauche()
                affiche_score('vert')
        if choix_couleur_robot=='jaune':
            if  liste_tuile[tuile_robot_jaune][5]!=1:
                deplacement_jaune_gauche()
                affiche_score('jaune')
                
def deplacement_haut(event):
    if bloque_bind==0:
        if choix_couleur_robot=='rouge':
            if  liste_tuile[tuile_robot_rouge][2]!=1:
                deplacement_rouge_haut()
                affiche_score('rouge')
        if choix_couleur_robot=='bleu':
            if  liste_tuile[tuile_robot_bleu][2]!=1:
                deplacement_bleu_haut()
                affiche_score('bleu')
        if choix_couleur_robot=='vert':
            if  liste_tuile[tuile_robot_vert][2]!=1:
                deplacement_vert_haut()
                affiche_score('vert')
        if choix_couleur_robot=='jaune':
            if  liste_tuile[tuile_robot_jaune][2]!=1:
                deplacement_jaune_haut()
                affiche_score('jaune')

def deplacement_bas(event):
    if bloque_bind==0:
        if choix_couleur_robot=='rouge':
            if  liste_tuile[tuile_robot_rouge][4]!=1:
                deplacement_rouge_bas()
                affiche_score('rouge')
        if choix_couleur_robot=='bleu':
            if  liste_tuile[tuile_robot_bleu][4]!=1:
                deplacement_bleu_bas()
                affiche_score('bleu')
        if choix_couleur_robot=='vert':
            if  liste_tuile[tuile_robot_vert][4]!=1:
                deplacement_vert_bas()
                affiche_score('vert')
        if choix_couleur_robot=='jaune':
            if  liste_tuile[tuile_robot_jaune][4]!=1:
                deplacement_jaune_bas()
                affiche_score('jaune')


def souris(event):
    """ évenements du clic gauche de la souris"""
    global choix_couleur_robot
    if event.x>=liste_tuile[tuile_robot_rouge][1]*40 and event.x<=liste_tuile[tuile_robot_rouge][1]*40+40:       # si le x de la souris est compris entre colonne de la tuile*40 et colonne de la tuile*40+40
        if event.y>=liste_tuile[tuile_robot_rouge][0]*40 and event.y<=liste_tuile[tuile_robot_rouge][0]*40+40:     # si le y de la souris est compris entre ligne de la tuile*40 et ligne de la tuile*40+40  ( rappel: la largeur d'une tuile est de 40)
            choix_couleur_robot="rouge"
    if event.x>=liste_tuile[tuile_robot_bleu][1]*40 and event.x<=liste_tuile[tuile_robot_bleu][1]*40+40:
        if event.y>=liste_tuile[tuile_robot_bleu][0]*40 and event.y<=liste_tuile[tuile_robot_bleu][0]*40+40:
            choix_couleur_robot="bleu"
    if event.x>=liste_tuile[tuile_robot_vert][1]*40 and event.x<=liste_tuile[tuile_robot_vert][1]*40+40:
        if event.y>=liste_tuile[tuile_robot_vert][0]*40 and event.y<=liste_tuile[tuile_robot_vert][0]*40+40:
            choix_couleur_robot="vert"
    if event.x>=liste_tuile[tuile_robot_jaune][1]*40 and event.x<=liste_tuile[tuile_robot_jaune][1]*40+40:
        if event.y>=liste_tuile[tuile_robot_jaune][0]*40 and event.y<=liste_tuile[tuile_robot_jaune][0]*40+40:
            choix_couleur_robot="jaune"               
    if event.x>=280 and event.x<=360:
        if event.y>280 and event.y<360:
            cadre_robot.destroy()            
            reinitialiser_variables()
            cadre_du_jeu()
    

def affiche_score(couleur):
    """Fonction qui compte et affiche le score"""
    global score_rouge,  score_bleu,  score_vert,  score_jaune, text_score_rouge, text_score_bleu, text_score_vert,  text_score_jaune
    if couleur=='rouge':
        score_rouge = score_rouge+1
        str_score = "Score: " + str(score_rouge)       # score_rouge est passé en chaine de caractère pour être écrite en text dans le label
        text_score_rouge["text"]=str_score        #      envoie str_score dans le label text_score_rouge
    if couleur=='bleu':
        score_bleu = score_bleu+1
        str_score = "Score: " + str(score_bleu)       
        text_score_bleu["text"]=str_score 
    if couleur=='vert':
        score_vert = score_vert+1
        str_score = "Score: " + str(score_vert)       
        text_score_vert["text"]=str_score 
    if couleur=='jaune':
        score_jaune = score_jaune+1
        str_score = "Score: " + str(score_jaune)       
        text_score_jaune["text"]=str_score 
        
        

def fin_de_partie(couleur):
    """Affichage du score de fin de partie"""
    if couleur=="rouge":
        canvas.create_text((LARGEUR//2-20, HAUTEUR//2),  text="vous avez gagné en "+str(score_rouge)+" coups",  fill="red",  font="Arial 30 bold")
    if couleur=="bleu":
        canvas.create_text((LARGEUR//2-20, HAUTEUR//2),  text="vous avez gagné en "+str(score_bleu)+" coups",  fill="blue",  font="Arial 30 bold")    
    if couleur=="vert":
        canvas.create_text((LARGEUR//2-20, HAUTEUR//2),  text="vous avez gagné en "+str(score_vert)+" coups",  fill="green",  font="Arial 30 bold")
    if couleur=="jaune":
        canvas.create_text((LARGEUR//2-20, HAUTEUR//2),  text="vous avez gagné en "+str(score_jaune)+" coups",  fill="yellow",  font="Arial 30 bold")



#créaton de la fenêtre racine
racine = tk.Tk()
racine.title("Robot Ricochet")


#Liaison des événements
racine.bind('<KeyPress-Right>', deplacement_droite)
racine.bind('<KeyPress-Left>', deplacement_gauche)
racine.bind('<KeyPress-Up>' , deplacement_haut)
racine.bind('<KeyPress-Down>', deplacement_bas)
racine.bind("<Button-1>", souris)
        
# programme pour executer le programme du jeu              
cadre_du_jeu()


# boucle principale   
racine.mainloop()