# operatory logiczne

# and, daje True tylko jeśli wszystkie są True
print( True and True) # True
print( True and False) # False
print( False and True) # False
print( False and False) # False

print(10 >= 5 and 3 < 9) # True
print(12 < 20 and 5 > 10) # False
print(3 == 5 and 6 < 1) # False


taskCompleted = True
linesOfCodeWritten = 100

if taskCompleted == True and linesOfCodeWritten >= 50:
    print("Go home")

hourOfDay = 15
if taskCompleted == True and linesOfCodeWritten >= 60 and hourOfDay >= 15:
    print("Go home")

# or, True jeśli którykolwiek z warunków jest True
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False

print (10 >= 10 or 5 > 3) # True

if 10 > 5 or "Ania" != "Ola":
    print("True or True")

if 3 == 5 or "Ania" == "Ola":
    print("False or False") # Kod się nie uruchomi


# not, odwraca wynik
print(not True) # False
print(not False) # True

print(not(3 == 3)) # False
print(not(5 > 10)) # True
print(not(10 >= 6 and "Ola" != "Ania")) # False

taskCompleted = False

if taskCompleted == True:
    print("Go home")

if not taskCompleted:
    print("Stay a bit longer and finish")
