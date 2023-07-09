
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.top_speed = 10
        self.num_wheels = 4

    def print_vehice_info(self):
        print(f"print_vehicle_info: {self.brand}, {self.name},\
 {self.top_speed}, {self.num_wheels}")
        
    def print_num_wheels(self):
        print(f"Vehice.num_wheels: {self.num_wheels}")
        
vehicle1 = Vehicle("Ford", "Mustang")
vehicle1.print_vehice_info()

class Car(Vehicle):
    def print_car_info(self):
        self.top_speed = 230
        print(f"print_car_info: {self.brand}, {self.name},\
 {self.top_speed}, {self.num_wheels}")
        
    def print_vehice_info(self):
        print(f"Car.print_vehicle_info: {self.brand}, {self.name},\
 {self.top_speed}, {self.num_wheels}")
        
car1 = Car("Audi", "A8")
car1.print_car_info()
car1.print_vehice_info()
car1.print_num_wheels()


class SuperCar(Car):
    def reach_speed_300(self):
        self.top_speed = 300
        print("Super car reached 300!")

super_car1 = SuperCar("Ferrari", "F40")
super_car1.reach_speed_300()
super_car1.print_vehice_info()

super_car1.print_num_wheels()
