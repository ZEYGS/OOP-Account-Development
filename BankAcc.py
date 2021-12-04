class BankAccount:

    def __init__(self, owners, number, balance): 
        self.owners = owners
        self.number = number
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        self.balance-=amount

    def __str__(self):
        return 'Account Owners: '+str(self.owners)+', Number: '+str(self.number)+', Balance: '+str(self.balance)

owners=['Seth P.','Chris V.','Chris F.']
number=23500 
balance=6000
BankAccount=[("Account Owners:", owners),("Number:", number), ("Balance:", balance)]
print("\nCreated Account:")
print(BankAccount)

class BankAccount:

    def __init__(self, owners, number, balance): 
        self.owners = owners
        self.number = number
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount

    def __str__(self):
        return 'Account Owners: '+str(self.owners)+', Number: '+str(self.number)+', Balance: '+str(self.balance)
    
class InterestAccount(BankAccount):

    def __init__(self, owners, number, balance, interest_rate, minimum_balance): 
        super().__init__(owners, number, balance)
        self.interest_rate = interest_rate
        self.minimum_balance = minimum_balance
    
    def compute_interest(self):
        return self.balance*(self.interest_rate/100)
        
    def withdraw(self,amount):
        if self.balance - amount >= self.minimum_balance:
            super().withdraw(amount)
        else:
            print('Cannot Withdraw')

    def getOwners(self):
        return self.owners
    
    def setOwners(self,owners):
        self.owners = owners

    def __str__(self):
        return super().__str__() + ', Interest Rate: '+str(self.interest_rate)+', Minimum balance: '+str(self.minimum_balance)
    
    def __repr__(self):
        return self.__str__()   
    
    
class Customer:
    
        def __init__(self, name, birthday, gender, id_number, accounts): 
            self.name = name
            self.birthday = birthday
            self.gender = gender
            self.id_number = id_number
            self.accounts = accounts
        
        def create_account(self, number, balance, interest_rate, minimum_balance):
            interestAccount = InterestAccount(self.name, number, balance, interest_rate, minimum_balance)
            self.accounts.append(interestAccount)

        def __str__(self, name, balance, interest_rate, minimum_balance):
            return 'Account Owners: '+str(self.owners)+', Number: '+str(self.number)+', Balance: '+str(self.balance)+', Interest: '+str(self.interest_rate)
    
owners = ['Seth P','Chris V','Chris F']
bankAccount = InterestAccount(owners,389000,600,4,700)
print("\nCreated Account:")
print(bankAccount)
print('\nDepositing 2000...')
bankAccount.deposit(2000)
print('\nWithdrawn 400...')
bankAccount.withdraw(400)
customer1 = Customer('Seth P','4/17/1999','M',1111,str(bankAccount))
print('\nCreated Customer...') 
print((customer1))

def link_account(self,account):
    owners=account.getOwners()
    owners.append(self.name)
    account.setOwners(owners)
    self.accounts.append(account)