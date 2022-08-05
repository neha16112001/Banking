from tkinter import *
from BankingGUI.database import connection
c=connection.connection()
cursor,con=c.con()
def transaction_history(id):
    tran_history=Tk()
    tran_history.geometry('800x600')
    str='select * from transaction where id=%s'
    cursor.execute(str,id)
    data=cursor.fetchall()
    for i in range(len(data)):
        for j in range(len(data[0])):
            b=Entry(tran_history)
            b.grid(row=i,column=j)
            b.insert(END,data[i][j])
    tran_history.mainloop()