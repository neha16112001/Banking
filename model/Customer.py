class Customer:
    # def __init__(self,id,name,mob,email,bal):
    #     self.id=id
    #     self.name=name
    #     self.email=email
    #     self.mob=mob
    #     self.bal=bal

    @property
    def cust_id(self):
        return self.id

    @property
    def cust_name(self):
        return self.name

    @property
    def cust_email(self):
        return self.email

    @property
    def cust_mob(self):
        return self.mob

    @property
    def cust_bal(self):
        return self.bal

    @cust_id.setter
    def cust_id(self,id):
        self.id=id

    @cust_name.setter
    def cust_name(self,name):
        self.name=name

    @cust_email.setter
    def cust_email(self,email):
        self.email=email

    @cust_mob.setter
    def cust_mob(self,mob):
        self.mob=mob

    @cust_bal.setter
    def cust_bal(self,bal):
        self.bal=bal

    def getbal(self):
        return self.bal

    def setbal(self,bal):
        self.bal=bal