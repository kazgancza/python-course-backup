def cToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def fToC(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

print("20\xB0C to " + str(cToF(20)) + "\xB0F")
print("86\xB0F to " + str(fToC(86)) + "\xB0C")

