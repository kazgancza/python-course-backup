# int
floatNum =  23.999999999999
intNum = int(floatNum)
print(type(intNum))
print(intNum)

print(int(" 678    "))
print(int(100))


#float
intNum = 56
float1 = float(intNum)
print(type(float1))
print(float1)

str1 = "123.565678"
float2 = float(str1)
print(type(float2))
print(float2)


# Konkatenacja (łączenie), tylko te same typy zmiennych; tu: str
print( "Wartość float1: " + str(float1) + " " + str(78) + " " + str([1, 2, 3, 4]) )

# używając przecinka mogą być różne typy zmiennych
print("Wartość float1:", float1, " ", 78, " ", [1,2,3,4])