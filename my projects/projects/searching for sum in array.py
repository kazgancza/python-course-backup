import random

arrayOfNumbers = []
i = 1
l = 100
while len(arrayOfNumbers) <= l:
    arrayOfNumbers.append(i)
    i += 1

targetNumber = random.randint(1, l)

for i in arrayOfNumbers:
    for e in arrayOfNumbers:
        if i + e == targetNumber:
            print(i, "+", e, "=", targetNumber) 