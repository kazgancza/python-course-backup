names = ("Ola", "Ania", "Kasia")

fullNames = list(map(lambda a: a + " Kowalska", names))

longFullNames = list(filter(lambda a: len(a) > 12, fullNames))

print(longFullNames)