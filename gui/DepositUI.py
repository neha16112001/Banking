from tkinter import *
from tkinter import messagebox
from BankingGUI.dao import CustomerDAO
c=CustomerDAO.CustomerDAO()
def depositUI(id):
    def desposit_amt():
        if(len(amt.get())!=0):
            a=c.deposit(id,int(amt.get()))
            if(a==1):
                messagebox.showinfo(message='AMOUNT DEPOSITED')
                messagebox.showinfo(message='YOUR BALANCE IS:' + str(c.getbalance(id)))
                deposit.destroy()
            else:
                messagebox.showwarning(message='SORRY!SOMETHING WENT WRONG')
        else:
            messagebox.showwarning(message='PLEASE ENTER AMOUNT')
    deposit=Tk()
    deposit.geometry('300x300')

    Label(deposit,text='ENTER THE AMOUNT TO BE DEPOSITED').pack()
    amt=Entry(deposit)
    amt.pack()

    deposit_btn=Button(deposit,text='PROCEED',width=15,command=desposit_amt)
    deposit_btn.pack()

    deposit.mainloop()