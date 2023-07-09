
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5

    def __get_gears_info_str(self):
        return f"Gears number: {str(self.__gears)}"

    def print_info(self):
        print(self.brand, self.name, self.__get_gears_info_str())
    
vehicle1 = Vehicle("Ford", "T1")
# print(vehicle1.__gears()) # błąd
# vehicle1.__get_gears_info_str() # błąd
vehicle1.print_info()
print(vehicle1._Vehicle__gears) # obejście tego

class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
#        print(self.__gears) # błąd

car1 = Car("Audi", "A4")