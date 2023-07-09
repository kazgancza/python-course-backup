# Napisz program, który pobierze od użytkownika napis, a następnie wyświetli na ekranie inny napis,
# który powstanie poprzez zamianę każdej litery na dwie kopie siebie.
# Na przykład dla napisu "Hello" program powinien wyświetlić "HHeelllloo".

text = input("Wprowadź napis:")
text_x2 = ""

for letter in text:
    letter_x2 = letter * 2
    text_x2 += letter_x2

print(text_x2)
