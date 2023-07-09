# WAŻNE

# immutable: int, float, bool, str, frozenset
# zmiana wartości zmiennej zapisze ją w innym miejscu w pamięci

def modifyStr(strData):
    print(id(strData))
    strData += "!"
    print(id(strData))
    print(strData)


string = "Hello"

modifyStr(string)
print(string)

# mutable: list, set, dict
# przy zmianie wartości zmiennej nie powstanie nowe miejsce w pamięci
# dlatego modyfikując ją w funkcji później pozostanie zmieniona

def mofifyList(listData):
    print(id(listData))
    # listData = [1,2,3,4,5,6]
    # Nie czaje
    listData.append(10)
    print(id(listData))
    

listValue = [0,1,2]
print(id(listValue))
mofifyList(listValue)