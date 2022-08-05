from BankingGUI.database import connection
c=connection.connection()
cursor,con=c.con()
class CustomerDAO:
    def signin_datainsert(self,username,password):
        str='insert into user(username,password) values(%s,%s)'
        list=[username,password]
        if cursor.execute(str,list):
            print('Data saved')
            con.commit()

    def logindata(self,username,password):
        str='select password from user where username=%s'
        if(cursor.execute(str,username)):
            data=cursor.fetchone()
            if(data[0]==password):
                return 1
        else:
            return 0
