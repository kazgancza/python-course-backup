
def addNumber(a, b): # def definiuje funkcję, addNumber to nazwa funkcji, w nawiasie wartości w tej funkcji (nieobowiązkowem, ale musi być nawias)
    return a + b

def subNumber(a, b):
    return a - b

def multiplyNumber(a,b):
    return a * b

def add4numbers(num1, num2, num3, num4): # może być więcej wartości funkcji, np. tu 4
    result = num1 + num2 + num3 + num4 # dłuższy zapis, liczy w osobnej linii
    return result

print(addNumber(10,5))

number = subNumber(100, 56) # dłuższy zapis, zapisuje wynik w zmiennej i wyślwietla zmienną linijkę niżej
print(number)

number = multiplyNumber(33, 4)
print(number) # 132

sum = add4numbers(1, number, addNumber(10, 6), 9)
print(sum)
