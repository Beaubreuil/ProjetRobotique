from Tkinter import * 
from arene import Arene
from robot import Robot
from Obstacle import Obstacle
import math as m

class Affichage(object):
	def __init__(self,arene):	
		fenetre = Tk()#creer une fenetre
		fenetre.title('Arene')#donner un nom  la fenetre
		fenetre.geometry("1000x500")#donner la taille de la fenetre
		#on definit la zone ou on dessine(fenetre,y,x,couleur d'arrier plan)
		#les *5 sont la car la matrice est trop petite sur l'affichage donc chaque case de la matrice correspond a un carree de cote 5 sur l'affichage
		zone_dessin =Canvas(fenetre, width=5*arene.nb_ligne, height=5*arene.nb_colonne,background='white')
		zone_dessin.pack()
		#on parcoure tous les elements de la matrice et on les colorie selon leur valeur
		i=0
		j=0
		while j<arene.nb_colonne:
			i=0
			while i<arene.nb_ligne:
				if arene.matrice[i,j]==1:
					zone_dessin.create_rectangle(i*5,j*5,(i+1)*5,(j+1 )*5,fill='black')
				if arene.matrice[i,j]==2:
					zone_dessin.create_rectangle(j*5,i*5,(j+1)*5,(i+1 )*5,fill='red')
				i=i+1
			j=j+1
		for a in arene.list_rob:
			zone_dessin.create_line(a.x*5,a.y*5,round(100*m.cos(a.angle),1)+a.x*5,a.y*5+round(100*m.sin(-a.angle),1),arrow='last',fill='yellow')
		fenetre.mainloop()

#o=Obstacle(50,80,1)
p=Robot(60,60,m.pi/4)
b=Arene(200,100,[],[p])
p.changer_angle(m.pi/4)
a=Affichage(b)
print p.x,p.y
p.avancer(20)
print p.x,p.y
b=Arene(200,100,[],[p])
a=Affichage(b)

