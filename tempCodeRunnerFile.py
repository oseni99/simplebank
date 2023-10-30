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
        print(f"You have succesfully deposited {amount}")
       
    def acct_balance(self):
        print(f"Hello {self.name}, your balance is {self.balance}")

    def withdraw(self,amount):
        x = float(amount)
        if x < self.balance:
            self.balance -= x
            print(f"You made a withdrawal of {x}")
        else:
            print("Sorry,Insuficient Funds")
        
    
    def account_number(self):
        #self.randoms = randoms
        
        mylst = [0,1,2,3,4,5,6,7,8,9]
        x = random.choices(population=mylst,k=9)
        return ("-".join(map(str,x)))

    

print(f"Welcome to {Bank.bank}")

name = str(input("Enter your name: ")).title()
socials = int(input("Enter your ssn to proceed: "))
address = input("Enter your address: ")

b = Bank(name,socials,address)
print(f"Hello {name}\nYou have now succesfully registered to {Bank.bank} and your account number is {b.account_number()}")

while True:
    creation = False 
    choice = input("Which account type do you want: \n1.Savings \n2.Checking")
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print("Savings Account Created Succesfully")
            creation = True
            break
        elif choice ==2:
             print("Checking Account Succesfully Created")
             creation = True
             break
    else:
        print("Invalid Choice, Can you choose 1 or 2")

while creation == True:
    print("Select 1:Deposit 2:Withdrawal 3:Check Balance 4:Stop")
    ques = input("Enter your choice: ")
    x = int(ques)
    if x in range(1,5):
        if x == 1:
            amount = input("Enter your deposit: ")
            q = float(amount)
            b.deposit(q)
            continue
        elif x == 2:
            amount = input("How much do you want to withdraw: ")
            b.withdraw(amount)
            continue 
        elif x == 3:
            b.acct_balance()
            continue
        elif x == 4:
            print(f"Thanks for banking with us at {Bank.bank} {name}")
            break 
        else:
            print("Can you kindly select an option?")
            break
    else:
        print("Can you please enter either 1,2 or 3")

        


        



