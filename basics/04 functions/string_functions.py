print("Hello" + "World")
print("Hello" * 3)

string = "Hello World!"
print(string[0]) # H
print(string[0:5]) # Hello

print("Hello" in string) # True
print("Hello" not in string) # False

multiLine = """line1
line2
line3
"""

print("ala".capitalize()) # Ala
print("Ola ma kota, Ola ma psa".count("Ola")) # 2 (Liczy ilość podanego tekstu w stringu)

print("Hello".center(20, "-")) # Centruje i wypełnia -

print(string.startswith("Hello")) # True
print(string.endswith("World!")) # True


print(string.find("Ola")) # -1, bo nie ma
print(string.find("World")) # 6, czyli indeks kiedy się zaczyna
print("Ola ma psa, Ola ma kota".rfind("Ola")) # 12, bo szuka od końca

print("1234553243".isalnum()) # True; są same liczby
print("kot".isalpha()) # True; są same znaki alfabetu

print("test".islower()) # True
print("Test".islower()) # False
print("TEST".isupper()) # False

print("TEST".isspace()) # False
print("      \n\n\t ".isspace()) # True

print("-|".join(["Ala", "Ola", "Adam"])) # Ala-|Ola-|Adam

print("Hello World".lower()) # hello world
print("Hello World".upper()) # HELLO WORLD
print("Hello World".swapcase()) # hELLO wORLD

print("    \n Hello World \n\n".lstrip()) # Usuwa białe znaki po lewej
print("    \n Hello World \n\n".rstrip()) # Usuwa białe znaki po prawej
print("    \n Hello World \n\n".strip()) # Usuwa białe znaki po obu stronach


print("Ola ma psa, Ola ma kota".replace("Ola", "Kasia")) # zamienia Ola na Kasia

print("My name is {myName}, I'am from {country}".format(myName = "Kuba", country = "Poland"))
print("My name is {myName}, My postal code is {code}".format(myName = "Kuba", code = 83104))
print("My name is {0}, My postal code is {1}".format("Kuba", 83104)) # Też zadziała
print("My name is {}, My postal code is {}".format("Kuba", 83104)) # Też zadziała