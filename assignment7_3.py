'''Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects'''

class Arithmetic:

    sum=0

    def __init__(self,value):
        self.no = value
    
    def chkPrime(self):
        if(self.no==2):
            return True
        for i in range(2,self.no):
            if(self.no%i==0):
               return False
        return True
    
    def Factors(self):
        print("Factors are :",end=" ")
        for i in range(1,self.no):
            if(self.no%i==0):
                self.sum+=i
                print(i,end=" ")
    
    def Sumof(self):
        print("Sum:",self.sum)

    def chkPerfect(self):
        if(self.no==self.sum):
            return True
        return False

if __name__ == "__main__":

    obj=Arithmetic(6)
    if(obj.chkPrime()):
        print("This is Prime No.")
    else:
        print("This is not Prime No.")
    obj.Factors()
    obj.Sumof()
    if(obj.chkPerfect()):
        print("THis is perfect No")
    else:
        print("This is not Perfect No")
