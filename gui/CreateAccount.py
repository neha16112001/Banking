from tkinter import *
from BankingGUI.gui import gui_dashboard,new_acc
def create_account():
    def acc_created():
        account.destroy()
        gui_dashboard.display_dashboard()
    def acc_not_created():
        account.destroy()
        new_acc.newAccount()
    account=Tk()
    account.geometry('250x250')
    Label(account,text='DO YOU ALREADY HAVE AN ACCOUNT IN OUR BANK?').pack()
    a=Entry(account)
    a.pack()
    acc_yes_btn=Button(account,width=15,text='YES',command=acc_created)
    acc_yes_btn.pack()
    acc_no_btn=Button(account,width=15,text='NO',command=acc_not_created)
    acc_no_btn.pack()
    account.mainloop()