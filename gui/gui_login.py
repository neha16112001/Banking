from tkinter import *
from BankingGUI.ui import CustomerUI
from tkinter import messagebox
from BankingGUI.gui import CreateAccount
c=CustomerUI.CustomerUI()
def login():
        def login_datasave():
                if(len(username.get())!=0 and len(password.get())!=0):
                        userid=username.get()
                        passwd=int(password.get())
                        a=c.login(userid,passwd)
                        if(a==1):
                                messagebox.showinfo(title='', message='LOGIN SUCCESSFUL!')
                                login.destroy()
                                CreateAccount.create_account()
                        else:
                                messagebox.showwarning(message='YOUR USERNAME OR PASSWORD WENT WRONG')
                else:
                        messagebox.showwarning(message='PLEASE ENTER BOTH THE FIELDS')
                        login.focus_force()

        login=Tk()
        Label(login,text='ENTER USERNAME').grid(row=0)
        username=Entry(login)
        username.grid(row=0,column=1)
        Label(login,text='ENTER PASSWORD').grid(row=1)
        password=Entry(login)
        password.grid(row=1,column=1)
        loginbtn=Button(login,text="LOGIN",width=15,command=login_datasave)
        loginbtn.grid(row=2)
        login.mainloop()
