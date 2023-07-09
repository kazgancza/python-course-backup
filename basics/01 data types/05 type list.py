
list =["Ola", "Ania", 23, 99, "Rafał"]
print( type(list))
print( list)

print( list[0]) # Ola
print( len(list)) # długość listy = 5
print( list[4]) # ostatni element
print( list[len(list)-1]) # ostatni element niezależnie od ilości


print( list[-1]) # ostatni element niezależnie od ilości
print( list[-2]) # przedostatni, itd.
# print( list[-6]) # IndexError: list index out of range


print( list[1:4]) # ['Ania', 23, 99]
print( list[2:]) # od 2 (czyli trzeci) do końca

list[0] = "Kasia" # zmiana jednego elementu listy
print(list)

del list[2] # usuwa konkretny element listy
print(list)

print( 99 in list ) # True/False, czy coś znajduje się w liście

print (99 in list)
print ("Rafał" in list)
print ("Ola" in list)


if "Ania" in list:
    print("Ania znajduje się w liście")


for v in list:
    print(v)


data = [
    ["Daniel", "Rafał"],
    ["Kasia", "Ania"],
    ["Ola", "Adam"]
    ]

print(len(data)) # 3 bo są 3 listy
print(len(data[1])) # 2 bo są dwa elementy w drugiej liście
print(data[0][1])

# dodawanie list
data1 = [1, 2, 3]
data2 = [4, 5, 6]

numbers = data1 + data2

print(numbers)

# monożenie list
numbersX2 = numbers * 2

print(numbersX2)

