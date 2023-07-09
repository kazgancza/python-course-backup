def findLargest(num1, num2):
    if num1 > num2:
        print("num1 jest większą liczbą:")
        return num1
    elif num2 > num1:
        print("num2 jest większą liczbą:")
        return num2
    else:
        print("Liczby są równe")
        return num1

print(findLargest(3,10))
print(findLargest(12,7))

