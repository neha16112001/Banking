from tkinter import *
from tkinter import messagebox
from BankingGUI.dao import CustomerDAO
from BankingGUI.model import Customer
cdao=CustomerDAO.CustomerDAO()
def withdraw(id):
    def withdraw_amt():
        if(len(amt.get())!=0):
            a=cdao.withdraw(id,int(amt.get()))
            if (a == 1):
                messagebox.showinfo(message='AMOUNT WITHDRAWED')
                messagebox.showinfo(message='YOUR BALANCE IS:'+str(cdao.getbalance(id)))
                withdraw.destroy()
            else:
                messagebox.showwarning(message='YOUR BALANCE IS NOT SUFFICIENT')
        else:
            messagebox.showwarning('PLEASE ENTER THE AMOUNT')
    withdraw=Tk()

    Label(withdraw,text='ENTER THE AMOUNT TO BE WITHDRAWED').pack()
    amt=Entry(withdraw)
    amt.pack()

    withdraw_btn=Button(withdraw,text='PROCEED',width=15,command=withdraw_amt)
    withdraw_btn.pack()

    withdraw.mainloop()