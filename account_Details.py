class acc_Det:
    def __init__(self,acc,bal,name):
        self.acc_no = acc
        self.balance = bal
        self.name = name

    def Debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"has been debited")
        print("balance now is",self.balance)

    def Credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"has been credit")
        print("balance now is",self.balance)

ac1 = acc_Det(123456,1000,"Rajath")
print("hello",ac1.name)
print("the acc number is",ac1.acc_no)
print("the balance in ur acc is",ac1.balance)
ac1.Debit(500)
ac1.Credit(600)
