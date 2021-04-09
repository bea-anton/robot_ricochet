#############################################
#groupe MIASHS 1
#Alae KARTOUT
#Basma BAGNAH AMADOU
#Yacine
#Victor
#Beatriz ANTON ARTAZA
# https://github.com/bea-anton/projet_incendie.git
##############################################

##############################################
# import des librairies 

import tkinter as tk
import random

#############################################

COULEUR_FOND = "rosybrown"
COULEUR_QUADR = "grey"
COULEUR_MUR="black"

LARGEUR = 800
HAUTEUR = 800
COTE = 50
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE

tableau = None

##############################################
# fonctions

def quadrilage():
    """Affiche un quadrilage sur le canvas."""
    x0, x1 =0, LARGEUR
    y = 0
    while y <= HAUTEUR:
        canvas.create_line(x0, y, x1, y, fill=COULEUR_QUADR)
        y += COTE
    y0, y1 = 0, LARGEUR
    x = 0
    while x <= LARGEUR:
        canvas.create_line(x, y0, x, y1, fill=COULEUR_QUADR)
        x += COTE

racine = tk.Tk()
racine.title("Robot Ricochet")
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)
quadrilage()
canvas.grid(column=0, row=0)

racine.mainloop()