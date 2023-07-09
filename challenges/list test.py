data = [0, 1, 2, 3, 4, 5, 6]

print("Długość listy:", len(data))

del data[1]
print("Długość listy po skasowaniu elementu:", len(data))

if 3 in data:
    print("3 jest w liście data")

for v in data:
    print(v)

print("Przerwa")

for v in data:
    print(v*2)

