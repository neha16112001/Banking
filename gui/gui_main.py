from tkinter import *
from BankingGUI.gui import gui_login,gui_signin
m=Tk()

m.geometry('250x250')
m.configure(bg='black')
b1=Button(m,text='LOGIN',width=15,command=gui_login.login).pack(padx=20,pady=30)
b2=Button(m,text='SIGNIN',width=15,command=gui_signin.signin).pack(padx=5,pady=20)
m.mainloop()