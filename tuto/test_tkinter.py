from tkinter import *


Arene = Tk()#creer une fenetre
Arene.title('Arene')#donner un nom à la fenetre
Arene.geometry("500x500")#donner la taille de la fenetre
#---------------------------------------------------------------------------------------------
bouton = Button(Arene, text ="Quitter",command=Arene.destroy)#creation d'un bouton
bouton.pack()#inserer le bouton dans la fenetre
#---------------------------------------------------------------------------------------------
texte = Label(Arene, text = "FiveGuys")#creer un text
texte['fg'] = 'red'#assigner la couleur rouge au text --- remplacer fg par bg pour couleur de fond
texte.pack()#inserer le texte


#OU BIEN

#voir dans fonction Canvas avec zone de dessin


#---------------------------------------------------------------------------------------------
Entree = Entry(Arene)#creer une ligne de saisie (servant à rien pour linstant)
Entree.pack()#inserer la ligne de saisie
#--------------------------------------------------------------------------------------------
zone_dessin =Canvas(Arene, width=300, height=300)#creer une zone de dessin
zone_dessin.pack()#inserer la zone de dessin
zone_dessin.create_line(0,0,300,300)#creer une ligne à partir de deux points
zone_dessin.create_rectangle(100,100,200,200)#creer un rectangle à partir de deux point
zone_dessin.create_text(200,380, text = "Robot",fill = 'black')#creation text
#creer une zone de dessin est obligatoire avant de pouvoir dessiner( logique)



Arene.mainloop()#obligatoire


