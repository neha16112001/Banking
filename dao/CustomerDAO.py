from BankingGUI.database import connection
from datetime import datetime
c=connection.connection()
cursor,con=c.con()
def transaction(id,transaction_type,amount,balance):
    currdatetime = datetime.now()
    formatted = currdatetime.strftime('%Y-%m-%d %H:%M:%S')
    str='insert into transaction(id,transaction_type,amount,balance,datetime) values(%s,%s,%s,%s,%s)'
    list=[id,transaction_type,amount,balance,formatted]
    if cursor.execute(str,list):
        con.commit()
class CustomerDAO:
    def insert(self,c):
        str = 'insert into customer(id,name,mob,email,bal) values(%s,%s,%s,%s,%s)'
        list = [c.cust_id, c.cust_name, c.cust_mob,c.cust_email,c.cust_bal]
        if (cursor.execute(str, list)):
            con.commit()
            return 1
        else:
            return 0

    def deposit(self, id, amount):
        str = 'select bal from customer where id=%s'
        cursor.execute(str, id)
        bal = cursor.fetchone()
        balance = bal[0] + amount
        str = 'update customer set bal=%s where id=%s'
        list = [balance, id]
        transaction_type = 'Deposit'
        transaction(id, transaction_type, amount, balance)
        if (cursor.execute(str, list)):
            con.commit()
            return 1
        else:
            return 0

    def withdraw(self,id,amount):
        str = 'select bal from customer where id=%s'
        cursor.execute(str, id)
        bal = cursor.fetchone()
        if(amount<bal[0]):
            balance=bal[0]-amount
            str = 'update customer set bal=%s where id=%s'
            list = [balance, id]
            transaction_type = 'Withdrawal'
            transaction(id, transaction_type, amount, balance)
            if (cursor.execute(str, list)):
                con.commit()
                return 1
        else:
            return 0

    def getbalance(self,id):
        str='select bal from customer where id=%s'
        cursor.execute(str,id)
        bal=cursor.fetchone()
        return bal[0]