from tkinter import *
from tkinter import messagebox
from BankingGUI.ui import CustomerUI
from BankingGUI.gui import gui_login
c=CustomerUI.CustomerUI()
def signin():
        def signin_datasave():
                if(len(fname.get())!=0 and len(lname.get())!=0 and len(userid.get())!=0 and len(passwd.get())!=0 and len(c_password.get())!=0):
                        first_name=fname.get()
                        last_name=lname.get()
                        username=userid.get()
                        password=int(passwd.get())
                        cpassword=int(c_password.get())
                        a = c.signin(username,password,cpassword)
                        if (a == 1):
                                messagebox.showinfo(title='', message='REGISTRATION SUCCESSFUL!')
                                signin.destroy()
                                gui_login.login()

                        else:
                                messagebox.showwarning(message='SORRY!YOUR CONFIRM PASSWORD DOES NOT MATCHES WITH PASSWORD')
                else:
                        messagebox.showwarning(message='ENTER ALL THE DETAILS')
                        signin.focus_force()

        signin=Tk()

        Label(signin,text='ENTER YOUR FIRST NAME:').pack()

        fname=Entry(signin)
        fname.pack()

        Label(signin, text='ENTER YOUR LAST NAME:').pack()
        lname = Entry(signin)
        lname.pack()

        Label(signin, text='ENTER YOUR USERNAME:').pack()
        userid = Entry(signin)
        userid.pack()

        Label(signin, text='ENTER YOUR PASSWORD:').pack()
        passwd = Entry(signin)
        passwd.pack()

        Label(signin,text='CONFIRM PASSWORD:').pack()
        c_password=Entry(signin)
        c_password.pack()

        Button(signin,text='Signin',width=15,command=signin_datasave).pack()
        signin.mainloop()
