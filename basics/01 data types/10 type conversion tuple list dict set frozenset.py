# konwersja na tuple
listData = [1,2,3,4,5,6]

tupleData = tuple(listData)
print(type(tupleData))
print(tupleData)

# konwersja na set
otherList = list(("Ola", 23, 234))
print(type(otherList))
print(otherList)

setData = set(otherList)
print(type(setData))
print(setData)

# konwersja na frozenset
frozenSetData = frozenset(tupleData)
print(type(frozenSetData))
print(frozenSetData)

# konwersja na tuple (krotka)
tupleData = (("Ola", 1234), ("Adam", 2345))

dictData = dict(tupleData)
print(dictData)
print(dictData["Ola"])
