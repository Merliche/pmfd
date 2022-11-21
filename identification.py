from tkinter import *
from tkinter import messagebox
import sqlite3
from functools import partial



def check_if_exist(identifiants):
    conn = sqlite3.connect('my_DB.db')
    cur = conn.cursor()
    cur.execute("""SELECT id FROM utilisateurs WHERE CB=?""",(identifiants[0],))
    id = cur.fetchone()
    cur.execute("""SELECT CB,code_pin FROM utilisateurs WHERE id=?""", id,)
    response = cur.fetchone()
    user_identifiants = list(response)
    print(user_identifiants)
    if identifiants[1] == user_identifiants[1]:
        print('Toto')
    else:
        print("tata")
        




OptionList = [
"5136405006383498",
"3285548746932323",
"5764831715489314",
"5434 8952 2314 7594",
"5129 0309 5703 7668",
"5395 3319 9090 6720"
] 


def validateLogin(CB, password):
    CB_values = CB.get()
    password_values = password.get()
    print("username entered :", CB.get())
    print("password entered :", password.get())
    identifiants = [CB_values,password_values]
    print(identifiants)
    if check_if_exist(identifiants):
        Window.destroy()
    else:
        messagebox.showerror("error", "try again")
        Window.mainloop()
    return identifiants

#window
Window = Tk()  
Window.geometry('400x150')  
Window.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
CBLabel = Label(Window, text="CB").grid(row=0, column=0)
CB = StringVar()
CBEntry = OptionMenu(Window,CB,*OptionList).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(Window,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(Window, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, CB, password)

#login button
loginButton = Button(Window, text="Login", command=validateLogin).grid(row=4, column=0)  

Window.mainloop()