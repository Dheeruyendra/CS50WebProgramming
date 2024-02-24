class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def addPassenger(self, name):
        if self.isFull():
            return False
        self.passengers.append(name)
        return True
    
    def isFull(self):
        return self.capacity == len(self.passengers)


flight = Flight(3)

names = ["Divyansh", "Geet", "CS50", "David"]

for name in names:
    if flight.addPassenger(name):
        print(f"Yo {name} you got a ride.")
    else :
        print(f"Sorry we are full {name}")