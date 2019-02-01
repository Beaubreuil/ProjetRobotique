class Robot(object):
	def __init__(self,x,y,angle):
		self.x=x
		self.y=y
		self.angle=angle
		self.couleur=0 #noir en binaire
		self.largeur=20
		self.longueur=50

	def get_position(self):
		return self.x, self.y


def changement_angle(robot, angle):
    if angle > 0:
        angle = angle%360
    else :
        angle = angle%(-360)
        
    robot.angle += angle

#jeu de test:
a=Robot(0,0,90)
print (a.get_position()==(0,0))
a.x,a.y=a.x+1,a.y+1
print (a.get_position()==(1,1))
print (a.angle==90)

#--------------------------------------------------
#jeu de test (fct changement angle):
changement_angle(a, 30)#ajout de 30°
print(a.angle==90)#False verifie si modification resultat correct
print(a.angle==120)#True verifie si resultat correct

changement_angle(a, -30)#-30°
print(a.angle==90)#True resultat correct
changement_angle(a, 390)#+390 => +30 
print(a.angle==120)#True resultat correct
changement_angle(a, -390)#-390° => -30°
print(a.angle==90)#True resultat correct
changement_angle(a, 0)#angle nul
print(a.angle==90)#True resultat correct
