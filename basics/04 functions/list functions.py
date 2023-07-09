list1 = [0,1,2,3,4,5]
print(list1[3])
print(list1[1:5])

list1[0] = 9
print(list1)

del list1[1]
print(list1)
print(len(list1))
print(max(list1))
print(min(list1))

print(list(("Ala", "Ola"))) # Zamiana krotki na listę

print([0,1,2] + [3,4]) # Dodawanie list
print([0,1] * 3) # Mnożenie list

print(9 in [0,1]) # Sprawdzanie czy się znajduje w liście
print(0 not in [0,1]) # Sprawdzanie czy NIE się znajduje w liście

list1.append(99)
print(list1)
print(list1.count(3)) # Liczy ilość wystąpień czegoś w liście

list1.extend([7,8,9])
print(list1)

list1.insert(3, 9) # Wkłada 9 na index 3 nie usuwając go, tylko przesuwając
print(list1)

print(list1.index(9)) # Pokazuje index dla podanej wartości (pierwszy od lewej)

list1.reverse() # Odwraca kolejność
print(list1)

list1.sort() # Sortuje od min do max
print(list1)

num = list1.pop() # Zwraca i usuwa wartość pod indeksem (domyślnie ostatnią)
print(num)
print(list1)
