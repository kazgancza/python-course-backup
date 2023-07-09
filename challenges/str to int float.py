number = int(input("Podaj liczbę całkowitą: "))

def calculateSquareArea(number):
    return number ** 2

print(calculateSquareArea(number))

number = float(input("Podaj liczbę dziesiętną: "))

decinalNum = calculateSquareArea(number)
print(round(decinalNum, 2))