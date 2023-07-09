
for v in [1,2,3,4]:
    print(v * 2)

for v in ("Ania", "Ola", "Rafał"):
    print(v)

for el in {3,4,5,6,"Ola"}:
    print(el)

for v in "Hello":
    print(v)
else:
    print("koniec pętli")

dictData = {
    "Ania": "ania@example.com",
    "Adam": "adam@example.com"
}

for key in dictData:
    print(key)

for key in dictData.keys(): # to samo co wyżej
    print(dictData[key])

for key, value in dictData.items():
    print(key, " : ", value)

for v in dictData.values():
    print(v)

