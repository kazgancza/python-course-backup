
str = "Hello World!"
print(str)
print(len(str)) # funkcja len podaje ilość znaków w zmiennej (12)
print(type(str))

print(str[0]) #Pierwsza litera
print(str[11]) #Ostatnia litera (trzeba odjąć jeden od 12, bo zaczynamy od zera)


print(str[len(str) - 1]) # Wyświetlenie ostatniego znaku

print(str[0:5]) # Hello

print(str * 4)

strX3 = str * 3

print(strX3)

str2 = str + " and Hello again!"

print(str2)

print(str2[6:]) #bez cyfry po : automatycznie daje do końca łańcucha znaków

print(str2[::3]) # ::3 daje co trzecią licząc od pierwszej

multiLine = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)


multiLine2 = "Pierwsza linia\nDruga linia\nTrzecia linia"
# \n kolejna linia
# \t tabulacja
# \"CUDZYSŁÓW\\"
# \\ wyświetla \

print(multiLine2)