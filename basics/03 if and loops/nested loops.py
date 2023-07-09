
listsData = [
    [0,1,2,3,4],
    ["Ola", "Ala", "Adam"],
    [10, "Adam", 20, "Ania"]
]

for listData in listsData: # każda iteracja daje dostęp do kolejnej listy w liście
    for v in listData: # każda iteracja wypisuje zawartość listy
        print(v)
