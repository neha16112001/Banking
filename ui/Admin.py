from BankingGUI.database import connection
from BankingGUI.model import Customer
from BankingGUI.dao import CustomerDAO
c=connection.connection()
cursor,con=c.con()
custdao=CustomerDAO.CustomerDAO()
class Admin:
    def adminvalidate(self,cust_id,cust_name,cust_mob,cust_email,cust_bal):
        c = Customer.Customer(cust_id,cust_name,cust_mob,cust_email,cust_bal)
        a = custdao.insert(c)
        return a
