# nieupożądkowany zbiór unikalnych wartości


setData = { 2, 3, 1, 4, 5 }
setData.add(22)

setData.discard(1)
print(type(setData))
print(setData)

for v in setData:
    print(v)

frozenData = frozenset(setData) # konwersja na zbiór bez możliwości zmiany elementów
print(type(frozenData))
# frozenData.add(56) # 'frozenset' object has no attribute 'add'

for value in frozenData:
    print(value)


