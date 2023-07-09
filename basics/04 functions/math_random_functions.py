import math
import random


print(type(str(12)))
print(type(str([12, 34])))

number = int("123")
print(type(number))

number += 10
print(number)

floatNum = float("45.67")
print(type(floatNum))
floatNum *= 2
print(floatNum)

# wartość bezwzględna
print(abs(9))
print(abs(-9.1))

# zaokrąglanie do GÓRY
# najmniejsz l. całkowita nie mniejsza niż podana
print(math.ceil(11.000001)) # 12
print(math.ceil(9.999)) # 10
print(math.ceil(-1.000001)) # -1

# zaokrąglanie w DÓŁ
# największa l. całkowita nie większa niż podana
print(math.floor(11.000001)) # 11
print(math.floor(5.12)) # 5
print(math.floor(-5.12)) # -6

# maksymalna wartość w sekwencji, liście, krotce...
print(max(10,1,-9,33,89,0)) # 89
print(max([10,1,-9,33,89,0])) # 89
print(max((10,1,-9,33,89,0))) # 89

# minimalna wartość ....
print(min(10,1,-9,33,89,0)) # -9
print(min([10,1,-9,33,89,0])) # -9
print(min((10,1,-9,33,89,0))) # -9

# potęga
print(4**3) # 64
print(pow(4,3)) # 64

# pierwiastek kwadratowy
print(math.sqrt(256)) # 16

# zaokrąglanie do x liczby po przecinku
print(round(12.7891234, 3))


#_________________________________________________

# randomowa od 0 do 1
print(random.random())

# randomowa z listy, itp
print(random.choice([0,1,2,3,4]))
print(random.choice(["Ola", "Ania", "Adam"]))

# randomowa z zakresu: od, do, krok
print(random.randrange(-10, 30, 5))

# losowa kolejność w liście
listData = [0,1,2,3,4,5,6]
random.shuffle(listData)

print(listData)