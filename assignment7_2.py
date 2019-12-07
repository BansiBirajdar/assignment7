'''Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.'''
class BankAccount:
    ROI=10.5
    def __init__(self,name,amount):
        self.Name=name
        self.Amount=amount

    def Deposit(self):
        amount=int(input("enter the deposit amount="))
        self.Amount+=amount
    def Withdraw(self):
        amount=int(input("enter the withdraw amount="))
        self.Amount-=amount
    
    def CalculateIntrest(self):
        self.Amount=float(self.Amount+self.Amount*(BankAccount.ROI/100))
        
    def Display(self):
        print("Name=",self.Name)
        print("amount",self.Amount)
def main():
        name=input("enter the name=")
        amount=float(input("enter the amount="))
        obj=BankAccount(name,amount)
        obj.Deposit()
        obj.Withdraw()
        obj.CalculateIntrest()
        obj.Display()
        name=input("enter the name=")
        amount=float(input("enter the amount="))
        obj1=BankAccount(name,amount)
        obj1.Deposit()
        obj1.Withdraw()
        obj1.CalculateIntrest()
        obj1.Display()
if __name__=="__main__":
    main()