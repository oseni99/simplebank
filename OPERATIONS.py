# trying to create a simple banking operation with OOP 
import random 
random.seed(42)

# THE CLASS BANK 
class Bank():
    address = "627 West Battle Street,Talladega,Alabama"
    bank = "Talladega Western Bank"

    def __init__(self,name,ssn,address):
        self.name = name 
        self.ssn = ssn 
        self.address = address
        self.balance = 0.0 
        assert isinstance(self.name,str), "It has to be a name please"
        assert isinstance(self.ssn,int), "Can you enter the correct length and format"
        assert isinstance(self.address,str), "It has to be a string"

    def deposit(self,amount):
        self.balance+=amount 
       
    def acct_balance(self):
        print(f"User {self.name}, your balance is {self.balance}")

    def withdraw(self,amount):
        if amount < self.balance:
            self.balance-= amount
            print(f"Here is your withdrawal {self.amount}")
        else:
            print("Sorry,Insuficient Funds")
        
    
    def account_number(self):
        #self.randoms = randoms
        
        mylst = [0,1,2,3,4,5,6,7,8,9]
        x = random.choices(population=mylst,k=9)
        print("-".join(map(str,x)))

    

print(f"Welcome to {Bank.bank}")

name = str(input("Enter your name: "))
socials = int(input("Enter your ssn to proceed"))
address = input("Enter your address:")

b = Bank(name,socials,address)
print(f"You have now succesfully registered to {Bank.bank}")



