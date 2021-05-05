#############################################
# groupe MIASHS 1
# Alae KARTOUT
# Basma BAGNAH AMADOU
# Yacine
# Victor
# Beatriz ANTON ARTAZA
# https://github.com/bea-anton/projet_incendie.git
##############################################

##############################################
# import des librairies

import tkinter as tk
import random

racine = tk.Tk()
racine.title("Robot Ricochet")

#############################################

COULEUR_FOND = "rosybrown"
COULEUR_QUADR = "grey"
COULEUR_MUR = "black"

LARGEUR = 800
HAUTEUR = 800
COTE = 50
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

tableau = None
objets = []
couleurs = ["red"]

##############################################
# fonctions


def quadrilage():
    """Affiche un quadrilage sur le canvas."""
    x0, x1 = 0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE


def robot_rouge():
    global objets
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append ( canvas.create_oval (( x,y), (x+40, y+40),
    fill="red"))

def robot_vert():
    global objets
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval (( x,y), (x+40, y+40),
    fill="green" ))

def robot_jaune():
    global objets
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval((x,y), (x+40, y+40),
    fill = "yellow"))


def robot_bleu():
    global objets
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval((x,y), (x+40, y+40),
    fill = "blue"))


def ligne_verticale():
    global objets
    x = random.randrange(100, 750, 50)
    y = random.randrange(0 , 1, 50)
    objets.append(canvas.create_line((x, y), (x, y+50), fill="black"))
    p = random.randrange(100, 750, 50)
    q = random.randrange(750, 800, 50)
    objets.append(canvas.create_line((p, q), (p, q+50), fill="black"))
    

def ligne_horizontale():
    global objets
    x = random.randrange(0, 1, 1)
    y = random.randrange(100, 750, 50)
    objets.append(canvas.create_line((x, y), (x+50, y), fill="black"))
    p = random.randrange(750, 800, 50)
    q = random.randrange(100, 750, 50)
    objets.append(canvas.create_line((p, q), (p+50, q), fill="black"))

def obstacle_croix():
    global objets
    x = random.randint(100,750)
    y = random.randint(100, 750)
    objets.append(canvas.create_line((x, y), (x, y+50), fill="black"))
    objets.append(canvas.create_line((x+50,y), (x,y), fill="black"))

def undo():
    global objets
    canvas.delete(objets[-1:])
    objets = objets[:-1]

bouton_robot_rouge = tk.Button(racine, text="Robot Rouge", command=robot_rouge)
bouton_robot_vert = tk.Button(racine, text="Robot Vert", command=robot_vert)
bouton_robot_jaune = tk.Button(racine, text="Robot Jaune", command=robot_jaune)
bouton_robot_bleu = tk.Button(racine, text="Robot Bleu", command=robot_bleu)
bouton_ligne_verticale = tk.Button(racine, text="Lignes verticales",
command=ligne_verticale)
bouton_ligne_horizontale = tk.Button(racine, text="Lignes horizontales",
command=ligne_horizontale)
bouton_obstacle_croix = tk.Button(racine, text="Obstacle croix",
command=obstacle_croix)
bouton_undo = tk.Button(racine, text="Undo", command=undo)
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)
quadrilage()
bouton_robot_rouge.grid(column=0, row=1)
bouton_robot_vert.grid(column=0, row=2)
bouton_robot_jaune.grid(column=0, row=3)
bouton_robot_bleu.grid(column=0, row=4)
bouton_ligne_verticale.grid(column=0, row=5)
bouton_ligne_horizontale.grid(column=0, row=6)
bouton_undo.grid(column=0, row=7)
bouton_obstacle_croix.grid(column=0, row=8)
canvas.grid(column=1, row=1, columnspan=3, rowspan=20)

racine.mainloop()
