from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime
import uuid
class VehicleType(Enum):
    CAR="CAR"
    BIKE="BIKE"
    TRUCK="TRUCK"

class Spotstatus(Enum):
    AVAILABLE="AVAILABLE"
    OCCUPIED="OCCUPIED"

class SpotSize(Enum):
    SMALL="SMALL"
    MEDIUM="MEDIUM"
    LARGE="LARGE"

class Feestrategy(ABC):
    @abstractmethod
    def calculatefee(self,hour,vtype):
        pass

class Hourlyfee(Feestrategy):
    def calculatefee(self,hour,vtype):
        if vtype == VehicleType.BIKE:
            return hour*10
        if vtype  == VehicleType.TRUCK:
            return hour*100
        if vtype == VehicleType.CAR:
            return hour*50

class Vehicle:
    def __init__(self,license_plate,vtype):
        self.license_plate=license_plate
        self.vtype=vtype
    
    def get_type(self):
        pass
    
class Bike(Vehicle):
    def get_type(self):
        VehicleType.BIKE

class Car(Vehicle):
    def get_type(self):
        VehicleType.CAR
        
class Truck(Vehicle):
    def get_type(self):
        VehicleType.TRUCK
        
    
class ParkingSpot:
    def __init__(self,id,size):
        self.spotid=id
        self.spotsize=size
        self.spotstatus=Spotstatus.AVAILABLE
        self.vehicle=None
        
    def isavaialable(self):
        if self.spotstatus==Spotstatus.AVAILABLE:
            return True
        else:
            return False
    def assign(self,vehicle):
        self.spotstatus=Spotstatus.OCCUPIED
        self.vehicle=vehicle
       
    def release(self):
        self.vehicle=None
        self.spotstatus=Spotstatus.AVAILABLE


class Ticket:
    def __init__(self,ParkingSpot,Vehicle,Feestrategy):
        self.ticketid= str(uuid.uuid4())
        self.spot=ParkingSpot
        self.entrytime=datetime.now()
        self.exittime=None
        self.vehicle=Vehicle
        self.fee=None
        self.fee_strategy=Feestrategy
    def close(self):
        self.exittime=datetime.now()
        duration_hours = self.getduration(self.entrytime, self.exittime)
        self.fee = self.fee_strategy.calculatefee(duration_hours, self.vehicle.vtype)
        self.spot.release()
        return self.fee
        
    def getduration(self, entrytime,exittime):
        time= exittime-entrytime
        return time.total_seconds()/3600
        
class ParkingFloor:
    def __init__(self,id):
        self.floorid=id
        self.spots=[]
    def findspot(self,vehicle):
        for i in self.spots:
            if i.isavaialable() and i.spotsize==SpotSize.SMALL and vehicle.vtype==VehicleType.BIKE:
                return i
            if i.isavaialable() and i.spotsize==SpotSize.MEDIUM and vehicle.vtype==VehicleType.CAR:
                return i
            if  i.isavaialable() and i.spotsize==SpotSize.LARGE and vehicle.vtype==VehicleType.TRUCK:
                return i
        return None
    
    def get_free_count(self):
        count=0
        for spot in self.spots:
            if spot.isavaialable():
                count+=1
        return count

       
class Parkinglot:
    instance=None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
            
            
    def __init__(self):
        self.floors=[]
        self.active_tickets={}
    
    def get_free_floor_count(self):
        count=0
        for floor in self.floors:
            count=count+floor.get_free_count()
        return count
    
    def is_full(self):
        return self.get_free_floor_count()==0
        
        
    def park(self,Vehicle):
        spot=None
        for floor in  self.floors:
            spot=floor.findspot(Vehicle)
            if spot:
                break
        if spot is None:
            raise Exception("Parking lot is full")
    
        spot.assign(Vehicle)
        ticket= Ticket(spot,Vehicle,Hourlyfee())
        self.active_tickets[ticket.ticketid] = ticket
        return ticket
    
    def exit(self, ticket):
        fee = ticket.close()
        del self.active_tickets[ticket.ticketid]
        return fee
# 1. Create the parking lot (singleton)
lot = Parkinglot()

# 2. Create a floor
floor1 = ParkingFloor("F1")

# 3. Add spots to the floor
floor1.spots.append(ParkingSpot("S1", SpotSize.SMALL))
floor1.spots.append(ParkingSpot("S2", SpotSize.MEDIUM))
floor1.spots.append(ParkingSpot("S3", SpotSize.LARGE))

# 4. Add floor to lot
lot.floors.append(floor1)

# 5. Create a vehicle
car = Car("MH-1234", VehicleType.CAR)

# 6. Park the car
ticket = lot.park(car)
print("Ticket ID:", ticket.ticketid)
print("Spot assigned:", ticket.spot.spotid)
print("Spot status:", ticket.spot.spotstatus)
print("Total no of empty spaces in Praking lot",lot.get_free_floor_count())

# 7. Exit — fee calculated
fee = lot.exit(ticket)
print("Fee charged:", fee)
print("Spot status after exit:", ticket.spot.spotstatus)

        
                
            
        
       

        
        
            
        
        
    