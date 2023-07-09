from functools import reduce

# lambda to jednolinijkowa anonimowa funkcja,
# przypisując ją do zmiennej zadziała jak zwykła funkcja
sum = lambda a,b: a + b

print(sum(4,5)) # 9
print(sum(14,5)) # 19


def generateLambda(num):
    return lambda a: a * num

doubler = generateLambda(2)
print(doubler(4)) # 8



listData = [0,1,2,3]


# map iteruje po każdym elemencie (listData) wykonując (lambda...)
# zwraca każdy element osobno, dlatego list tworzy je w liście
result = list( map(lambda a: a * 3, listData) )

print(result)


# filter zostawi tylko te elementy które spełniają warunek
result = list( filter(lambda a: a > 1, listData) )

print(result)

# redukuje do jednego łancucha znaków w tym przypadku
result = reduce(lambda x,y: x + " " + y, ("Ola", "Ania"))

print(result)