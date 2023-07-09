data = ("Ala", "Ola", "Kasia")
# data[0] = "Rafał" 
# TypeError: 'tuple' object does not support item assignment

names = data + ("Rafał",) # dodając jeden element krotki nie zapomnij o przecinku!
print(names)
print(len(names))
print(type(names))

numbers = 1, 2, 3 # nie potrzeba nawiasów
print(type(numbers))

emptyTuple = ()
print(emptyTuple)
print(type(emptyTuple))

print(names[1])
print(names[-1])
print(names[1:3])

cars = ( ("Dodge", "Ford"), ("Pontiac") )
print(cars[0][0])

if "Ford" in cars[0]:
    print("Ford w krotce nr 1")

del cars
# print(cars)
# NameError: name 'cars' is not defined.

# del names[0]
# TypeError: 'tuple' object doesn't support item deletion

# Mnożenie krotek:
tupleX3 = names * 3
print(tupleX3)
