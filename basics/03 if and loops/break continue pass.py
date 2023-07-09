data = [0,1,2,3,4,5]

for i in data:
    if i == 3:
        break # wychodzi z pętli
    print(i*2)

print("")

for i in data:
    if i == 3 or i == 5:
        continue # pomija iterację i przechodzi do kolejnej
    print(i)

if 10 > 2:
    pass # pusty wypełniacz, wpisuje się go, żeby nie wywaliło błędu przez brak kodu
