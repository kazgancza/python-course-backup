import os
import pickle


script_dir = os.path.dirname(__file__)


class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def __str__(self):
        return str(f"{self.name} {self.surname} {self.city}")
    
person1 = Person("Kasia", "Nowak", "Toruń")
person2 = Person("Michał", "Michalski", "Gdańsk")
person3 = Person("Ola", "Mucha", "Warszawa")

fh = open(f"{script_dir}/people.dat", "wb")
pickle.dump(person1, fh)
pickle.dump(person2, fh)
pickle.dump(person3, fh)
fh.close()


fh = open(f"{script_dir}/people.dat", "rb")
person1_from_file = pickle.load(fh)
person2_from_file = pickle.load(fh)
person3_from_file = pickle.load(fh)
fh.close()

print(person1_from_file)
print(person2_from_file)
print(person3_from_file)