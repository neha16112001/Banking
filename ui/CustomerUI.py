from BankingGUI.dao import LoginSigninDAO
cdao=LoginSigninDAO.CustomerDAO()
class CustomerUI:
    def signin(self,username,password,cpassword):
        if(password==cpassword):
            cdao.signin_datainsert(username,password)
            return 1
        else:
            return 0
    def login(self,username,password):
        a=cdao.logindata(username,password)
        return a