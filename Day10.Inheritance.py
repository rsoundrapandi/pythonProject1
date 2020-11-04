class hdfc():

    def accountdetails(self):
        accountno=int(input("Enter the Account No"))
        pin = int(input("Enter the pin value:"))
        self.accountno=accountno
        self.pin=pin

        if(self.accountno==accountno and self.pin==pin):

            print("Login is successful")
        else:

            print("invalid credentials")

class hdfc1(hdfc):

    def deposit(self):
        super().accountdetails()
        amount=int(input("Enter the amount value :"))
        self.balanceamount = 0
        if(amount>0):
            self.balanceamount +=amount
            print("Balance amount value is :",self.balanceamount)
        else:
            print("Amount is not credited o the account")


test=hdfc1()

test.deposit()

