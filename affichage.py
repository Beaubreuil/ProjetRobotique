from tkinter import *
from arene import Arene
from arene import calcul_hypo
from arene import calcul_angle
from robot import Robot
from obstacle import Obstacle

import math as m
from tkinter.filedialog import *

class Affichage(object):
    def __init__(self,arene):
        self.arene=arene
        self.vitesse=10 

    def afficher(self):
    	for i in range(0,self.arene.nb_ligne):
    		for j in range(0,self.arene.nb_colonne):
    			if self.arene.matrice[i,j]==1:
    				zone_dessin.create_rectangle(i,j,i+1,j+1,fill='black')        
    def afficher_robot(self):
    	r=zone_dessin.create_polygon(p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi),fill='red',outline='red')
    	global r
    	f=zone_dessin.create_line(p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1),arrow='last',fill='yellow')
    	global f
    
    def zone(self):
    	zone_dessin =Canvas(fenetre, width=self.arene.nb_ligne,height=self.arene.nb_colonne,background='white')
    	global zone_dessin
    	zone_dessin.focus_set()
    	zone_dessin.bind('<Key>',clavier)
    	zone_dessin.pack()

      
"""dessiner() permet de bouger l'image du robot et de sa fleche selon les coordonnée du robot """        
def dessiner():
	zone_dessin.coords(r,p.x+t*m.cos(p.angle+angle),p.y-t*m.sin(p.angle+angle),p.x+t*m.cos(p.angle-angle),p.y-t*m.sin(p.angle-angle),p.x+t*m.cos(p.angle+angle+m.pi),p.y-t*m.sin(p.angle+angle+m.pi),p.x+t*m.cos(p.angle-angle+m.pi),p.y-t*m.sin(p.angle-angle+m.pi))
	zone_dessin.coords(f,p.x,p.y,round(50*m.cos(p.angle),1)+p.x,p.y+round(50*m.sin(-p.angle),1))

	"""Fonction qui recoit les touches appuyé par l'utilisateur et effectue des actions pour certaines d'entre elles.
-Touche Up permet d'augmenter la vitesse
-Touche Down permet baisser la vitesse
-Touche Right permet de faire tourner le robot a droite
-Touche Left permet de faire tourner le robot a gauche"""
def clavier(event):
	touche=event.keysym
	print(touche)
	if touche =='Up':
		z.vitesse=z.vitesse+1
	if touche =='Down':
		z.vitesse=z.vitesse-1
	if touche =='Left':
		p.changer_angle(m.pi/10)
		dessiner()
	if touche =='Right':
		p.changer_angle(-m.pi/10)
		dessiner()

arret=False
def main():
    global arret
    if arret==False:
        if p.distancemax(z.arene):
            p.changer_angle(m.pi/7)
        p.avancer(z.vitesse)
        dessiner()
        fenetre.after(50,main)
        
"""Les different Boutons"""
def Demarrer():
    global arret
    if arret==True:
        arret=False
    main()
    
"""Fonction qui permet d'effacer un affichage pour pouvoir en importer un autre"""
def reset():
	zone_dessin.delete(ALL)
	zone_dessin.destroy()

"""Permet de creer a partir d'un fichier une situation donne
Format fichier accepte:
ARENE
nb_ligne
nb_colonne
ROBOT
x
y
angle en degre
OBSTACLE
x
y
forme(un int)
FIN"""

def import_file():
    filepath = askopenfilename(title="Ouvrir un fichier",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filepath,'r')
    ARENE=False
    ROBOT=False
    OBSTACLE=False
    L=[]
    for i in fichier.readlines():
    	if i.strip()=="ARENE":
    		ARENE=True
    		ROBOT=False
    		OBSTACLE=False
    	elif i.strip()=="ROBOT":
    		b=Arene(int(L[0]),int(L[1]))
    		b.cree_mur()
    		L=[]
    		ARENE=False
    		ROBOT=True
    		OBSTACLE=False
    	elif i.strip()=="OBSTACLE":
    		p=Robot(int(L[0]),int(L[1]),m.radians(int(L[2])))
    		global p
    		angle=p.calcul_angle()
    		global angle
    		t=p.calcul_hypo()
    		global t
    		b.inserer_robot(p)
    		L=[]
    		ARENE=False
    		ROBOT=False
    		OBSTACLE=True
    	elif i.strip()=="FIN":
    		a=0
    		while a<len(L):
    			o=Obstacle(int(L[a]),int(L[a+1]),int(L[a+2]))
    			b.inserer_obs(o)
    			a=a+3
    		z=Affichage(b)
    		z.arene=b
    		global z
    		z.zone()
    		z.afficher()
    		z.afficher_robot()
    	elif ARENE:
    		L.append(i.strip())
    	elif ROBOT:
    		L.append(i.strip())
    	elif OBSTACLE:
    		L.append(i.strip())
    	fichier.close()
"""permet de sauvegarder une configuration : creer un nouveau fichier Scenario.txt"""
def export_file():
    f=open('Scenario.txt','w')
    f.write('ARENE\n')
    f.write(str(z.arene.nb_ligne)+'\n')
    f.write(str(z.arene.nb_colonne)+'\n')
    f.write("ROBOT\n")
    for i in z.arene.list_rob:
    	f.write(str(i.x)+'\n')
    	f.write(str(i.y)+'\n')
    	f.write(str(int(m.degrees(i.angle)))+'\n')
    f.write("OBSTACLE\n")
    for i in z.arene.list_obj:
    	f.write(str(i.x)+'\n')
    	f.write(str(i.y)+'\n')
    	f.write(str(i.forme)+'\n')
    f.write("FIN")
    f.close()

def arreter():
    global arret
    arret=True

arret=False

"""cree une fenetre"""
fenetre = Tk()#creer une fenetre
fenetre.title('Arene')#donner un nom  la fenetre

fenetre.geometry("1200x600")
"""creation des different bouton"""
BoutonExporter = Button(fenetre, text ='Exporter', command = export_file)
BoutonExporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonArreter = Button(fenetre, text ='Arreter', command = arreter)
BoutonArreter.pack(side = LEFT, padx = 10, pady = 10)

BoutonGo = Button(fenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

BoutonQuitter = Button(fenetre, text ='Quitter', command = fenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

BoutonImporter = Button(fenetre, text ='Importer', command = import_file)
BoutonImporter.pack(side = LEFT, padx = 10, pady = 10)

BoutonReset = Button(fenetre, text ='Reset', command = reset)
BoutonReset.pack(side = LEFT, padx = 10, pady = 10)

"""creation de case avec des informations a l'interieur"""
label = Label(fenetre, text="x y", bg="yellow")
label.pack()

fenetre.mainloop()


