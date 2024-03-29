from tkinter import *
from tkinter.filedialog import *
from modele.arene import *
from math import pi, cos, sin, pow, sqrt
from threading import Thread
class Affichage(Thread):
    """La classe affichage permet de faire le lien entre notre modèle et notre interface graphique.
        Elle utilise notre matrice pour en faire un représentation concrète dans la fenètre graphique.
        :param arene: l'arène dont on souhaite avoir la représentation en graphique
    """
    def __init__(self,arene,fen,robot):
        super(Affichage,self).__init__()
        self.arene=arene
        self.vitesse=10
        self.fen=fen
        self.p=robot
        self.a=robot.calcul_angle()
        self.t=robot.calcul_hypo()
        self.avancer=1
        self.tourner=0

    """Cette fonction sert a dessiner tous les obstacles et le mur de l'arène.
    """
    def afficher(self):
        for i in range(0,self.arene.nb_colonne):
            for j in range(0,self.arene.nb_ligne):
                if self.arene.matrice[j,i]==1:
                    self.zone_dessin.create_rectangle(i,j,i+1,j+1,fill='black')

    """Cette fonction permet de dessiner le robot a l'initialisation.
    Le dessin est fait avec la fonction create_polygon en utilisant les coordonnées du robot.
    """
    def afficher_robot(self):
        p=self.p
        t=self.t
        angle=self.a
        self.r=self.zone_dessin.create_polygon(p.x+t*cos(p.angle+angle),p.y-t*sin(p.angle+angle),p.x+t*cos(p.angle-angle),p.y-t*sin(p.angle-angle),p.x+t*cos(p.angle+angle+pi),p.y-t*sin(p.angle+angle+pi),p.x+t*cos(p.angle-angle+pi),p.y-t*sin(p.angle-angle+pi),fill='red',outline='red')
        self.f=self.zone_dessin.create_line(p.x,p.y,round(50*cos(p.angle+(p.angle_tete-90)*pi/180),1)+p.x,p.y+round(50*sin(-p.angle+(p.angle_tete-90)*pi/180),1),arrow='last',fill='yellow')

    """Cette fonction initialise la zone de dessin, le canvas qui sera utilisé pour dessiner.
    """
    def zone(self):
        self.zone_dessin =Canvas(self.fen, width=self.arene.nb_colonne,height=self.arene.nb_ligne,background='white')
        #self.zone_dessin.focus_set()
        #self.zone_dessin.bind('<Key>',clavier)
        self.zone_dessin.pack()

    def dessiner(self):
        """Cette fonction permet de bouger l'image du robot et de sa fleche selon les coordonnée du robot.
        """
        p=self.p
        t=self.t
        angle=self.a
        self.zone_dessin.coords(self.r,int(p.x+t*cos(p.angle+angle)),int(p.y-t*sin(p.angle+angle)),int(p.x+t*cos(p.angle-angle)),int(p.y-t*sin(p.angle-angle)),int(p.x+t*cos(p.angle+angle+pi)),int(p.y-t*sin(p.angle+angle+pi)),int(p.x+t*cos(p.angle-angle+pi)),int(p.y-t*sin(p.angle-angle+pi)))
        self.zone_dessin.coords(self.f,int(p.x),int(p.y),int(round(50*cos(p.angle),1)+p.x),int(p.y+round(50*sin(-p.angle),1)))
    """Update l'affichage selon les mouvements du robots et laisse une trace sur l'arène.
    """
    def update(self):
        self.z.zone_dessin.create_rectangle(self.p.x,self.p.y,self.p.x+1,self.p.y+1,fill='green')
        self.z.dessiner()

    """Fonction pour le thread qui lance l'update de l'affichage avec un temps d'attente entre les update successifs.
    """
    def run(self):
        while True:
            self.update()
            time.sleep(1./50)
