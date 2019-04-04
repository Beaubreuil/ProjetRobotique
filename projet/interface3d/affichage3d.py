import pyglet
import pyglet.gl as pgl
from PIL.Image import*
from pyglet.window import key
import OpenGL.GL as ogl
from modele.obstacle import*
import math as m
import time
from modele.controleur_robotreel_carre import ControleurRobotReelCarre
from modele.controleur_robotreel_mur import ControleurRobotReelMur
from threading import Thread 


class Affichage(Thread):

    def __init__(self, fenetre3d,arene,robot):
        super(Affichage,self).__init__()
        self.fenetre3d = fenetre3d
        pgl.glClearColor(0, 0, 0, 1)
        pgl.glEnable(pgl.GL_DEPTH_TEST)
        self.r=ObstacleRectangle(0,0,10,50)
        self.robot=robot
        self.arene=arene
        self.x=200
        self.ctrl=ControleurRobotReelMur(self.robot)
        #self.ctrl=ControleurRobotReelCarre(self.robot)

    def draw(self) :
        #z=50 #m.sqrt(self.r.largeur**2+self.r.longueur**2)
        print(self.arene.list_obj)
        for i in self.arene.list_obj:
            i.hauteur=50
            # Effacer la fenetre
            #self.fenetre3d.clear()

            # Creation d'une matrice
            #pgl.glPushMatrix()

            # Debut du dessin
            #pgl.glBegin(ogl.GL_QUADS)
            x=i.x-i.largeur//2
            y=i.y-i.longueur//2

            # Premier carre rouge de derrier
            pgl.glColor3ub(255, 0, 0)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, 0, y)

            # Second carre bleu de gauche
            pgl.glColor3ub(0, 0, 255)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x, 0, y+i.longueur)

            # Troisieme carre vert du dessous
            pgl.glColor3ub(0, 255, 0)
            pgl.glVertex3f(x, 0, y)
            pgl.glVertex3f(x+i.largeur, 0, y)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)
            pgl.glVertex3f(x, 0, y+i.longueur)

            # Quatrieme carre rose de droite
            pgl.glColor3ub(255, 0, 255)
            pgl.glVertex3f(x+i.largeur, 0, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)

            # Cinquieme carre gris fclair du haut
            pgl.glColor3ub(122, 122, 122)
            pgl.glVertex3f(x, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)

            # Sixieme face fonce
            pgl.glColor3ub(40, 40, 40)
            pgl.glVertex3f(x, 0, y+i.longueur)
            pgl.glVertex3f(x, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, i.hauteur, y+i.longueur)
            pgl.glVertex3f(x+i.largeur, 0, y+i.longueur)
            # Fin du dessin
            #pgl.glEnd()

            # Effacer la matrice
            #pgl.glPopMatrix()
            #pgl.glFlush()
    def on_draw(self):
        self.fenetre3d.clear()
        #pgl.glPushMatrix()
        #pgl.glRotatef(self.fenetre3d.xRotation, 0, 1, 0)
        #pgl.glRotatef(0, 0, 1, 1)
        pgl.glBegin(ogl.GL_QUADS)
        #bleu
        pgl.glColor3ub(0, 0, 255)
        pgl.glVertex3f(0, 0, 0)
        pgl.glVertex3f(0,10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        #rouge
        pgl.glColor3ub(255, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne,10, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        #vert
        pgl.glColor3ub(0, 255, 0)
        pgl.glVertex3f(0, 0, self.arene.nb_ligne)
        pgl.glVertex3f(0,10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 10, self.arene.nb_ligne)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        #jaune
        pgl.glColor3ub(255, 255, 0)
        pgl.glVertex3f(00, 0, 00)
        pgl.glVertex3f(00,10, 00)
        pgl.glVertex3f(00, 10, self.arene.nb_ligne)
        pgl.glVertex3f(00, 0, self.arene.nb_ligne)
        
        #blanc
        pgl.glColor3ub(255, 255, 255)
        pgl.glVertex3f(00, 0, self.arene.nb_ligne)
        pgl.glVertex3f(00,0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, 0)
        pgl.glVertex3f(self.arene.nb_colonne, 0, self.arene.nb_ligne)
        
        self.draw()
        pgl.glEnd()
        """kitten = pyglet.image.load('image2.jpg')
        sprite = pyglet.sprite.Sprite(kitten)
        sprite.draw()
        i=open('image2.jpg')
        (largeur, hauteur)= i.size
        for j in range(largeur):
          for k in range(hauteur):
              print(i.getpixel((j,k)))"""
        pgl.glFlush()
    def obstacle (self, robot,originex, originey, arene, pas):
        """Cette fonction permet la détection des obstacles se trouvant sur une demi devant le robot ?
            :param originex: x de l'origine de la demi-droite
            :param origeney: y de l'origine de la demi-droite
            :param arene: arene (matrice) dans lequel se trouve le robot
            :param pas: pas entre chaque avancer sur la demi-droite de détection
            :returns : position x, y de l'obstacle qui permetra le calcul de la distance avec celui-ci
        """
        recherche_x= originex
        recherche_y= originey
        while True:
                    recherche_x+=m.cos(robot.angle)*pas
                    recherche_y-=m.sin(robot.angle)*pas
                    #recherche_x=int(round(recherche_x,0))
                    #recherche_y=int(round(recherche_y,0))
                    if recherche_x<0 or recherche_y<0 or recherche_x>arene.nb_colonne or recherche_y>arene.nb_ligne:
                        return recherche_x, recherche_y
                    if arene.matrice[int(recherche_y), int(recherche_x)]==1:
                        return recherche_x, recherche_y

    def on_resize(self, width, height):

        # Definir le repere (la zone de la fenetre utilisee)
        #pgl.glViewport(0, 0, width, height)

        # Utiliser une projection
        pgl.glMatrixMode(ogl.GL_PROJECTION)
        pgl.glLoadIdentity()
        #self.x-=1
        Ratio = width/height
        pgl.gluPerspective(35, Ratio, 1, 1000)
        x=self.robot.x+m.cos(self.robot.angle)*(self.robot.largeur//2)
        y=self.robot.y-m.sin(self.robot.angle)*(self.robot.longueur//2)
        a,b=self.obstacle(self.robot,self.robot.x,self.robot.y,self.arene,1)
        print(a,b)
        #print(x,y)
        pgl.gluLookAt(x, 10, y, a, 0, b, 0, 1, 0)
        pgl.glMatrixMode(ogl.GL_MODELVIEW)

        #pgl.glTranslatef(0, 0, -400)

    def update(self,dt):
        if not self.ctrl.stop():
            self.ctrl.update()
            self.on_resize(600,600)
            self.on_draw()
            


