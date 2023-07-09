"""
i = 1
while i <= 100:
    if i%3 == 0:
        if i%5 == 0:
            print("FizzBuzz")
        else: print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else: print(i)
    i += 1
"""

i = 1
while i <= 100:
    text = ""
    if i%3 == 0:
        text += "Fizz"
    if i%5 == 0:
        text += "Buzz"
    if text == "":
        print(i)
    else: print(text)
    i += 1
