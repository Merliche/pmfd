import os
import tkinter.font as font
from tkinter import *
import sys
import sqlite3 
from functools import partial
from tkinter import messagebox



##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Cartes des distributeurs de billet')
fen.geometry("1900x1063")
#fen.attributes('-fullscreen',True)
choix_banque = IntVar()
solde = IntVar()
historique = IntVar()
retrait = IntVar()






    
##----- Création du canevas -----##
dessin = Canvas(fen, width = 1900, height = 1790, bg = 'white')
dessin.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3)

#Chemin absolu vers image
'''h:/NSI/Projet/distributeur-billet-main/''' 

path_map= os.path.abspath('banque/mapboubou.gif')
path_populaire = os.path.abspath('banque/populaire.gif')
path_cic = os.path.abspath('banque/cic.gif')
path_societegenerale = os.path.abspath('banque/societegenerale.gif')
path_postale = os.path.abspath('banque/LaBanquePostale.gif')



##----- Dessiner dans le canevas -----##
im = PhotoImage(file = path_map, master=fen)
im2 = PhotoImage(file = path_populaire, master=fen)
im3 = PhotoImage(file = path_cic, master=fen)
im4 = PhotoImage(file = path_societegenerale, master=fen)
im5 = PhotoImage(file = path_postale, master=fen)
logo1 = dessin.create_image(650, 400, image = im )
logo2 = dessin.create_image(1600, 150, image = im2 )
logo3 = dessin.create_image(1600, 420, image = im3 )
logo4 = dessin.create_image(1600, 620, image = im4 )
logo5 = dessin.create_image(1600, 820, image = im5 )
ligne1 = dessin.create_line(1460, 225, 650, 400, width=4, fill='#000000')
ligne2 = dessin.create_line(1490, 425, 750, 500, width=4, fill='#000000')
ligne3 = dessin.create_line(1490, 625, 700, 585, width=4, fill='#000000')
ligne4 = dessin.create_line(1490, 825, 520, 685, width=4, fill='#000000')










def afficher_informations():
    pass
    


def afficher_solde(identifiants):
    conn = sqlite3.connect('my_DB.db')
    cur = conn.cursor()
    solde = cur.execute("SELECT Solde FROM utilisateursWHERE CB=?", (identifiants,))
    conn.close
    cur.close
    Solde = Label(fen, text="Votre solde est :"+str(solde))
    Solde.grid()
    return solde
    

def afficher_historique():
    pass

def check_for_money():
    pass
#verifier si argent sur solde en faisant solde - demande de retrait
#si resultat <0 mettre une box d'info d'erreur et demander de recommencer ou si ca te fait chier juste detruit la fenetre
#si >0 alors mettre image ou gif d'argent qui sors du truc qui fait sortir l'argent



def give_money(user_solde, retrait):
    if user_solde - retrait < 0:
        messagebox.showerror("error", "try again")
        return afficher_retrait
    else:
        messagebox.askyesnocancel(title="None", message="Etes-vous sur de votre choix?" )


give_money(150,40)

def ask_for_amount():
    pass

 
#def afficher_depot():
#   pass


#def effectuer_transfert():
#    pass


def Quitter():
    sys.exit()



path_fond = os.path.abspath('banque/ecrandistributeur.gif')
bg = PhotoImage(file = path_fond)
fond_distrib = PhotoImage(file= path_fond)





'''

    Button_Connexion = Button(fen,text ='Se connecter',bg='#F0EBE9',\
                        fg='black',font=("Arial",30),activeforeground='white',\
                        activebackground='#048B9A',command= None)

'''
def CreateNewFen():
    
#destruction de l'ancienne image de fond, du texte et du bouton
    dessin.delete(ALL)
    Bouton_valider.destroy()
    banque4.destroy()
    banque1.destroy()
    banque3.destroy()
    banque2.destroy()
    
#création d'une nouvelle fenêtre avec une nouvelle taille
    fen.title("Bienvenue sur le distributeur")
    fen.geometry("1900x1563")
    fen.resizable(width=True,height=True)
    
    dessin.create_image(450,100,image = bg,anchor ='nw')
    dessin.create_text(500,25,text="Bienvenue sur ce distributeur",\
                                 font=("Arial",50, "bold"),anchor='nw')
    dessin.create_text(629,550,text="Retrait",\
                                 font=("Arial",22, "bold"),anchor='nw')
#   dessin.create_text(931,510,text="Dépot",\
#                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(638,635,text="Solde",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(931,550,text="Historique",\
                                 font=("Arial",22, "bold"),anchor='nw')
#    dessin.create_text(931,635,text="Transfert",\
#                                 font=("Arial",22, "bold"),anchor='nw')
#caractéristiques des options du theme solde
    Button_solde = Button(fen,text ='Solde',bg='#F0EBE9',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command= afficher_solde)

#caractéristiques des options du theme 2
    Button_historique = Button(fen,text ='Historique',bg='#F0EBE9',\
                        fg='black',font=("Arial",12),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_historique)
#caractéristiques des options du theme 3
    Button_retrait = Button(fen,text='Retrait',bg='#F0EBE9',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command=afficher_retrait)

#caractéristiques des options du theme 4
#    Button_depot = Button(fen,text ='Dépot',bg='#F0EBE9',fg='black',\
#                        font=("Arial",13),activeforeground='white',
#                        activebackground='#048B9A',command= afficher_depot)
#caractéristiques des options du theme 5
#    Button_transfert = Button(fen,text ='Transfert',bg='#F0EBE9',fg='black',\
#                        font=("Arial",12),activeforeground='white',
#                        activebackground='#048B9A',command= effectuer_transfert)

        
    #Button_Connexion.place(x = 500, y = 500)
#placements des options du theme 1
    Button_solde.place(x=555,y=635)

#placements des options du theme 2
    Button_historique.place(x=1090,y=555)
#placements des options du theme 3
    Button_retrait.place(x=545,y=555)

#placements des options du theme 4
#    Button_depot.place(x=1090,y=510)
#placements des options du theme 5
#    Button_transfert.place(x = 1090, y = 640)







def afficher_retrait():
    
    dessin.delete(ALL)
    newWindow = Toplevel(fen)
#création d'une nouvelle fenêtre avec une nouvelle taille
    newWindow.title("Bienvenue sur le distributeur")
    newWindow.geometry("1900x1563")
    newWindow.resizable(width=True,height=True)

    dessin.create_image(450,100,image = fond_distrib,anchor ='nw')
    dessin.create_text(500,25,text="Veuillez choisir le montant à retirer",\
                                 font=("Arial",50, "bold"),anchor='nw')
    dessin.create_text(629,550,text="20€",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(931,510,text="50€",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(638,635,text="40",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(931,550,text="70€",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(931,580,text="100€",\
                                 font=("Arial",22, "bold"),anchor='nw')
    dessin.create_text(931,635,text="Autre",\
                                 font=("Arial",22, "bold"),anchor='nw')

#caractéristiques des options du theme solde
    choix_1 = Button(newWindow,text ='20€ ',bg='#F0EBE9',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command= give_money)

#caractéristiques des options du theme 2
    choix_2 = Button(newWindow,text ='40€',bg='#F0EBE9',\
                        fg='black',font=("Arial",12),activeforeground='white',\
                        activebackground='#048B9A',command=give_money)
#caractéristiques des options du theme 3
    choix_3 = Button(newWindow,text='50€',bg='#F0EBE9',\
                        fg='black',font=("Arial",15),activeforeground='white',\
                        activebackground='#048B9A',command=give_money)

#caractéristiques des options du theme 4
    choix_4 = Button(newWindow,text ='70€',bg='#F0EBE9',fg='black',\
                        font=("Arial",13),activeforeground='white',
                        activebackground='#048B9A',command= give_money)
#caractéristiques des options du theme 5
    choix_5 = Button(newWindow,text ='Autre',bg='#F0EBE9',fg='black',\
                        font=("Arial",12),activeforeground='white',
                        activebackground='#048B9A',command= ask_for_amount)

        

#placements des options du theme 1
    choix_1.place(x=555,y=555)

#placements des options du theme 2
    choix_2.place(x=1090,y=555)
#placements des options du theme 3
    choix_3.place(x=745,y=555)

#placements des options du theme 4
    choix_4.place(x=1090,y=510)
#placements des options du theme 5
    choix_5.place(x = 1090, y = 640)


 #utiliser pour la deuxieme fenetre apres choix du distributeur
    menu_bar = Menu(newWindow)
    menu_fill = Menu(menu_bar, tearoff=0)
    menu_fill.add_command(label = 'Votre solde', command= afficher_solde)
    menu_fill.add_command(label = 'Historique', command= afficher_historique)
    menu_fill.add_command(label='Quitter', command= Quitter)
    menu_bar.add_cascade (label="Votre compte", menu=menu_fill)
    newWindow.config(menu=menu_bar)



banque1 = Radiobutton (fen,text= 'Banque Populaire', bg = '#3933FF' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 0)

banque2 = Radiobutton (fen,text= 'CIC', bg = '#5CC355' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 1)

banque3 = Radiobutton (fen,text= 'Société Générale', bg = '#FF0303' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 2)

banque4 = Radiobutton (fen,text= 'Banque Postale', bg = '#F9F902' ,fg = 'black',\
            activeforeground='white',\
            activebackground='#3933FF', variable = choix_banque, value = 3)


Bouton_valider = Button (fen,text= 'Valider votre choix',bg ='#FFFFFF',\
                fg = 'black', activeforeground= 'white',\
                    activebackground='#000000',command= CreateNewFen)
'''
menu_bar = Menu(fen)
menu_fill = Menu(menu_bar, tearoff=0)
menu_fill.add_command(label='Votre solde', command=afficher_solde)
menu_fill.add_command(label='Historique', command=afficher_historique)
menu_fill.add_command(label='Quitter', command=Quitter)
menu_bar.add_cascade(label="Votre compte", menu=menu_fill)
fen.config(menu=menu_bar)
'''
f = font.Font(size = 24)
Bouton_valider['font'] = f
banque1.place(x = 640, y = 400)
banque2.place(x = 750, y = 500)
banque3.place(x = 700, y = 585)
banque4.place(x = 520,y = 685)
Bouton_valider.place(x = 600, y = 900)


print("5")
fen.mainloop() 


def destroy(bouton):
    bouton.destroy()
    
