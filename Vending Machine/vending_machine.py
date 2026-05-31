from enum import Enum
import uuid
from abc import ABC, abstractmethod

class MachineState(Enum):
    IDLE = "IDLE"
    SELECTED = "SELECTED"
    DISPENSING = "DISPENSING"

class ProductCategory(Enum):
    SNACKS = "SNACKS"
    DRINK = "DRINK"
    CANDY = "CANDY" 

class Product:
    def __init__(self,name,price,productcategory):
        self.pid=str(uuid.uuid4())
        self.name=name
        self.price=price
        self.category=productcategory

class Slot:
    def __init__(self,product,quantity,price):
        self.slotid=str(uuid.uuid4())
        self.product=product
        self.quantity=quantity
        self.price=price
    def is_available(self):
        return self.quantity>0

class Payment(ABC):
    @abstractmethod
    def payamount(self,amount):
        pass
class CardPayment(Payment):
    def payamount(self,amount):
        print("Payment done via card")
        return True
        
class Cashpayment(Payment):
    def payamount(self,amount):
        if amount>=0:
            print("Payment done via cash")
            return True
        else:
           raise Exception("Insufficient cash")

class Admin:
    def __init__(self,name):
        self.admin_is=str(uuid.uuid4())
        self.name=name
    def restock(self,slot,quantity):
        slot.quantity+quantity
        print(f"Restocked {slot.product.name} by {quantity}")
    def update_price(self,slot,p):
        slot.price=p
        print(f"Updated price of {slot.product.name} to {p}")
        
class VendingMachine:
    def __init__(self):
        self.slots=[]
        self.state=MachineState.IDLE
        self.inserted_amount=0
        self.selected_slot=None
        
    def selected_product(self,slot_id):
        for s in self.slots:
            if s.slotid==slot_id:
                if not s.is_available():
                    raise Exception(f"{s.product.name} is out of stock")
                self.state=MachineState.SELECTED
                self.selected_slot=s
                print(f"Selected product: {s.product.name}, Price: {s.price}")
                return s
        raise Exception("Invalid slot id")

    def insert_money(self,amount,payment):
        if self.state!=MachineState.SELECTED:
            raise Exception("Please select a product first")
        if amount<self.selected_slot.price:
            raise Exception("Insufficient amount")  
        self.inserted_amount=amount
        payment.payamount(amount)
        self.dispense_product()
        
    def dispense_product(self):
        if self.selected_slot.is_available():
            self.state = MachineState.DISPENSING
            print(f"Dispensing: {self.selected_slot.product.name}")
            self.selected_slot.quantity -= 1
            change = self.inserted_amount - self.selected_slot.price
            if change > 0:
                self.return_change(change)
            self.selected_slot = None
            self.inserted_amount = 0
            self.state = MachineState.IDLE

        else:
             raise Exception(f"{self.selected_slot.product.name} is out of stock")
        
    def return_change(self, amount):
        print(f"Returning change: {amount}")   
        
    def notify_customer(self, msg):
        print(f"Notification: {msg}")


v1=VendingMachine()
p1=Product("Coke", 1.5, ProductCategory.DRINK)  
s1=Slot(p1,10,1.5)
v1.slots.append(s1)
v1.selected_product(s1.slotid)
payment_method=CardPayment()
v1.insert_money(2.0, payment_method)    

        
        
        
    