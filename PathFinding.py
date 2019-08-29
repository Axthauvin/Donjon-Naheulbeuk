from tkinter import *
import random
from PIL import Image, ImageTk
import os
from playsound import playsound


f = open("Profiles.txt")
lines = f.readlines()
#Exemple: Whatprofile 1 donne le premier profil
WhatProfile = 1
WhatProfile -= 1
NameOfProfile = lines[WhatProfile * 5]
Name = NameOfProfile.split(": ")[1]
Name = Name.split("\n")[0]
ChefDeGroupe = lines[WhatProfile * 5 +2]
ChefName = ChefDeGroupe.split(": ")[1]
ChefName = ChefName.split("\n")[0]
Dungeon = lines[WhatProfile * 5 + 4]
donjon = Dungeon.split(": ")[1]
donjon = donjon.split("\n")[0]
ThePPP = lines[WhatProfile * 5 + 1]
PPP = ThePPP.split(": ")[1]
PPP = PPP.split("\n")[0]
RG = Tk()

RG.attributes('-fullscreen', 1)
RG.configure(background='black')
ws = RG.winfo_screenwidth()
hs = RG.winfo_screenheight()
W = Canvas(RG, width = ws, height = hs, bg = "black")
W.pack()

path = str(os.getcwd()) + "/Persos/"



#|Informations sur le joueur |
PlayerIcone = W.create_rectangle(20, 20, 150, 120, fill = "darkgrey")
PlayerInfoBG = W.create_rectangle(140, 50, 400, 80, fill = "darkgrey", outline = "darkgrey")
#Fin rectangle en triangle
PlayerInfoBG2 = W.create_polygon(400, 50, 400, 80, 430, 50, fill = "darkgrey", outline = "darkgrey")
PlayerName = W.create_text(150, 55, text = Name, font="Folkard 15 italic bold", fill = "White", anchor = NW)





#Informations générales
image = Image.open(PPP)
image = image.resize((110, 80), Image.ANTIALIAS)
image.save('PlayerPP.png') 
img2P = ImageTk.PhotoImage(file = "PlayerPP.png")
PlayerImage = W.create_image(30, 30, anchor = NW, image = img2P)
Canvas.image = img2P
#Donjon
DungeonBG = W.create_rectangle(220, 135, 360, 160, fill = "darkgrey")
DonjonNumber = W.create_text(235, 137.5, text = "Donjon n° " + donjon, font="Folkard 13 italic bold", fill = "White", anchor = NW)



#Informations sur le personnage selectionné
#Nom Perso
PlayerCharacterNameBG = W.create_rectangle(220, 100, 385, 125, fill = "darkgrey", outline = "black")
CharacterName = W.create_text(235, 102.5, text = "Toute la companie", font="Folkard 13 italic bold", fill = "White", anchor = NW)
PlayerInfoBG2 = W.create_polygon(385, 100, 385, 125, 400, 100, fill = "darkgrey", outline = "black")
PlayerCharacterNameBGPetirCarré = W.create_rectangle(384, 101, 386, 124, fill = "darkgrey", outline = "darkgrey")

#Fond pièce
image = Image.open(path + "FondPersos.png")
FondPersos2 = ImageTk.PhotoImage(image)
PlayerCharacterBG = W.create_image(140, 80, anchor = NW, image = FondPersos2)
Canvas.image = FondPersos2


#Image perso
#image = Image.open(path + ChefName + ".png")
#Toute la companie est sélectionnée par défaut
image = Image.open(path + "AllGroup.png")
imgP = ImageTk.PhotoImage(image)
Character = W.create_image(150, 85, anchor = NW, image = imgP)
Canvas.image = imgP








def Aléfloor():
	Number = random.randint(0,2)
	path4 = (os.getcwd() + "/Dungeons/Dalles/")
	if Number == 0:
		return path4 + "Dalle0.png"
	if Number == 1:
		return path4 + "Dalle1.png"
	if Number == 2:
		return path4 + "Dalle2.png"
Aléfloor()
Orientation = []
def FindFloor(Quoi):
	global Orientation
	if Quoi == "a":
		return "Dalle"

	elif Quoi == "s":
		return "Stairs1"

	elif Quoi == "S":
		return "Stairs2"

	elif Quoi == "e":
		return "EnigmeU"
	elif Quoi == "E":
		return "EnigmeD"
	else:
		return "Mur"

		


#Création du donjon
path2 = (os.getcwd() + "/Dungeons/Dalles/")
f = open(os.getcwd() + "/Dungeons/Textes/Donjon" + donjon + ".txt")
DonjonPart = f.readlines()
#==================================
#			PATH FINDING
#==================================

def PathFinding(event):
	Targetx = event.x
	Targety = event.y
	Myx = int(W.coords("Player")[0])
	Myy = int(W.coords("Player")[1])

	#Arrondi le x du clic
	XChanged = str(Targetx)
	if Targetx >= 100:
		XChanged = XChanged[1] + XChanged[2]
	XChanged = int(XChanged)
	if XChanged >= 50:
		TargetxArrondi = Targetx + (50 - XChanged)
	else:
		TargetxArrondi = Targetx - XChanged
	print(TargetxArrondi)

	#Arrondi le y du clic
	YChanged = str(Targety)
	YChanged = YChanged[1] + YChanged[2]
	YChanged = int(YChanged)
	if YChanged >= 50:
		TargetyArrondi = Targety + (50 - YChanged)
	else:
		TargetyArrondi = Targety - YChanged
	print(TargetyArrondi)
	So = FindFloor(DonjonPart[int(TargetyArrondi / 50 - 4)][int(TargetxArrondi / 50)])
	if So == "Mur":
		playsound(os.getcwd() +  '/Sounds/Un cul de sac.mp3')
	else:
		Find = False
		ToFind = []
		OldFind = [(Myx, Myy, Myx, Myy, 0)]
		#Mettre la boucle ici :)
		while Find == False:
			for j in range(0, len(OldFind)):
				for i in range(0, 4):
					last = len(ToFind) - 1
					if i*90 == 0:
						ToFind.append((OldFind[j][0], OldFind[j][1] - 50, OldFind[j][0], OldFind[j][1], OldFind[j][4] + 1))
						So = FindFloor(DonjonPart[int(ToFind[last][1] / 50 - 5)][int(ToFind[last][0] / 50)])
					if i*90 == 90:
						ToFind.append((OldFind[j][0] + 50, OldFind[j][1], OldFind[j][0], OldFind[j][1], OldFind[j][4] + 1))
						So = FindFloor(DonjonPart[int(ToFind[last][1] / 50 - 4)][int(ToFind[last][0] / 50 + 1)])
					if i*90 == 180:
						ToFind.append((OldFind[j][0], OldFind[j][1] + 50, OldFind[j][0], OldFind[j][1], OldFind[j][4] + 1))
						So = FindFloor(DonjonPart[int(ToFind[last][1] / 50 - 3)][int(ToFind[last][0] / 50)])
					if i*90 == 270:
						ToFind.append((OldFind[j][0] - 50, OldFind[j][1], OldFind[j][0], OldFind[j][1], OldFind[j][4] + 1))
						So = FindFloor(DonjonPart[int(ToFind[last][1] / 50 - 4)][int(ToFind[last][0] / 50 - 1)])
					last = len(ToFind) - 1
					if So == "Mur":
						ToFind.pop(len(ToFind) - 1)
					else:
						if ToFind[last][0] == TargetxArrondi:
							if ToFind[last][1] == TargetyArrondi:
								Find = True
								print("J'ai trouvé la cible en " + str(ToFind[last][4]) + " coups.")
								if ToFind[last][4] >= 4:
									print("C'est trop loin")
								else:
									print("Go")
				OldFind = ToFind
				ToFind = []

			



LesImages = []
def Generate(x, y):
	global LesImages
	def AddImage(ImageTogenerate):
		global LesImages
		ImageTogenerate2 =(os.getcwd() + "/Dungeons/Dalles/" + ImageTogenerate)
		PictureGenerate2 = Image.open(ImageTogenerate2)
		MySolToGenerate2 = ImageTk.PhotoImage(PictureGenerate2)
		LesImages.append(MySolToGenerate2)
	#Ajoute à une liste l'Image Mur
	AddImage("Wall.png")
	#Ajoute à une liste l'Image Dalle1
	AddImage("Dalle1.png")
	#Ajoute à une liste l'Image Dalle2
	AddImage("Dalle2.png")
	#Ajoute à une liste l'Image Dalle3
	AddImage("Dalle3.png")
	#Ajoute à une liste l'Image Dalle4
	AddImage("Dalle4.png")
	#Ajoute à une liste l'Image Enigme
	AddImage("EnigmeL.png")
	#Ajoute à une liste l'Image Enigme
	AddImage("EnigmeU.png")
	#Ajoute à une liste l'Image Stairs1
	AddImage("Stairs1.png")
	#Ajoute à une liste l'Image Stairs2
	AddImage("Stairs2.png")

	for j in range(0, round(hs / 50)):
		for i in range(0, round(ws / 50) + 1):
			FindText = DonjonPart[j][i]
			Sol = FindFloor(FindText)
			if Sol == "Dalle":
				#Met une image aléatoire pour chaque dalle
				x = random.randint(1,4)
				#Créer une dalle avec l'image
				W.create_image(i*50, j*50 + 200, anchor = NW, image = LesImages[x], tags = "Floor")
				Canvas.image = LesImages[x]
			if Sol == "Mur":
				#Créer un mur
				W.create_image(i*50, j*50 + 200, anchor = NW, image = LesImages[0], tags = "Wall")
				Canvas.image = LesImages[0]
			if Sol == "Stairs1":
				#Créer un escalier gauche
				W.create_image(i*50, j*50 + 200, anchor = NW, image = LesImages[len(LesImages) - 2], tags = "Stairs")
				Canvas.image = LesImages[len(LesImages) - 2]
			if Sol == "Stairs2":
				#Créer un escalier Droit
				W.create_image(i*50, j*50 + 200, anchor = NW, image = LesImages[len(LesImages) - 1], tags = "Stairs")
				Canvas.image = LesImages[len(LesImages) - 1]
			if Sol == "EnigmeU":
				#Créer un escalier Droit
				W.create_image(i*50, j*50 + 200, anchor = NW, image = LesImages[len(LesImages) - 3], tags = "EnigmeUp")
				Canvas.image = LesImages[len(LesImages) - 3]
			

def GetPosition(x, y):
	global Orientation
	global LeSol
	FindText = DonjonPart[y][x]
	Sol = FindFloor(FindText)
	if Sol == "Dalle":
		Orientations = [0, 90, -90, 180]
		LeSol = Aléfloor()
		Picture = Image.open(LeSol)
		MySol = ImageTk.PhotoImage(Picture)
		Piece = W.create_image(ws / 2, hs / 2, anchor = CENTER, image = MySol, tags = "Floor")
		Canvas.image = MySol
	Generate(x, y)



def Talk():
	pass

Picture = ""
PannelImage = ""
def Consigne(Title, text, ImageExplanation):
	global PannelImage
	global PannelTitle
	global Pannel
	global Picture
	global BoutonV
	path3 = (os.getcwd() + "/Dungeons/Pannels/")
	Picture = Image.open(path3 + "UiFond.png")
	Pannel = ImageTk.PhotoImage(Picture)
	Image2 = W.create_image(ws / 2, hs / 2 , anchor = CENTER, image = Pannel, tags = "Pannel")
	W.image = Pannel
	path3 = (os.getcwd() + "/Dungeons/Pannels/")
	TitreImage = Image.open(path3 + "UiFondTitle.png")
	PannelTitle = ImageTk.PhotoImage(TitreImage)
	Image0 = W.create_image(ws / 2, hs / 2  - 290, anchor = CENTER, image = PannelTitle, tags = "Pannel")
	W.image = PannelTitle
	Titre = W.create_text(ws / 2, hs / 2 - 280, anchor = CENTER, text = Title, tags = "Pannel", font="Folkard 20", fill = "White")
	Texte = W.create_text(ws / 2 - 400, hs / 2 - 150 , anchor = NW, text = text, tags = "Pannel", font="Folkard 20", fill = "black")
	if ImageExplanation != "/":
		Explanation = Image.open(path3 + ImageExplanation)
		PannelImage = ImageTk.PhotoImage(Explanation)
		Image2 = W.create_image(ws / 2, hs / 2 + 100, anchor = CENTER, image = PannelImage, tags = "Pannel")
	ImageBouton = Image.open(path3 + "CloseButton.png")
	BoutonV = ImageTk.PhotoImage(ImageBouton)
	Bouton = W.create_image(ws / 2 + 373.5, hs / 2 - 223.5 , anchor = CENTER, image = BoutonV, tags = ("Pannel", "Ok"))
	def ClosePannel(*args):
		W.delete("Pannel")
	W.tag_bind("Ok","<Button-1>", ClosePannel)

#Position par defaut : 0, 10 (Le minimum 0, 0)
Px = 1
Py = 0
GetPosition(Px, Py)
MyImage = Image.open(os.getcwd() + "/Persos/" + ChefName + ".png")
MyImage = MyImage.resize((50, 50), Image.ANTIALIAS)
MyImage.save('ActualChefDeGroupe.png') 
CaracterImage = ImageTk.PhotoImage(file = 'ActualChefDeGroupe.png')
Perso = W.create_image(50, 250, anchor = NW, image = CaracterImage, tags = "Player")
W.bind('<Button-1>', PathFinding)
#Consigne("Bienvenue sur le jeu du\nDonjon de Naheulbeuk","Pour commencer, utilisez les touches fléchées pour vous déplacer.","Touches.png")
W.tag_lower("Floor")
RG.mainloop()