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
    global objects
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval (( x,y), (x+40, y+40),
    fill="red"))

def robot_vert():
    global objects
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval (( x,y), (x+40, y+40),
    fill="green" ))

def robot_jaune():
    global objects
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval((x,y), (x+40, y+40),
    fill = "yellow"))

def robot_bleu():
    global objects
    x = random.randint(40, 700 + 1)
    y = random.randint(40, 700 + 1)
    objets.append(canvas.create_oval((x,y), (x+40, y+40),
    fill = "blue"))

def ligne_verticale():
    x = random.randint(40, 700+1)
    y = random.randint(40, 700+1)
    objets.append(canvas.create_line((250, 0), (250, 500), fill="white")

def undo():
    global objets
    canvas.delete(objets[-1:])
    objets = objets[:-1]

bouton_robot_rouge = tk.Button(racine, text="Robot Rouge", command=robot_rouge)
bouton_robot_vert = tk.Button(racine, text="Robot Vert", command=robot_vert)
bouton_robot_jaune = tk.Button(racine, text="Robot Jaune", command=robot_jaune)
bouton_robot_bleu = tk.Button(racine, text="Robot Bleu", command=robot_bleu)
bouton_undo = tk.Button(racine, text="Undo", command=undo)
bouton_ligne_verticale = tk.Button(racine, text="Lignes verticales",
command=ligne_verticale)
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)
quadrilage()
bouton_robot_rouge.grid(column=0, row=1)
bouton_robot_vert.grid(column=0, row=2)
bouton_robot_jaune.grid(column=0, row=3)
bouton_robot_bleu.grid(column=0, row=4)
bouton_undo.grid(column=1, row=0)
bouton_ligne_verticale.grid(column=2, row=0)
canvas.grid(column=1, row=1, columnspan=3, rowspan=20)

racine.mainloop()
