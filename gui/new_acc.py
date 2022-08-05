from tkinter import *
from tkinter import messagebox
from BankingGUI.ui import Admin
from BankingGUI.gui import gui_dashboard
a=Admin.Admin()
def newAccount():
    def custdata():
        if(len(id.get())!=0 and len(name.get())!=0 and len(mob.get())!=0 and len(email.get())!=0 and len(bal.get())!=0):
            cust_id=id.get()
            cust_name=name.get()
            cust_mob=mob.get()
            cust_email=email.get()
            cust_bal=bal.get()
            n=a.adminvalidate(cust_id,cust_name,cust_mob,cust_email,cust_bal)
            if(n==1):
                messagebox.showinfo(message='ACCOUNT CREATED SUCCESSFULLY')
                newacc.destroy()
                gui_dashboard.display_dashboard()
            else:
                messagebox.showinfo(message='SORRY!SOMETHING WENT WRONG')
        else:
            messagebox.showwarning(message='PLEASE ENTER ALL THE DETAILS')
            newacc.focus_force()
    newacc=Tk()
    newacc.geometry('300x300')
    Label(newacc,text='ENTER ID:').pack()
    id=Entry(newacc)
    id.pack()

    Label(newacc,text='ENTER NAME:').pack()
    name=Entry(newacc)
    name.pack()

    Label(newacc,text='ENTER MOBILE NO:').pack()
    mob=Entry(newacc)
    mob.pack()

    Label(newacc,text='ENTER EMAIL-ID:').pack()
    email=Entry(newacc)
    email.pack()

    Label(newacc,text='ENTER BALANCE:    *Balance should greater than 100/-*').pack()
    bal=Entry(newacc)
    bal.pack()

    accbtn=Button(newacc,width=15,text='NEXT',command=custdata)
    accbtn.pack()

    newacc.mainloop()