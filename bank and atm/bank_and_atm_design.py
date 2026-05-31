from enum import Enum
from datetime import datetime
import uuid
class AccountType(Enum):
    SAVING="SAVING"
    CURRENT="CURRENT"
    
class TransactionType(Enum):
    DEPOSIT="DEPOSIT"
    WITHDRAWAL="WITHDRAWAL"
    TRANSFER="TRANSFER"
    
class Transaction:
    def __init__(self,amount,account_id,ttype,balance):
        self.tid=str(uuid.uuid4())
        self.amount=amount
        self.account_id=account_id
        self.balance_after=balance
        self.type=ttype
        self.timestamp=datetime.now()
        
class Account:
    def __init__(self,atype,customer):
        self.account_id=str(uuid.uuid4())
        self.account_number=str(uuid.uuid4())
        self.balance=0
        self.type=atype
        self.owner=customer
        self.Transactionlist=[]
    def add_trasaction(self,Transaction):
        self.Transactionlist.append(Transaction)
    
    def get_transaction(self):
        return self.Transactionlist
        

class Customer:
    def __init__(self,name):
        self.cid=str(uuid.uuid4())
        self.cname=name
        self.accounts=[]
    def create_account(self,type):
        a1=Account(type,self)
        self.accounts.append(a1)
        return a1


class Card:
    def __init__(self,number,pin,account):
        self.card_id=str(uuid.uuid4())
        self.card_number=number
        self.pin=pin
        self.account=account
        self.is_blocked=False
        self.failed_attempt=0

class ATM:
    def __init__(self,location,cash):
        self.atm_id=str(uuid.uuid4())
        self.location=location
        self.cash_available=cash
    
    def verify_pin(self,card,pin):
        if card.is_blocked:
            raise Exception("Card is blocked")
        if card.pin == pin:
            card.failed_attempt = 0
            return True
        else:
            card.failed_attempt += 1
            if card.failed_attempt >= 3:
                card.is_blocked = True
                raise Exception("Card blocked after 3 failed attempts")
            return False
    
    def check_balance(self,card):
        return card.account.balance
    
    def withdraw(self,card,amount):
        if card.is_blocked:
             raise Exception("Card is blocked")
        if card.account.balance>=amount:
            card.account.balance-=amount
            t = Transaction(amount, card.account.account_id,
                       TransactionType.WITHDRAWAL, card.account.balance)
            card.account.add_trasaction(t)
            return amount


class Bank:
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.accounts=[]
        self.customers=[]
    
    
    def check_balance(self,account):
        return account.balance
        
    
    def deposit(self,account,amount):
        account.balance+=amount
        t=Transaction(amount,account.account_id,TransactionType.DEPOSIT,account.balance)
        account.add_trasaction(t)
    
    def withdraw(self, account, amount):
        if account.balance>=amount:
            account.balance-=amount
            t=Transaction(amount,account.account_id,TransactionType.WITHDRAWAL,account.balance)
            account.add_trasaction(t)
    def transfer(self,account1,account2,amount):
        if self.check_balance(account1)>=amount:
            account1.balance-=amount
            account2.balance+=amount
            t=Transaction(amount,account1.account_id,TransactionType.TRANSFER,account1.balance)
            account1.add_trasaction(t)
            t2=Transaction(amount,account2.account_id,TransactionType.TRANSFER,account2.balance)
            account2.add_trasaction(t2)
            
 
            
# bank=Bank()
# c1=Customer("kajal")
# c2=Customer("sohan")
# account1=c1.create_account(AccountType.SAVING)
# account2=c2.create_account(AccountType.CURRENT)
# card1=Card(1235,7676,account1)
# bank.deposit(account1,1700)
# bank.withdraw(account1,100)
# bank.trasfer(account1,account2,600)
# print(bank.check_balance(account1))
# atm=ATM("jaipur",50000)
# atm.verify_pin(card1,1414)
# atm.withdraw(card1,500)
# print(atm.check_balance(card1))

bank = Bank()

# Create customers
c1 = Customer("Kajal")
c2 = Customer("Sohan")

# Create accounts
account1 = c1.create_account(AccountType.SAVING)
account2 = c2.create_account(AccountType.CURRENT)

# Create card
card1 = Card("1235", "7676", account1)

# Bank operations
bank.deposit(account1, 1700)
print("After deposit:", bank.check_balance(account1))    # 1700

bank.withdraw(account1, 100)
print("After withdraw:", bank.check_balance(account1))   # 1600

bank.transfer(account1, account2, 600)
print("account1 after transfer:", bank.check_balance(account1))  # 1000
print("account2 after transfer:", bank.check_balance(account2))  # 600

# ATM operations
atm = ATM("Jaipur", 50000)

# Wrong PIN test
result = atm.verify_pin(card1, "1414")
print("Wrong PIN result:", result)   # False

# Correct PIN
if atm.verify_pin(card1, "7676"):
    atm.withdraw(card1, 500)
    print("ATM balance after withdraw:", atm.check_balance(card1))  # 500

# Transaction history
print("account1 transactions:")
for t in account1.get_transaction():
    print(" ", t.type, t.amount, t.balance_after)






        
            
        