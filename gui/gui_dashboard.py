from tkinter import *
from tkinter import messagebox
from BankingGUI.gui import WithdrawalUI
from BankingGUI.gui import DepositUI
from BankingGUI.dao import CustomerDAO
from BankingGUI.gui import Transaction_historyUI
from BankingGUI.model import Customer
cdao=CustomerDAO.CustomerDAO()
cust=Customer.Customer()
def display_dashboard():
    def deposit_amount():
        if (len(id.get()) != 0):
            DepositUI.depositUI(int(id.get()))
        else:
            messagebox.showwarning(message='PLEASE ENTER THE ID FIRST')
    def withdraw_amount():
        if (len(id.get()) != 0):
            WithdrawalUI.withdraw(int(id.get()))
        else:
            messagebox.showwarning(message='PLEASE ENTER THE ID FIRST')
    def recharge():
        pass
    def transaction():
        if (len(id.get()) != 0):
            Transaction_historyUI.transaction_history(int(id.get()))
        else:
            messagebox.showwarning(message='PLEASE ENTER THE ID FIRST')
    def showbal(balance):
        if(len(id.get())!=0):
            bal=cdao.getbalance(int(id.get()))
            balance["text"]="Balance:"+str(bal)
        else:
            messagebox.showwarning(message='PLEASE ENTER THE ID FIRST')
    dashboard=Tk()
    dashboard.focus_force()
    dashboard.title('DASHBOARD')
    dashboard.geometry('400x400')

    Label(dashboard,text='ENTER YOUR ID FOR TRANSACTIONS').pack()
    id=Entry(dashboard)
    id.pack()

    balance=Label(dashboard)
    balance.pack()

    deposit=Button(dashboard,text='DEPOSIT AMOUNT',width=25,command=deposit_amount)
    deposit.pack()

    withdraw=Button(dashboard,text='WITHDRAW AMOUNT',width=25,command=withdraw_amount)
    withdraw.pack()

    recharge = Button(dashboard, text='RECHARGE', width=25,command=recharge)
    recharge.pack()

    transaction_history = Button(dashboard, text='TRANSACTION HISTORY', width=25,command=transaction)
    transaction_history.pack()

    show=Button(dashboard,text='SHOW BALANCE',width=25,command=lambda:showbal(balance))
    show.pack()

    dashboard.mainloop()
display_dashboard()
