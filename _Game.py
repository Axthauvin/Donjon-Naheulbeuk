import time
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from functools import partial
from tkinter.filedialog import askopenfilename
import os.path
from playsound import playsound


Open = "No"
imgP = ""
def RealGame(WhatProfile):
	global imgP
	#Récupère les infos relatives au profil
	f = open("Profiles.txt")
	lines = f.readlines()
	WhatProfile = int(WhatProfile)
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
	RG = Toplevel()

	RG.attributes('-fullscreen', 1)
	RG.configure(background='black')
	ws = RG.winfo_screenwidth()
	hs = RG.winfo_screenheight()
	W = Canvas(RG, width = ws, height = hs, bg = "black")
	W.pack()

	PlayerInfoBG = W.create_rectangle(140, 100, 320, 130, fill = "darkgrey", outline = "darkgrey")
	PlayerCharacterNameBG = W.create_rectangle(120, 140, 300, 165, fill = "darkgrey", outline = "darkgrey")
	DungeonBG = W.create_rectangle(120, 170, 300, 195, fill = "darkgrey")
	PlayerCharacterBG = W.create_oval(100, 140, 180, 220, fill = "darkgrey")

	path = "C:/Users/Axel/Desktop/Le saint dossier/Code/Python/Programmes/Donjon & Naheulbeuk/Persos/"
	image = Image.open(path + ChefName + ".png")
	imgP = ImageTk.PhotoImage(image)
	Character = W.create_image(105, 140, anchor = NW, image = imgP)
	Canvas.image = imgP

	PlayerInfoBG2 = W.create_polygon(320, 130, 320, 100, 335, 110, fill = "darkgrey", outline = "darkgrey")

	PlayerIcone = W.create_oval(50, 50, 150, 150, fill = "darkgrey")

	image = Image.open(PPP)
	image = image.resize((80, 80), Image.ANTIALIAS)
	image.save('PlayerPP.png') 
	img2P = ImageTk.PhotoImage(file = "PlayerPP.png")
	Character = W.create_image(100, 110, anchor = CENTER, image = img2P)
	Canvas.image = img2P
	PlayerName = W.create_text(150, 105, text = Name, font="Folkard 15 italic bold", fill = "White", anchor = NW)
	CharacterName = W.create_text(230, 155, text = ChefName, font="Folkard 13 italic bold", fill = "White", anchor = CENTER)
	DonjonNumber = W.create_text(235, 185, text = "Donjon n° " + donjon, font="Folkard 13 italic bold", fill = "White", anchor = CENTER)





	RG.mainloop()
	
	


imgPl = []
Playl = []
def _Game():
	global Open
	global Game
	global canvas
	Game = Tk()

	def Quit(*args):
		Game.quit()
	def New(*args):
		Create = Toplevel()
		labelframe = LabelFrame(Create, text="Créer une nouvelle compagnie", padx=30, pady=20)
		labelframe.pack(fill="both", expand="yes")
		
		ToWrite = []
		L1 = Label(labelframe, text="Choisir un nom de compagnie")
		L1.grid(row = 0)

		Name = Entry(labelframe)
		Name.grid(row = 1)

		L5 = Label(labelframe, text="Choisir votre chef de groupe")
		L5.grid(row = 2)


		Chef = ttk.Combobox(labelframe, values=["Ranger", "Magicienne", "Voleur", "Nain", "Barbare", "Elfe", "Ogre (Déconseillé)", "Ménestrel"])
		Chef.set("Ranger")
		Chef.grid(row = 3)

		L2 = Label(labelframe, text="")
		L2.grid(row = 4)

		filepath  = ""
		filename  = ""
		L3 = Label(labelframe, text = "Les dimensions de l'image doivent être de 200x200" + filename)
		FILETYPES = [ ("Images", "*.png") ]
		W = Canvas(labelframe, width = 200, height = 200)

		def set_filename():
			filepath = askopenfilename(filetypes=FILETYPES, initialdir=r'C:/Users')
			ToWrite.append(filepath)
			image = Image.open(filepath)
			Fond = ImageTk.PhotoImage(image)
			item = W.create_image(0, 0, anchor = NW, image = Fond)
			W.image = Fond
			filep = filepath.split("/")
			filename = filep[len(filep) - 1]
			L3.config(text = filename)

			Create.lift()
			return filepath

		
		
		
		Difficultée = ttk.Combobox(labelframe, values=["Bouseux (Facile)" , "Aventurier (Normal)", "Expert (Cauchemard)"])
		def Create_Profile():
			PName = Name.get()
			filepath = ToWrite[len(ToWrite) - 1]
			CDG = Chef.get()
			
			f = open("Profiles.txt","a+")

			f.write("Compagnie: " + Name.get() + "\n" )
			f.write("Image: " + filepath + "\n" )
			if CDG == "Ogre (Déconseillé)":
				CDG = "Ogre"
			f.write("Chef: " + CDG + "\n")
			f.write("Difficultée: " + Difficultée.get() + "\n")
			f.write("Donjon: 0\n")
			Create.destroy()

		B2 = Button(labelframe, text = "Choisir l'image de profil", command = set_filename)
		B2.grid(row = 5)

		L3.grid(row = 6)

		L4 = Label(labelframe, textvariable = "")
		L4.grid(row = 7)

		image = Image.open("Default.png")
		Fond = ImageTk.PhotoImage(image)
		item = W.create_image(0, 0, anchor = NW, image = Fond)
		W.image = Fond
		W.grid(row = 8)
		
		
		L5 = Label(labelframe, text="Vous êtes un :")
		L5.grid(row = 9)

		
		Difficultée.set("Bouseux (Facile)")
		Difficultée.grid(row = 10)
		

		B1 = Button(labelframe, text = "Valider & Fermer", command = Create_Profile)
		B1.grid(row = 11, column = 0)
		B2 = Button(labelframe, text = "Annuler", command = Create.destroy)
		B2.grid(row = 11, column = 1)

		Create.title("Create")
		
		Create.focus_set()
		Create.overrideredirect(True)

		Create.lift()
		Create.mainloop()
		
	

	
	def OpenLevels(*args):
		global Open
		global canvas
		global canvas
		global imgPl
		if Open == "No":
			canvas.itemconfig("Continuer", state = "normal")
			canvas.itemconfig("Erreur", state = "hidden")
			Open = "Yes"
			f = open("Profiles.txt")
			def file_len(fname):
				with open(fname) as f:
					i = 0
					for i, l in enumerate(f):
						pass
				return i + 1
			Hauteur1 = 495
			if file_len("Profiles.txt") == 1:
				canvas.create_text(ws - 690, hs - 495, text = "Vous devez vous créer au moins \n une compagnie pour jouer. \n Ou alors, rechargez vos compagnies \n ici :", font="Folkard 15 ", fill = "White", anchor = NW, tags = ("Continuer", "Erreur"))
				canvas.create_rectangle(ws - 660, hs - 350, ws - 500, hs - 300, fill = "Grey", tags = ("Continuer", "Erreur", "Reload"))
				canvas.create_text(ws - 650, hs - 340, fill = "White", text = "Recharger", font="Folkard 20  ",  anchor = NW, tags = ("Continuer", "Erreur", "Reload"))
				canvas.create_text(ws - 690, hs - 280, text = "Ou alors, créer vous une \nnouvelle compagnie ici :       → ", font="Folkard 15 ", fill = "White", anchor = NW, tags = ("Continuer", "Erreur"))

				
			else:
				NumberOfProfiles = file_len("Profiles.txt") / 5
				lines = f.readlines()
				for x in range(0, int(NumberOfProfiles)):
					#Afficher le nom + le contour
					NameOfProfile = lines[x * 5]
					Name = NameOfProfile.split(": ")[1]
					Name = Name.split("\n")[0]
					canvas.create_rectangle(ws - 695, hs - Hauteur1, ws - 355, hs - Hauteur1 + 157, fill = "darkgrey", tags = "Continuer")
					canvas.create_text(ws - 680, hs - Hauteur1 + 10, text = Name, font="Folkard 20 italic bold", fill = "White", anchor = NW, tags = "Continuer")

					#Afficher l'image ========================= Donjon
					image = Image.open("DonjonLogo.png")
					imgP = ImageTk.PhotoImage(image)
					canvas.create_image(ws - 680, hs - Hauteur1 + 40, anchor = NW, image = imgP, tags = "Continuer")
					imgPl.append(imgP)
					Canvas.image = imgPl[x]
					

					#Avoir les informations de profil
					#| N° du donjon|
					Dungeon = lines[x * 5 + 4]
					donjon = Dungeon.split(": ")[1]
					donjon = donjon.split("\n")[0]
					canvas.create_text(ws - 630, hs - Hauteur1 + 40, text = "Progression: Donjon n°" + donjon, font="Folkard 12 italic bold", fill = "White", anchor = NW, tags = "Continuer")
					#|Chef de groupe|
					ChefG = lines[x * 5 + 2]
					RealC = ChefG.split(": ")[1]
					RealC = RealC.split("\n")[0]
					canvas.create_text(ws - 630, hs - Hauteur1 + 60, text = "Chef de groupe: " + RealC, font="Folkard 12 italic bold", fill = "White", anchor = NW, tags = "Continuer")
					#|Difficultée|
					Difficultée = lines[x * 5 + 3]
					Diff = Difficultée.split(": ")[1]
					Diff = Diff.split("\n")[0]
					Diff = Diff.split(" ")[0]
					canvas.create_text(ws - 630, hs - Hauteur1 + 80, text = "Difficulté: " + Diff, font="Folkard 12 italic bold", fill = "White", anchor = NW, tags = "Continuer")
					#|Bouton pour jouer|
					image = Image.open("Playbutton.png")
					Play = ImageTk.PhotoImage(image)
					canvas.create_image(ws - 650, hs - Hauteur1 + 100, anchor = NW, image = Play, tags = ("Continuer", str(x), "Playbutton"))
					Playl.append(Play)
					Canvas.image = Playl[x]
					Hauteur1 -= 160

		else :
			canvas.itemconfig("Continuer", state = "hidden")
			Open = "No"

		
	def click(event):
		if canvas.find_withtag(CURRENT):
			tags = canvas.itemcget(CURRENT, "tags")
			Who = tags.split(" ")
			ProfileToLoad = Who[1]
			RealGame(ProfileToLoad)
			

        
	def Reaload(*args):
		global Open
		f = open("Profiles.txt")
		def file_len(fname):
			with open(fname) as f:
				i = 0
				for i, l in enumerate(f):
					pass
			return i + 1
		Hauteur1 = 495
		if file_len("Profiles.txt") == 1:
			messagebox.showinfo("Erreur", "Vous n'avez aucun profils à charger. Si vous les avez perdu, bien fait pour vous. \nNAH !")
		else:
			print("Reload done")
			Open = "No"
			OpenLevels()


	Game.attributes('-fullscreen', 1)
	Game.configure(background='black')
	ws = Game.winfo_screenwidth()
	hs = Game.winfo_screenheight()
	
	img = Image.open('Test.png')
	img = img.resize((ws, hs), Image.ANTIALIAS)
	img.save('Real.png') 
	Fond = PhotoImage(file='Real.png')

	canvas = Canvas(Game, width = ws, height = hs)
	
	item = canvas.create_image(ws / 2 , hs / 2, anchor = CENTER, image = Fond)
	canvas.image = Fond

	Open = "No"
	OpenLevelsFond = canvas.create_rectangle(ws - 700, hs - 500, ws - 350, hs - 10,fill = "black", state = "hidden", tags = "Continuer")
	TitleP = canvas.create_rectangle(ws - 700, hs - 550, ws - 525, hs - 500, fill = "black",  state = "hidden", tags = "Continuer")
	TitlePText = canvas.create_text(ws - 690, hs - 540, fill = "White",  state = "hidden", text = "Profiles" , font="Folkard 20 italic bold", anchor = NW, tags = "Continuer")
	ContinueF = canvas.create_rectangle(ws - 310, hs - 300, ws - 175, hs - 270,fill = "black", tags = "Continue")
	ContinueB = canvas.create_text(ws - 300, hs - 300, text = "Continuer", font="Folkard 20 italic bold", fill = "White", anchor = NW, tags = "Continue")
	canvas.tag_bind("Continue","<Button-1>", OpenLevels)

	canvas.tag_bind("Playbutton","<Button-1>", click)
	canvas.tag_bind("Reload","<Button-1>", Reaload)


	NouveauF = canvas.create_rectangle(ws - 310, hs - 250, ws - 60, hs - 220,fill = "black", tags = "Nouveau")
	NouveauB = canvas.create_text(ws - 300, hs - 250, text = "Nouvelle compagnie", font="Folkard 20 italic bold", fill = "White", anchor = NW, tags = "Nouveau")
	canvas.tag_bind("Nouveau","<Button-1>", New)

	QuitF = canvas.create_rectangle(ws - 310, hs - 200, ws - 210, hs - 170,fill = "black", tags = "Quit")
	QuitB = canvas.create_text(ws - 300, hs - 200, text = "Quitter", font="Folkard 20 italic bold", fill = "White", anchor = NW, tags = "Quit")
	canvas.tag_bind("Quit","<Button-1>", Quit )

	canvas.pack()
	Game.mainloop()
Root = Tk()
Root.title("Donjon de Naheulbeuk")
Root.overrideredirect(True)
w = 400
h = 200
ws = Root.winfo_screenwidth()
hs = Root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
Root.geometry('%dx%d+%d+%d' % (w, h, x, y))
W = Canvas(Root, width=w, height=h)
Fond = PhotoImage(file='Donjon de Naheulbeuk.png')
item = W.create_image(0, 0, anchor = NW, image = Fond)
W.image = Fond
W.pack()
Secs = 0
def maj():
	global Secs
	Secs = Secs + 1
	if Secs == 3:
		Secs = 0
		Root.destroy()
		time.sleep(1)
		_Game()
	Root.after(1000, maj)
maj()
Root.mainloop()