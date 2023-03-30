class vehicle:
    def vehicle_info(self):
        print("Insie vehicle class")
class Car(vehicle):
    def car_info(sel,cnaem):
        print("Car name is ",cnaem)
class Bike(vehicle):
    def bike_info(self,bname):
        print("bike name is ",bname)
class Truck(vehicle):
    def truck_info(self,tname):
        print("Truck name is ",tname)


obj=Car()
obj.vehicle_info()
obj.car_info("COOPER")

obj2=Bike()
obj2.bike_info("Ninja")
obj2.vehicle_info()

obj3=Truck()
obj3.truck_info("Volvo")
obj3.vehicle_info()