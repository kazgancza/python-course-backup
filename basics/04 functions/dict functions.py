data = {
    "name": "Ola",
    "city": "Warszawa"
}
print(data["name"])
dataPostalCode = "postalCode"
data[dataPostalCode] = 12345
print(data)
print(len(data))

del data["city"]
print(data)
data.clear()
print(data)

data = {
    "name": "Kasia",
    "city": "Kraków"
}
dataCopy = data.copy() # Płytka kopia, elementy mają to samo miejsce w pamięci
print(dataCopy)
print(data["name"] is dataCopy["name"])
print(data is dataCopy) # False (lista jest w innym miejscu w pamięci)

data2 = dict.fromkeys(("name","city","code"))
print(data2)

data3 = dict.fromkeys(("name","city","code"), 0) # Druga wartość to domyślna
print(data3)

print(data2.get("x", "DEFAULT")) # Zwraca wartość podanego klucza, druga wartość to domyślna

print(data2.keys())
print(data2.values())