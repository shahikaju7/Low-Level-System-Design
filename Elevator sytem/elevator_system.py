from enum import Enum
import uuid
class Direction(Enum):
    UP="UP"
    DOWN="DOWN"
    IDLE="IDLE"

class ElevatorStatus(Enum):
    MOVING="MOVING"
    IDLE="IDLE"

class DoorStatus(Enum):
    OPEN="OPEN"
    CLOSED="CLOSED"

class User:
    def __init__(self,name,weight,floor):
        self.uid=str(uuid.uuid4())
        self.uname=name
        self.weight=weight
        self.current_floor=floor
    def press_button(self,floor,direction):
        request=ElevatorRequest(floor,direction,self)
        return request
        

class Elevator:
    def __init__(self,capacity):
        self.eid=str(uuid.uuid4())
        self.capacity=capacity
        self.current_weight=0
        self.current_floor=0
        self.status=ElevatorStatus.IDLE
        self.door=DoorStatus.CLOSED
        self.direction=Direction.IDLE
    def has_space(self,weight):
        return self.current_weight+weight<=self.capacity
    def reach_floor(self,floor):
        self.current_floor=floor
        self.open_door()     
    def open_door(self):
        if self.status==ElevatorStatus.IDLE:
            self.door=DoorStatus.OPEN
    def close_door(self):
        self.door=DoorStatus.CLOSED

class ElevatorRequest:
    def __init__(self,floor,direction,user):
        self.requestid=str(uuid.uuid4())
        self.floor=floor
        self.direction=direction
        self.user=user

class BuildingSystem:
    instance=None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def __init__(self,totalfloor):
        self.elevators=[]
        self.total_floor=totalfloor
    def is_available(self,elevator,weight):
        return elevator.has_space(weight)
        
    def request_elevator(self,user,floor,direction):
        elevator=None
        for e in self.elevators:
            if self.is_available(e,user.weight):
                if e.direction==direction:
                    elevator=e
                    break
                elif  e.direction==Direction.IDLE:
                    elevator=e
        if elevator is None:
            raise Exception("No elevator is free")
        else:
            return elevator
               
    def assign(self,request):
        return self.request_elevator(request.user,request.floor,request.direction)

# Setup
e1 = Elevator(100)
e2 = Elevator(100)

b1 = BuildingSystem(5)
b1.elevators.append(e1)
b1.elevators.append(e2)

# Create users
u1 = User("Kajal", 45, 2)
u2 = User("Rohan", 57, 1)

# Check space
print("e1 has space for u1:", b1.is_available(e1, u1.weight))

# u1 presses button on floor 2 going UP
r1 = u1.press_button(2, Direction.UP)
print("Request floor:", r1.floor)
print("Request direction:", r1.direction)

# Assign elevator
elevator = b1.assign(r1)
print("Assigned elevator id:", elevator.eid)

# u2 presses button on floor 1 going UP
r2 = u2.press_button(1, Direction.UP)
elevator2 = b1.assign(r2)
print("Assigned elevator id:", elevator2.eid)

# Move elevator to requested floor
elevator.reach_floor(r1.floor)
print("Elevator now on floor:", elevator.current_floor)
print("Door status:", elevator.door)

    
            
        
        
        