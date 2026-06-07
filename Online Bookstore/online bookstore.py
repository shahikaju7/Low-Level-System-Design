from abc import ABC, abstractmethod
import threading
import uuid
from enum import Enum
class OrderStatus(Enum):
    PLACED="PLACED"
    PROCESSING="PROCESSING"
    SHIPPED="SHIPPED"
    DELIVERED="DELIVERED"
    CANCELLED="CANCELLED"

class UserRole(Enum):
    USER="USER"
    ADMIN="ADMIN"
class User():
    def __init__(self, name, email,password):
        self.uid=uuid.uuid4()
        self.name = name
        self.email = email
        self.role=UserRole.USER
        self.password=password

class Order():
    def __init__(self,book,user,payment):
        self.oid=uuid.uuid4()
        self.status = OrderStatus.PLACED
        self.book=book
        self.user=user
        self.payment=payment

class Book():
    def __init__(self,author,subject,title,price):
        self.bid=uuid.uuid4()
        self.author=author
        self.subject=subject
        self.title=title
        self.price=price

class Admin(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)
        self.role=UserRole.ADMIN

class Payment(ABC):
    @abstractmethod
    def processPayment(self,amount):
        pass
    @abstractmethod
    def refundPayment(self,txnid):
        pass

class UPIPayment(Payment):
    def processPayment(self,amount):
        print("UPI payment ")
    
    def refundPayment(self, txnid):
        print("UPI refund")

class CreditCardPayment(Payment):
    def processPayment(self,amount):
        print("Credit Card payment ")
    
    def refundPayment(self, txnid):
        print("Credit Card refund")

class DebitCardPayment(Payment):
    def processPayment(self,amount):
        print("Debit Card payment ")
    
    def refundPayment(self, txnid):
        print("Debit Card refund")

class Inventory():
    instance=None
    __lock=threading.Lock()
    def __new__(cls):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.bookStock={}
        self.titleIndex={}
        self.authorIndex={}
        self.subjectIndex={}
        self.restock=10

# CaseUse
# Value is integerdict[key] = dict.get(key, 0) + value
# Value is listdict.setdefault(key, []).append(value)

    def addBook(self,book,qty):
        self.bookStock[book]=self.bookStock.get(book,0)+qty
        self.titleIndex.setdefault(book.title, []).append(book)
        self.authorIndex.setdefault(book.author, []).append(book)
        self.subjectIndex.setdefault(book.subject, []).append(book)

    def deleteBook(self,book):
        del self.bookStock[book]
        self.titleIndex[book.title].remove(book)
        self.authorIndex[book.author].remove(book)
        self.subjectIndex[book.subject].remove(book)
    
    def updateStock(self,book,qty):
        with self.__lock:
            self.bookStock[book] = self.bookStock.get(book, 0) + qty
    
    def searchBook(self,query,type):
        if type == "title":
            return self.titleIndex.get(query, [])
        elif type == "author":
            return self.authorIndex.get(query, [])
        elif type == "subject":
            return self.subjectIndex.get(query, [])
    
    def checkstock(self,book):
        return self.bookStock.get(book,0)

class OrderManger():
    instance=None

    def __new__(cls):
        if cls.instance is None:
            cls.instance=super().__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.orders=[]
    def placeOrder(self,user,book,payment):
        order = Order(user, book, payment)
        self.orders.append(order)
        print(f"Order {order.oid} placed successfully!")
        return order
     
    def cancel_order(self, order_id):
        for order in self.orders:
            if order.oid == order_id:
                # can only cancel if PLACED or PROCESSING
                if order.status in [OrderStatus.PLACED, OrderStatus.PROCESSING]:
                    order.status = OrderStatus.CANCELLED
                    print(f"Order {order_id} cancelled!")
                    return order
                else:
                    print(f"Order {order_id} cannot be cancelled!")
                    return None
    
    def process_payment(self, payment, amount):
        payment.processPayment(amount)

# Facade
class BookstoreService:
    def __init__(self):
        self.inventory = Inventory()
        self.order_manager = OrderManger()
    
    # User operations
    def search_book(self, query):
        return self.inventory.searchBook(query, "title")
    
    def place_order(self, user, book, payment):
        # Step 1 - check stock
        if self.inventory.bookStock.get(book, 0) <= 0:
            print("Book out of stock!")
            return None
        # Step 2 - process payment
        self.order_manager.process_payment(payment, book.price)
        # Step 3 - update stock
        self.inventory.updateStock(book, -1)
        # Step 4 - place order
        return self.order_manager.placeOrder(user, book, payment)
    
    def cancel_order(self, oid, book):
        order = self.order_manager.cancel_order(oid)
        if order:
            # restore stock
            self.inventory.updateStock(book, +1)
    
    # Admin operations
    def add_book(self, user, book, quantity):
        if user.role == UserRole.ADMIN:
            self.inventory.addBook(book, quantity)
        else:
            raise Exception("Unauthorized!")
    
    def delete_book(self, user, book):
        if user.role == UserRole.ADMIN:
            self.inventory.deleteBook(book)
        else:
            raise Exception("Unauthorized!")
    

B1=Book("Author1","Subject1","Book1",100)
B2=Book("Author2","Subject2","Book2",200)   
admin=Admin("Admin1","admin1@example.com","adminpass")
service=BookstoreService()
service.add_book(admin,B1,10)
service.add_book(admin,B2,5)
user=User("User1","user1@example.com","userpass")
payment=UPIPayment()
order=service.place_order(user,B1,payment)
service.cancel_order(order.oid,B1)
      





