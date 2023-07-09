# Napisz program, który pobiera od użytkownika długość boku kwadratu, a następnie rysuje ten kwadrat za pomocą znaków gwiazdki (*).

size = input("Podaj liczbę:")

text = "*"

i = 0

while i < int(size):
    print(text * int(size))
    i += 1