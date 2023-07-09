
class Vehicle:
    def __init__(self):
        pass

    @property
    def gears(self):
        print(f"getter: {self.__gears}")
        if (self.__gears > 0):
            return self.__gears
        else: return -1

    @gears.setter
    def gears(self, new_gears):
        print(f"new_gears: {new_gears}")
        if (new_gears > 0): self.__gears = new_gears

vehicle1 = Vehicle()
vehicle1.gears = 8
print(vehicle1.gears)