class vehicle:
    def vehicle_info(self):
        print("Inside vechile class")
class car(vehicle):
    def car_info(self):
        print("Inside Car class")

class SpotsCar(car):
    def sports(self):
        print("Function inside sports car class")
obj=SpotsCar()
obj.sports()
obj.car_info()
obj.vehicle_info()